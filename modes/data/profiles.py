# data/engine_profiles.py

ENGINE_PROFILES = {
    "Unreal": {
        "dimension": ["3D"],
        "realism": ["high"],
        "coding": ["medium", "high"],
        "platform": ["pc", "console"],
        "machine": ["High"]
    },
    "Unity": {
        "dimension": ["2D", "3D"],
        "realism": ["low", "medium","high"],
        "coding": ["high", "medium"],
        "platform": ["mobile", "pc"],
        "machine": ["High","Moderate","Low"]
    },
    "Godot": {
        "dimension": ["2D"],
        "realism": ["low"],
        "coding": ["low", "medium"],
        "platform": ["pc"],
        "machine":["Moderate","Low"]
    }
}
GAME_PROFILE={

    "Small Puzzle Game": {
        "experience": ["beginner", "intermediate"],
        "time_commitment": ["low", "medium"],
        "team_size": ["solo"],
        "goal": ["learning", "portfolio"],
        "genre_interest": ["puzzle"]
    },

    "2D Platformer": {
        "experience": ["beginner", "intermediate"],
        "time_commitment": ["medium"],
        "team_size": ["solo", "small_team"],
        "genre_interest": ["platformer"]
    },

    "Short Horror Game": {
        "experience": ["intermediate", "advanced"],
        "time_commitment": ["medium", "high"],
        "genre_interest": ["horror"]
     },

    "Action Prototype": {
        "experience": ["intermediate", "advanced"],
        "time_commitment": ["high"],
        "genre_interest": ["action"]
     },

    "Small Simulation Game": {
        "experience": ["advanced"],
        "time_commitment": ["high"],
        "team_size": ["small_team"],
        "genre_interest": ["simulation"]
    }

 }