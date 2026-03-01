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