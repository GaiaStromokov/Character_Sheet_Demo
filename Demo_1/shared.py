import json
from box import Box
import sys
import os

db = None
pc = None

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def init_db():
    """
    Loads the database from a file and assigns it to this module's 'db' variable.
    """
    # We use 'global' here to specify that we are assigning a new object
    # to the 'db' variable that lives at the top level of THIS FILE,
    # not creating a new local variable. This is the correct use of 'global'.
    global db
    with open(resource_path('Database/db.json'), 'r') as f:
        db = Box(json.load(f))
    print("Database has been loaded and is ready in shared.db")