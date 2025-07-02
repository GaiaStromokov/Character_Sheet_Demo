# backend.py
from Sheet.get_set import *

import shared

    
def stage_Level(sender, data, user_data, pop_fields):
    old_obj = gLevel()
    print(f"old Level: {old_obj} -> new Level: {data}")
    if old_obj != data:
        print("Changing Level")
        set_Level("stage_Level",data,"NA")
        check_Class()
        shared.pc.new_Level()
        pop_fields("Level")
    else: print("Not changing Level")
    


def stage_Race(sender, data, user_data, pop_fields):
    old_obj = gRace()
    print(f"old race: {old_obj} -> new race: {data}")
    if old_obj != data:
        print("Changing race")
        set_Race("stage_Race",data,"NA")
        set_Subrace("clear_Subrace","","NA")
        shared.pc.new_Race()
        pop_fields("Race")
    else: print("Not changing race")

def stage_Subrace(sender, data, user_data, pop_fields):
    old_obj = gSubrace()
    print(f"old subrace: {old_obj} -> new subrace: {data}")
    if old_obj != data:
        print("Changing subrace")
        set_Subrace("stage_Subrace",data,"NA")
        shared.pc.new_Race()
        pop_fields("Race")
    else: print("Not changing subrace")

def stage_Class(sender, data, user_data, pop_fields):
    old_obj = gClass()
    print(f"old class: {old_obj} -> new class: {data}")
    if old_obj != data:
        print("Changing class")
        set_Class("stage_Class",data,"NA")
        check_Class()
        set_Subclass("clear_Subclass","","NA")
        shared.pc.new_Class()
        pop_fields("Class")
    else: print("Not changing Class")


def check_Class():
    set_valid_class()
    if get_valid_class() == False:
        set_Subclass("check_Class","","NA")

def stage_Subclass(sender, data, user_data, pop_fields):
    old_obj = gSubclass()
    print(f"old subclass: {old_obj} -> new subclass: {data}")
    if old_obj != data:
        print("Changing subclass")
        set_Subclass("stage_Subclass",data,"NA")
        shared.pc.new_Class()
        pop_fields("Class")
    else: print("Not changing subclass")


def stage_Background(sender, data, user_data, pop_fields):
    old_obj = gBackground()
    print(f"old background: {old_obj} -> new background: {data}")
    if old_obj != data:
        print("Changing background")
        set_Background("stage_Background",data,"NA")
        shared.pc.new_Background()
        pop_fields("Background")
    else: print("Not changing background")


def stage_Background_Prof_Select(sender, data, user_data, pop_fields):
    set_Background_Prof_Select("Stage_Background_Prof_Select", data, user_data)
    shared.pc.update_Background_Prof()
    pop_fields("Background Prof Select")


def stage_Atr_Base(sender, data, user_data, pop_fields):
    set_Atr_Base("Stage_Atr_Base", data, user_data)
    shared.pc.update_Atr()
    pop_fields("Atr")

def stage_Race_Asi(sender, data, user_data, pop_fields):
    set_Rasi("Stage_Rasi",data,user_data)
    shared.pc.update_Atr()
    pop_fields("Atr")

def stage_Race_Use(sender, data, user_data, pop_fields):
    set_Race_Use("Stage_Race_Use",data,user_data)




def stage_Milestone_Level_Select(sender, data, user_data, pop_fields):
    print(f"data={data}")
    if data == "Clear":
        clear_Milestone_Level_Select("Stage_Milestone_Level_Select_Clear", data, user_data)
    else:
        set_Milestone_Level_Select("Stage_Milestone_Level_Select", data, user_data)
    shared.pc.update_Milestone_Feat()
    pop_fields("All")

def stage_Milestone_Feat_Select(sender, data, user_data, pop_fields):
    set_Milestone_Feat_Select("Stage_Milestone_Feat_Select", data, user_data)
    shared.pc.update_Milestone_Feat()
    pop_fields("Milestone")


def stage_Milestone_Feat_Choice(sender, data, user_data, pop_fields):
    set_Milestone_Feat_Choice("Stage_Milestone_Feat_Choice", data, user_data)
    shared.pc.update_Milestone_Feat()
    pop_fields("Milestone")
    
def stage_Milestone_Feat_Use(sender, data, user_data, pop_fields):
    set_Milestone_Feat_Use("Stage_Milestone_Feat_Use", data, user_data)
    


def stage_Milestone_Asi_Select(sender, data, user_data, pop_fields):
    set_Milestone_Asi_Select("Stage_Milestone_Asi_Select", data, user_data)
    shared.pc.update_Atr()
    pop_fields("Atr")



def stage_Race_Spell_Use(sender, data, user_data, pop_fields):
    set_Race_Spell_Use("stage_Race_Spell_Use", data, user_data)

def stage_Race_Spell_Select(sender, data, user_data, pop_fields):
    set_Race_Spell_Select("stage_Race_Spell_Select", data, user_data)
    pop_fields("Race")

def stage_Class_Use(sender, data, user_data, pop_fields):
    set_Class_Use("Stage_Class_Use", data, user_data)


def stage_Class_Skill_Select(sender, data, user_data, pop_fields):
    set_Class_Skill_Select("Stage_Class_Skill_Select", data, user_data)
    shared.pc.update_Class_Select()
    pop_fields("Class")

def stage_Class_select(sender, data, user_data, pop_fields):
    set_Class_select("Stage_Class_select", data, user_data)
    shared.pc.update_Class_Select()
    pop_fields("Class")






def stage_Spell_Learn(sender, data, user_data, pop_fields):
    set_Spell_Learn("stage_Spell_Learn", data, user_data)
    shared.pc.update_Spell_Learn()
    pop_fields("Spell Learn")
    pop_fields("Spell Prepare")
    
    
def stage_Spell_Prepare(sender, data, user_data, pop_fields):
    set_Spell_Prepare("stage_Spell_Prepare", data, user_data)
    shared.pc.update_Spell_Prepare()
    pop_fields("Spell Prepare")
    pop_fields("Spell Cast")

def stage_Spell_Cast(sender, data, user_data, pop_fields):
    set_Spell_Cast("stage_Spell_Cast", data, user_data)
    shared.pc.update_Spell_Cast()
    pop_fields("Spell Cast")



def stage_Long_Rest(sender, data, user_data, pop_fields):
    set_Long_Rest("stage_Long_Rest", data, user_data)
    pop_fields("Long Rest")

def stage_Health_Mod(sender, data, user_data, pop_fields):
    set_Health_Mod("stage_Health_Mod", data, user_data)


def stage_Arcane_Ward(sender, data, user_data, pop_fields):
    set_Arcane_Ward("stage_Arcane_Ward", data, user_data)
    pop_fields("Arcane Ward")
    
    
    
def stage_Player_Prof_Select(sender, data, user_data, pop_fields):
    set_Player_Prof_Select("stage_Player_Prof_Select", data, user_data)
    shared.pc.recalculate_stats()
    pop_fields("Generic")
    
