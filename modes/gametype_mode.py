# modes/game_type.py

from modes.data.questions import GAME_TYPE
from modes.data.profiles import GAME_PROFILE


def collect_user_profile(questions):
    user_profile = {}

    for question in questions:
        print("\n" + question["text"])

        for key, option in question["options"].items():
            print(f"  {key}) {option['label']}")

        if question["multi"]:
            raw = input("Select all that apply (comma separated): ")
            selected = raw.lower().replace(" ", "").split(",")
        else:
            selected = [input("Select one option: ").lower().strip()]

        for choice in selected:
            option = question["options"].get(choice)
            if not option:
                continue

            for trait_key, trait_value in option["traits"].items():
                user_profile.setdefault(trait_key, []).append(trait_value)

    return user_profile


def score_profiles(user_profile, profiles):
    scores = {}
    match_details = {}
    conflict_details = {}

    for name, traits in profiles.items():
        score = 0
        matches = []
        conflicts = []

        for trait_key, user_values in user_profile.items():
            profile_values = traits.get(trait_key, [])

            for value in user_values:
                if value in profile_values:
                    score += 2
                    matches.append(f"{trait_key}: {value}")
                else:
                    conflicts.append(f"{trait_key}: {value}")

        scores[name] = score
        match_details[name] = matches
        conflict_details[name] = conflicts

    return scores, match_details, conflict_details


def generate_reasoning(winner, scores, matches, conflicts):
    sorted_profiles = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print("\nScores:")
    for profile, score in sorted_profiles:
        print(f"{profile}: {score}")

    print(f"\nRecommended Game Type: {winner}")

    print("\nWhy this fits you:")
    for match in matches[winner]:
        print(f"- Matches your preference for {match}")

    for profile, _ in sorted_profiles[1:3]:
        print(f"\nWhy not {profile}?")
        for conflict in conflicts[profile][:3]:
            print(f"- Conflicts with your {conflict}")


def run_game_type_mode():
    user_profile = collect_user_profile(GAME_TYPE)

    scores, matches, conflicts = score_profiles(
        user_profile,
        GAME_PROFILE
    )

    winner = max(scores, key=scores.get)

    generate_reasoning(winner, scores, matches, conflicts)