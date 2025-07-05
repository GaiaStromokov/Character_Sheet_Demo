from dearpygui.dearpygui import *
import shared
import json, sys, os

from manager.components import Milestone_comp, Race_comp, Class_comp, Background_comp
from manager.character import init_pc
from Sheet.UI import init_ui, populate_Start

def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def on_exit_callback():
    shared.save_db()
    save_init_file(resource_path("utils/config_save.ini"))
    stop_dearpygui()

create_context()
with font_registry():
    font_choice = add_font(resource_path("utils/Helvetica.ttf"), 13)

configure_app(init_file=resource_path("utils/config_save.ini"), docking=True, docking_space=True)
create_viewport(title="rpg", width=1200, height=840)
set_exit_callback(on_exit_callback)

bind_font(font_choice)
setup_dearpygui()

shared.init_db()
init_pc()
shared.pc.start_configuration()
init_ui()
populate_Start()

show_viewport()
start_dearpygui()
destroy_context()