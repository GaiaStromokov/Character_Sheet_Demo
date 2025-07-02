from dictionary_data.import_central import *
import json, math
import shared
from data_updater.components.registry import race_registry, subrace_registry, class_registry, subclass_registry, feat_registry, background_registry
from data_updater.components.Milestone_comp import Milestone_config
from Sheet.get_set import *

class Character():
    def __init__(self):
        pass

    def start_configuration(self):
        self.init_schema()
        self.Background.Create()
        self.Race.Select()
        self.Class.Select()
        self.Milestone.on_init()
        self.Race.Upd()
        self.Class.Upd()
        self.recalculate_stats()
        self.init_spells()
        self.update_spells()

    def new_Level(self):
        self.Race.Upd()
        self.Class.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()
        self.update_spells()

    def init_schema(self):
        race_func = race_registry.get(gRace())
        if race_func: self.Race = race_func()
        class_func = class_registry.get(gClass())
        if class_func: self.Class = class_func()
        self.Milestone = Milestone_config()
        
        background_func = background_registry.get(gBackground())
        if background_func: self.Background = background_func()

    def new_Race(self):
        self.wipe_data("Race Abil")
        race_func = race_registry.get(gRace())
        if race_func: self.Race = race_func()
        self.Race.Select()
        self.Race.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()

    def new_Class(self):
        self.wipe_data("Class Abil")
        self.wipe_data("Class Spell")
        class_func = class_registry.get(gClass())
        if class_func: self.Class = class_func()
        self.Class.Select()
        self.Class.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()
        self.init_spells()
        self.update_spells()
    
    def new_Background(self):
        self.wipe_data("Background Data")
        background_func = background_registry.get(gBackground())
        if background_func: self.Background = background_func()
        self.Background.Create()
        self.recalculate_stats()
        

    def update_Atr(self):
        self.wipe_data("Atr")
        self.Milestone.Upd()
        self.recalculate_stats()
        self.update_spells()

    def update_Class_Select(self):
        self.Class.Select()
        self.Class.Upd()
        self.Milestone.Upd()
        self.recalculate_stats()

    def update_Spell_Learn(self):
        pass

    def update_Spell_Prepare(self):
        pass

    def update_Spell_Cast(self):
        pass

    def update_Background_Prof(self):
        self.Background.Create()
        self.recalculate_stats()
        

    def init_spells(self):
        if can_cast(): self.spell_data = spell_data_default

    def update_Milestone_Feat(self):
        self.update_Atr()
        

    def update_spells(self):
        if gClass() in spellcast_L: self.Class.Spell_config()
        elif gSubclass() in spellcast_L: self.Subclass.Spell_config()
        else: pass
    

    def wipe_data(self, source):
        if source == "Race Abil": gRace_data().Abil={}
        if source == "Class Abil": gClass_data().Abil={}
        if source == "Class Spell": shared.db.Spell=spell_default
        if source == "Background Data": 
            shared.db.Background.Data={"Prof": {}, "Equipment": {}}

    def recalculate_stats(self):
        
        self.pull_atr_data()
        self.sum_Proficiency()
        self.sum_Skill()
        self.sum_Speed()
        self.sum_Vision()
        self.sum_Initiative()
        self.sum_HP()

    def pull_atr_data(self):
        cdata = gRace_data().Rasi
        for key in Atr_L:
            gAtr()[key]["Rasi"] = 0
            for i, rasi_list in enumerate(cdata):
                if key in rasi_list:
                    gAtr()[key]["Rasi"] = i + 1
                    break
        
        for key in Atr_L:
            val = gAtr()[key]["Base"] + gAtr()[key]["Rasi"] + gAtr()[key]["Milestone"]
            mod = (val- 10) // 2
            gAtr()[key]["Val"] = val
            gAtr()[key]["Mod"] = mod

    def sum_Proficiency(self):
        for i in Prof_L:
            gProf()[i] = gProf()["Player"][i] + gProf()["Race"][i] + gProf()["Class"][i] + gProf()["Background"][i] + gProf()["Feat"][i]

    def sum_Skill(self):
        all_skills = set(gSkill()["Race"] + gSkill()["Class"] + gSkill()["Background"] + gSkill()["Feat"])
        for skill in Skill_L:
            gSkill()[skill]["Sum"] = skill in all_skills
            gSkill()[skill]["Mod"] = gAtr()[dict_Skill[skill]["Atr"]]["Mod"]
            if gSkill()[skill]["Sum"]:
                gSkill()[skill]["Mod"] += gPB()

    def sum_Speed(self):
        for speed in Speed_L:
            gSpeed()[speed]["Val"]=gSpeed()[speed]["Race"]+gSpeed()[speed]["Class"] + gSpeed()[speed]["Feat"]

    def sum_Vision(self):
        for vision in Vision_L:
            gVision()[vision]["Val"]=gVision()[vision]["Race"]+gVision()[vision]["Class"]+gVision()[vision]["Feat"]

    def sum_Initiative(self):
        gInitiative()["Val"] = gAtr()["DEX"]["Mod"]+gInitiative()["Race"]+gInitiative()["Class"]+gInitiative()["Feat"]

    def sum_HP(self):
        sum = gHP()["Player"] + gHP()["Race"] + gHP()["Feat"]
        gHP()["Sum"] = sum
        gHP()["Current"] = sum
        


def init_pc():
    # CHANGE THIS: if db is None:
    # TO THIS:
    if shared.db is None:
        print("ERROR: Cannot initialize PC because the database (shared.db) has not been loaded.")
        return

    print("Initializing Player Character (PC)...")
    # This line was already correct! It assigns to the module's attribute.
    shared.pc = Character()