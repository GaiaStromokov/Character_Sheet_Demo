from dearpygui.dearpygui import *
import json
import shared
import sys
import os

from data_updater.components import Milestone_comp, Race_comp, Class_comp, Background_comp
#----
from data_updater.character import init_pc
from Sheet.UI import init_ui, populate_Start

def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def save_db():
    with open(resource_path('Database/db.json'), 'w') as f:
        if shared.db:
            json.dump(shared.db.to_dict(), f, indent=4)
            print("Database saved.")
        else:
            print("Database was not loaded, nothing to save.")

def start_game():
    shared.init_db()
    init_pc()
    shared.pc.start_configuration()
    init_ui()
    populate_Start()

create_context()
with font_registry():
    font_choice = add_font(resource_path("config/Helvetica.ttf"), 13)
configure_app(init_file=resource_path("config/config_save.ini"), docking=True, docking_space=True)
create_viewport(title="rpg", width=1200, height=840)
bind_font(font_choice)
setup_dearpygui()

start_game()

set_exit_callback(save_db)
show_viewport()
start_dearpygui()
destroy_context()
save_init_file(resource_path("config/config_save.ini"))