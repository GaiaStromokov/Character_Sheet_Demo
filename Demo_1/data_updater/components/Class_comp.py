import shared
from Sheet.get_set import *
from dictionary_data.import_central import *
from .registry import class_registry, subclass_registry

def fill_uses(name, num):
    past = gClass_abil().get(name, {}).get("Use", [])
    gClass_abil()[name]["Use"] = (past + [False] * num)[:num]

def fill_select(name, num):
    past = gClass_abil().get(name, {}).get("Select", [])
    gClass_abil()[name]["Select"] = (past + [""] * num)[:num]

def remove_ability(name):
    gClass_abil().pop(name, None)

def ensure_ability(name):
    return gClass_abil().setdefault(name, {})

def ensure_subclass_made():
    if gSubclass():
        subclass_func = subclass_registry.get(f"{gClass()}_{gSubclass()}")
        if subclass_func: shared.pc.Subclass = subclass_func()

def ensure_subclass_Upd():
    if gSubclass(): shared.pc.Subclass.Upd()

def ensure_subclass_Select():
    if gSubclass(): shared.pc.Subclass.Select()

def Wipe_Class():
    gProf()["Class"] = {"Armor": [],"Weapon": [],"Tool": [],"Lang": []}
    gSkill()["Class"] = []
    gInitiative()["Class"]=0
    gSavingThrow()["Class"]=[]

class Fighter():
    def __init__(self):
        ensure_subclass_made()
    def Select(self):
        Wipe_Class()
        shared.db.HD.Die=10
        gProf()["Class"]["Armor"].extend(list(dict_Armor.keys()))
        gProf()["Class"]["Weapon"].extend(list(dict_Weapon.keys()))
        gSkill()["Class"].extend([s for s in gClass_Skill() if s in dl[f"{gClass()} Skills"]])
        ensure_subclass_Select()
    def Upd(self):
        level = gLevel()
        if level >= 1:
            ensure_ability("Fighting Style")
            fill_select("Fighting Style", 1)
            ensure_ability("Second Wind")
            use_list = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1][level]
            fill_uses("Second Wind", use_list)
        else:
            remove_ability("Fighting Style")
            remove_ability("Second Wind")
        if level >= 2:
            ensure_ability("Action Surge")
            use_list = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2][level]
            fill_uses("Action Surge", use_list)
        else:
            remove_ability("Action Surge")
        if level >= 5:
            ensure_ability("Extra Attack")
        else:
            remove_ability("Extra Attack")
        if level >= 9:
            ensure_ability("Indomitable")
            use_list = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2][level]
            fill_uses("Indomitable", use_list)
        else:
            remove_ability("Indomitable")
        ensure_subclass_Upd()

class Fighter_Champion():
    def __init__(self):
        pass
    def Select(self):
        pass
    def Upd(self):
        level = gLevel()
        if level >= 3:
            ensure_ability("Improved Critical")
        else:
            remove_ability("Improved Critical")
        if level >= 7:
            ensure_ability("Remarkable Athlete")
        else:
            remove_ability("Remarkable Athlete")
        if level >= 10:
            ensure_ability("Fighting Style")
            fill_select("Fighting Style", 2)
        if level >= 15:
            remove_ability("Improved Critical")
            ensure_ability("Superior Critical")
        else:
            remove_ability("Superior Critical")
        if level >= 18:
            ensure_ability("Survivor")
        else:
            remove_ability("Survivor")

class Fighter_BattleMaster():
    def __init__(self):
        pass
    def Select(self):
        if gLevel() >= 3:
            ensure_ability("Student of War")
            fill_select("Student of War", 1)
            selected_tool = gClass_abil()["Student of War"].get("Select", [""])[0]
            if selected_tool and selected_tool not in gProf()["Class"]["Tool"]:
                gProf()["Class"]["Tool"].append(selected_tool)
        else:
            remove_ability("Student of War")
    def Upd(self):
        level = gLevel()
        if level >= 3:
            ensure_ability("Combat Superiority")
            uses_num=[0,0,0,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,6][level]
            select_num=[0,0,0,3,3,3,3,5,5,5,7,7,7,7,7,9,9,9,9,9,9][level]
            fill_uses("Combat Superiority", uses_num)
            fill_select("Combat Superiority", select_num)
            
            ensure_ability("Relentless")
        else:
            remove_ability("Combat Superiority")
            remove_ability("Relentless")

class Fighter_EldrichKnight():
    def __init__(self):
        pass
    def Select(self):
        pass
    def Upd(self):
        level = gLevel()
        if level >= 3:
            ensure_ability("Weapon Bond")
        else:
            remove_ability("Weapon Bond")
        if level >= 7:
            ensure_ability("War Magic")
        else:
            remove_ability("War Magic")
        if level >= 10:
            ensure_ability("Eldrich Strike")
        else:
            remove_ability("Eldrich Strike")
        if level >= 15:
            ensure_ability("Arcane Charge")
        else:
            remove_ability("Arcane Charge")
        if level >= 18:
            remove_ability("War Magic")
            ensure_ability("Improved War Magic")
        else:
            remove_ability("Improved War Magic")
    def Spell_config(self):
        cspell=gSpell_data()
        cspell["Caster"] = "Wizard"
        cspell["max_spell_level"] = [0,0,0,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4][gLevel()]
        cspell["cantrips_available"] = [0,0,0,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3][gLevel()]
        cspell["spells_available"] = [0,0,0,3,4,4,4,5,6,6,7,8,8,9,10,10,11,11,11,12,13][gLevel()]
        cspell["abil"] = "INT"
        cspell["slots"] = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,2,0,0,0],[0,3,0,0,0],[0,3,0,0,0],[0,3,0,0,0],[0,4,2,0,0],[0,4,2,0,0],[0,4,2,0,0],[0,4,3,0,0],[0,4,3,0,0],[0,4,3,0,0],[0,4,3,2,0],[0,4,3,2,0],[0,4,3,2,0],[0,4,3,3,0],[0,4,3,3,0],[0,4,3,3,0],[0,4,3,3,1],[0,4,3,3,1]][gLevel()]
        cspell["mod"] = gAtr()["INT"]["Mod"]
        cspell["atk"] = f"{'+' if (gPB() + cspell['mod']) >= 0 else ''}{gPB() + cspell['mod']}"

        cspell["dc"] = 8 + gPB() + cspell["mod"]
        cspell["prepared_available"] = cspell["mod"] + gLevel()
        
        past = gSpell()["Slot"]
        for index,val in enumerate(cspell["slots"]):
            gSpell().Slot[index] = (past[index] + [False] * val)[:val]

class Wizard():
    def __init__(self):
        ensure_subclass_made()
    def Select(self):
        Wipe_Class()
        shared.db.HD.Die=6
        gProf()["Class"]["Weapon"].extend(["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"])
        gSkill()["Class"].extend([s for s in gClass_Skill() if s in dl[f"{gClass()} Skills"]])
        ensure_subclass_Select()
    def Spell_config(self):
        cspell=gSpell_data()
        cspell["Caster"] = "Wizard"
        cspell["max_spell_level"] = [0,1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,9][gLevel()]
        cspell["cantrips_available"] = [0,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5][gLevel()]
        cspell["spells_available"]= gLevel() * 2
        cspell["slots"]=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 2, 0, 0, 0, 0, 0, 0, 0, 0],[0, 3, 0, 0, 0, 0, 0, 0, 0, 0],[0, 4, 2, 0, 0, 0, 0, 0, 0, 0],[0, 4, 3, 0, 0, 0, 0, 0, 0, 0],[0, 4, 3, 2, 0, 0, 0, 0, 0, 0],[0, 4, 3, 3, 0, 0, 0, 0, 0, 0],[0, 4, 3, 3, 1, 0, 0, 0, 0, 0],[0, 4, 3, 3, 2, 0, 0, 0, 0, 0],[0, 4, 3, 3, 3, 1, 0, 0, 0, 0],[0, 4, 3, 3, 3, 2, 0, 0, 0, 0],[0, 4, 3, 3, 3, 2, 1, 0, 0, 0],[0, 4, 3, 3, 3, 2, 1, 0, 0, 0],[0, 4, 3, 3, 3, 2, 1, 1, 0, 0],[0, 4, 3, 3, 3, 2, 1, 1, 0, 0],[0, 4, 3, 3, 3, 2, 1, 1, 1, 0],[0, 4, 3, 3, 3, 2, 1, 1, 1, 0],[0, 4, 3, 3, 3, 2, 1, 1, 1, 1],[0, 4, 3, 3, 3, 3, 1, 1, 1, 1],[0, 4, 3, 3, 3, 3, 2, 1, 1, 1],[0, 4, 3, 3, 3, 3, 2, 2, 1, 1]][gLevel()]
        cspell["abil"] = "INT"
        cspell["mod"] = gAtr()["INT"]["Mod"]
        cspell["atk"] = f"{'+' if (gPB() + cspell['mod']) >= 0 else ''}{gPB() + cspell['mod']}"

        cspell["dc"] = 8 + gPB() + cspell["mod"]
        cspell["prepared_available"] = cspell["mod"] + gLevel()
        
        past = gSpell()["Slot"]
        for index,val in enumerate(cspell["slots"]): gSpell().Slot[index] = (past[index] + [False] * val)[:val]
    def Upd(self):
        level = gLevel()
        if level >=1:
            ensure_ability("Spellcasting")
            ensure_ability("Arcane Recovery")
            fill_uses("Arcane Recovery", 1)
        else:
            remove_ability("Spellcasting")
            remove_ability("Arcane Recovery")
        if level >=18:
            ensure_ability("Spell Mastery")
            fill_uses("Spell Mastery", 2)
            fill_select("Spell Mastery", 2)
        else:
            remove_ability("Spell Mastery")
        if level >=20:
            ensure_ability("Signature Spells")
            fill_uses("Signature Spells", 2)
            fill_select("Signature Spells", 2)
        else:
            remove_ability("Signature Spells")
        ensure_subclass_Upd()

class Wizard_Abjuration():
    def __init__(self):
        pass
    def Select(self):
        pass
    def Upd(self):
        level = gLevel()
        if level >= 2:
            ensure_ability("Abjuration Savant")
            
            ab_ward = ensure_ability("Arcane Ward")
            ward_max_hp = level + gAtr()["INT"]["Mod"]
            ward_current_hp = ab_ward.get("HP", {}).get("Current", ward_max_hp)
            ab_ward["HP"] = {"Max": ward_max_hp, "Current": ward_current_hp}
            fill_uses("Arcane Ward", 1)
        else:
            remove_ability("Abjuration Savant")
            remove_ability("Arcane Ward")
        if level >= 6:
            ensure_ability("Projected Ward")
        else:
            remove_ability("Projected Ward")
        if level >= 10:
            ensure_ability("Improved Abjuration")
        else:
            remove_ability("Improved Abjuration")
        if level >= 14:
            ensure_ability("Spell Resistance")
        else:
            remove_ability("Spell Resistance")

class Wizard_Conjuration():
    def __init__(self):
        pass
    def Select(self):
        pass
    def Upd(self):
        level = gLevel()
        if level >= 2:
            ensure_ability("Conjuration Savant")
            
            ensure_ability("Minor Conjuration")
        else:
            remove_ability("Conjuration Savant")
            remove_ability("Minor Conjuration")
        if level >= 6:
            ensure_ability("Benign Transportation")
            fill_uses("Benign Transportation", 1)
            
        else:
            remove_ability("Benign Transportation")
        if level >= 10:
            ensure_ability("Focused Conjuration")
        else:
            remove_ability("Focused Conjuration")
            
        if level >= 14:
            ensure_ability("Durable Summons")
            
        else:
            remove_ability("Durable Summons")

class_registry["Fighter"] = Fighter
class_registry["Wizard"] = Wizard
subclass_registry["Fighter_Champion"] = Fighter_Champion
subclass_registry["Fighter_BattleMaster"] = Fighter_BattleMaster
subclass_registry["Fighter_EldrichKnight"] = Fighter_EldrichKnight
subclass_registry["Wizard_Abjuration"] = Wizard_Abjuration
subclass_registry["Wizard_Conjuration"] = Wizard_Conjuration