from box import Box
import json
import sys
import os

db = None
pc = None

def get_db_path():
    if getattr(sys, 'frozen', False):
        # Running as a packaged .exe. The .exe is in the 'dist' folder.
        base_path = os.path.dirname(sys.executable)
        return os.path.join(base_path, 'db.json')
    else:
        # Running as a .py script. The 'dist' folder is in the project root.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(script_dir, 'dist', 'db.json')

def init_db():
    global db
    db_path = get_db_path()
    try:
        with open(db_path, 'r') as f:
            db = Box(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"FATAL ERROR: Could not load db.json from '{db_path}'.")
        print("Please ensure the 'dist' folder exists and contains a valid 'db.json' file.")
        sys.exit(1)


def save_db():
    if db:
        db_path = get_db_path()
        try:
            with open(db_path, 'w') as f:
                json.dump(db.to_dict(), f, indent=4)
                print("saves")
        except Exception as e:
            print(f"Error saving database: {e}")