from modes.engine_mode import run_engine_mode
from modes.gametype_mode import run_game_type_mode

MODES = {
    "1": {
        "name": "Choose Game Engine",
        "handler": run_engine_mode
    },
    "2": {
        "name": "Choose what game to make next",
        "handler": run_game_type_mode
    }
}

def display_modes():
    print("\nGame Dev Journey Decision Companion")
    print("--------------------------------------")
    for key, mode in MODES.items():
        print(f"{key}. {mode['name']}")
    print("0. Exit")

def main():
    while True:
        display_modes()
        choice = input("\nSelect a mode: ").strip()

        if choice == "0":
            print("Good luck on your game dev journey")
            break

        mode = MODES.get(choice)

        if mode:
            print(f"\n--- {mode['name']} ---\n")
            mode["handler"]()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()