# engine_questions.py

ENGINE_QUESTIONS = [
    {
        "id": "dimension",
        "text": "What type of games interest you?",
        "multi": True,
        "options": {
            "a": {"label": "2D", "traits": {"dimension": "2D"}},
            "b": {"label": "3D", "traits": {"dimension": "3D"}},
        }
    },
    {
        "id": "realism",
        "text": "What visual style do you prefer?",
        "multi": False,
        "options": {
            "a": {"label": "Realistic", "traits": {"realism": "high"}},
            "b": {"label": "Stylized / Simple", "traits": {"realism": "low"}},
        }
    },
    {
        "id": "coding",
        "text": "How comfortable are you with programming?",
        "multi": False,
        "options": {
            "a": {"label": "Love coding", "traits": {"coding": "high"}},
            "b": {"label": "Okay with it", "traits": {"coding": "medium"}},
            "c": {"label": "Prefer visual tools", "traits": {"coding": "low"}},
        }
    },
    {
        "id": "platform",
        "text": "Which platforms are you targeting?",
        "multi": True,
        "options": {
            "a": {"label": "Mobile", "traits": {"platform": "mobile"}},
            "b": {"label": "PC", "traits": {"platform": "pc"}},
            "c": {"label": "Console", "traits": {"platform": "console"}},
        }
    },
    {
        "id": "machine",
        "text": "how good is your pc or laptop?",
        "multi": False,
        "options": {
            "a": {"label": "High", "traits": {"machine": "High"}},
            "b": {"label": "Moderate", "traits": {"machine": "Moderate"}},
            "c": {"label": "Low", "traits": {"machine": "Low"}},
        }
    }
]
GAME_TYPE= [

    {
        "id": "experience",
        "text": "What is your current experience level?",
        "multi": False,
        "options": {
            "a": {"label": "Beginner", "traits": {"experience": "beginner"}},
            "b": {"label": "Intermediate", "traits": {"experience": "intermediate"}},
            "c": {"label": "Advanced", "traits": {"experience": "advanced"}},
        }
    },

    {
        "id": "time",
        "text": "How many hours per week can you commit?",
        "multi": False,
        "options": {
            "a": {"label": "Less than 5", "traits": {"time_commitment": "low"}},
            "b": {"label": "5-15", "traits": {"time_commitment": "medium"}},
            "c": {"label": "15+", "traits": {"time_commitment": "high"}},
        }
    },

    {
        "id": "team",
        "text": "Are you working solo or in a team?",
        "multi": False,
        "options": {
            "a": {"label": "Solo", "traits": {"team_size": "solo"}},
            "b": {"label": "Small team", "traits": {"team_size": "small_team"}},
        }
    },
        {
        "id": "goal",
        "text": "What is your main goal for this project?",
        "multi": False,
        "options": {
            "a": {"label": "Build portfolio", "traits": {"goal": "portfolio"}},
            "b": {"label": "Learn new skills", "traits": {"goal": "learning"}},
            "c": {"label": "Just for fun", "traits": {"goal": "fun"}},
        }
    },

    {
        "id": "genre",
        "text": "What genres interest you?",
        "multi": True,
        "options": {
            "a": {"label": "Puzzle", "traits": {"genre_interest": "puzzle"}},
            "b": {"label": "Platformer", "traits": {"genre_interest": "platformer"}},
            "c": {"label": "Horror", "traits": {"genre_interest": "horror"}},
            "d": {"label": "Action", "traits": {"genre_interest": "action"}},
            "e": {"label": "Simulation", "traits": {"genre_interest": "simulation"}},
        }
    }

]