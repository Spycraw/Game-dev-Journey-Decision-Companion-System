# modes/engine_mode.py

from modes.data.questions import ENGINE_QUESTIONS
from modes.data.profiles import ENGINE_PROFILES


def collect_user_profile():
    user_profile = {}

    for question in ENGINE_QUESTIONS:
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


def score_engines(user_profile):
    scores = {}
    match_details = {}
    conflict_details = {}

    for engine, traits in ENGINE_PROFILES.items():
        score = 0
        matches = []
        conflicts = []

        for trait_key, user_values in user_profile.items():
            engine_values = traits.get(trait_key, [])

            for value in user_values:
                if value in engine_values:
                    score += 2
                    matches.append(f"{trait_key}: {value}")
                else:
                    conflicts.append(f"{trait_key}: {value}")

        scores[engine] = score
        match_details[engine] = matches
        conflict_details[engine] = conflicts

    return scores, match_details, conflict_details


def generate_reasoning(winner, scores, matches, conflicts):
    sorted_engines = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    second = sorted_engines[1][0]
    third = sorted_engines[2][0]

    print("\nScores:")
    for engine, score in scores.items():
        print(f"{engine}: {score}")

    print(f"\nRecommended Engine: {winner}")

    print("\nWhy this fits you:")
    for match in matches[winner]:
        print(f"- Matches your preference for {match}")

    print(f"\nWhy not {second}?")
    for conflict in conflicts[second][:3]:
        print(f"- Conflicts with your {conflict}")

    print(f"\nWhy not {third}?")
    for conflict in conflicts[third][:3]:
        print(f"- Conflicts with your {conflict}")

    print("\nSuggested First Steps:")
    print("- Install the engine")
    print("- Complete beginner tutorial")
    print("- Build small playable prototype in 2 weeks")


def run_engine_mode():
    user_profile = collect_user_profile()

    scores, matches, conflicts = score_engines(user_profile)

    winner = max(scores, key=scores.get)

    generate_reasoning(winner, scores, matches, conflicts)