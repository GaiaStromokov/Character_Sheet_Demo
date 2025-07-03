import shared
from Sheet.get_set import *
from access_data.book import *
from .registry import race_registry, subrace_registry

def create_subrace():
    if gSubrace():
        subrace_func = subrace_registry.get(f"{gRace()}_{gSubrace()}")
        if subrace_func: shared.pc.Subrace = subrace_func()

def subrace_Select():
    if gSubrace(): shared.pc.Subrace.Select()
    
def subrace_Update():
    if gSubrace(): shared.pc.Subrace.Upd()

def fill_uses(name, num):
    past = gRace_abil().get(name, {}).get("Use", [False])
    gRace_abil()[name] = {"Use": (past + [False] * num)[:num]}

def fill_uses_extend(index, name, num):
    past = gRace_abil().get(index, {}).get(name, {}).get("Use", [False])
    gRace_abil()[index][name] = {"Use": (past + [False] * num)[:num]}
    
    
def fill_select(name, num):
    past = gRace_abil()["Data"].get(name, {}).get("Select", [])
    gRace_abil()[name]["Select"] = (past + [""] * num)[:num]

def ensure_ability(name):
    return gRace_abil().setdefault(name, {})

def ensure_ability_extend(index, name):
    return gRace_abil()[index].setdefault(name, {})


def extend_prof(cat, items):
    index = "Tool" if cat in ["Game", "Music", "Job"] else cat
    gProf()["Race"][index].extend(items)

def extend_skill(items):
    gSkill()["Race"].extend(items)

def set_static_speed(speed, val):
    gSpeed()[speed]["Race"] = val

def set_static_vision(vision, val):
    gVision()[vision]["Race"] = val

def set_static_initiative(val):
    gInitiative["Race"] = val
    
def Wipe_Race():
    gProf()["Race"] = {"Armor": [],"Weapon": [],"Tool": [],"Lang": []}
    gSkill()["Race"] = []
    for speed in Speed_L: gSpeed()[speed]["Race"]=0
    for vision in Vision_L: gVision()[vision]["Race"]=0
    gInitiative()["Race"]=0
    gHP()["Race"]=0
    gSavingThrow()["Race"]=[]


class Empty():
    def __init__(self):
        Wipe_Race()
        

    def Select(self):
        pass

    def Upd(self):
        pass
        
class Human():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        set_static_speed("Walk", 30)
        extend_prof("Lang", ["Common"])
        subrace_Select()

    def Upd(self):
        subrace_Update()

class Human_Standard():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        pass

class Human_Variant():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        pass

class Elf():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        set_static_vision("Dark", 60)
        set_static_speed("Walk", 30)
        extend_skill(["Perception"])
        extend_prof("Lang", ["Common", "Elvish"])
        subrace_Select()

    def Upd(self):
        subrace_Update()

class Elf_High():
    def __init__(self):
        self.Select()
    def Select(self):
        extend_prof("Weapon", ["Longsword", "Shortsword", "Shortbow", "Longbow"])
    def Upd(self):
        ensure_ability("Cantrip")
        fill_select("Cantrip", 1)

class Elf_Wood():
    def __init__(self):
        self.Select()
    def Select(self):
        set_static_speed("Walk", 35)
        gProf()["Race"]["Weapon"].extend(["Shortbow", "Longsword", "Shortsword", "Longbow"])
    def Upd(self):
        pass
class Elf_Drow():
    def __init__(self):
        self.Select()
    def Select(self):
        gVision()["Dark"]["Race"] = 120
        gProf()["Race"]["Weapon"].extend(["Rapier", "Shortsword", "Hand Crossbow"])
    def Upd(self):
        level = gLevel()
        ensure_ability("Drow Magic")
        if level >= 1:
            ensure_ability_extend("Drow Magic", "Dancing Lights")
        if level >= 3:
            gRace_abil()["Drow Magic"]["Faerie Fire"] = {"Use": gRace_abil().get("Drow Magic", {}).get("Faerie Fire", {}).get("Use", False)}

class Elf_ShadarKai():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Blessing of the Raven Queen", gPB())

class Dwarf():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        gVision()["Dark"]["Race"] = 60
        gSpeed()["Walk"]["Race"] = 30
        extend_prof("Weapon", ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"])
        extend_prof("Lang", ["Common", "Dwarvish"])
        subrace_Select()
    def Upd(self):
        subrace_Update()

class Dwarf_Hill():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        hp_bonus = gLevel()
        gHP()["Race"] = hp_bonus

class Dwarf_Mountain():
    def __init__(self):
        self.Select()
    def Select(self):
        extend_prof("Armor", ["Light", "Medium"])
    def Upd(self):
        pass

class Halfling():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        set_static_speed("Walk", 25)
        extend_skill(["Stealth"])
        extend_prof("Lang", ["Common", "Halfling"])
        
        subrace_Select()
    def Upd(self):
        subrace_Update()

class Halfling_Lightfoot():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        pass

class Halfling_Stout():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        pass

class Gnome():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        set_static_speed("Walk", 25)
        set_static_vision("Dark", 60)
        extend_prof("Lang", ["Common", "Gnomish"])
        
        subrace_Select()
    def Upd(self):
        subrace_Update()

class Gnome_Forest():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        pass

class Gnome_Rock():
    def __init__(self):
        self.Select()
    def Select(self):
        extend_prof("Tool", ["Tinker"])
    def Upd(self):
        pass

class Dragonborn():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        set_static_speed("Walk", 30)
        extend_prof("Lang", ["Common", "Draconic"])
        
        subrace_Select()
    def Upd(self):
        subrace_Update()

class Dragonborn_Black():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class Dragonborn_Blue():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class Dragonborn_Brass():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class Dragonborn_Bronze():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class Dragonborn_Copper():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class Dragonborn_Gold():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class Dragonborn_Green():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class Dragonborn_Red():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class Dragonborn_Silver():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class Dragonborn_White():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Breath Weapon")
        fill_uses("Breath Weapon", 1)

class HalfOrc():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        set_static_vision("Dark", 60)
        set_static_speed("Walk", 30)
        extend_skill(["Intimidation"])
        extend_prof("Lang", ["Common", "Orc"])
        subrace_Select()
    def Upd(self):
        ensure_ability("Relentless Endurance")
        fill_uses("Relentless Endurance", 1)
        
        ensure_ability("Savage Attacks")


class HalfOrc_Standard():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        pass

class Tiefling():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        set_static_vision("Dark", 60)
        set_static_speed("Walk", 30)
        extend_prof("Lang", ["Common", "Infernal"])
        
        subrace_Select()
    def Upd(self):
        subrace_Update()

class Tiefling_Asmodeus():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Infernal Legacy")
        level = gLevel()
        if level >= 1:
            ensure_ability_extend("Infernal Legacy", "Thaumaturgy")
        if level >= 3:
            ensure_ability_extend("Infernal Legacy", "Hellish Rebuke")
            fill_uses_extend("Infernal Legacy", "Hellish Rebuke", 1)
        if level >= 5:
            ensure_ability_extend("Infernal Legacy", "Darkness")
            fill_uses_extend("Infernal Legacy", "Darkness", 1)

class Tiefling_Baalzebul():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Legacy of Maladomini")
        level = gLevel()
        if level >= 1:
            ensure_ability_extend("Legacy of Maladomini", "Thaumaturgy")
        if level >= 3:
            ensure_ability_extend("Legacy of Maladomini", "Ray of Sickness")
            fill_uses_extend("Legacy of Maladomini", "Ray of Sickness", 1)
        if level >= 5:
            ensure_ability_extend("Legacy of Maladomini", "Crown of Madness")
            fill_uses_extend("Legacy of Maladomini", "Crown of Madness", 1)

class Tiefling_Dispater():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Legacy of Dis")
        level = gLevel()
        if level >= 1:
            ensure_ability_extend("Legacy of Dis", "Thaumaturgy")
        if level >= 3:
            ensure_ability_extend("Legacy of Dis", "Disguise Self")
            fill_uses_extend("Legacy of Dis", "Disguise Self", 1)
        if level >= 5:
            ensure_ability_extend("Legacy of Dis", "Detect Thoughts")
            fill_uses_extend("Legacy of Dis", "Detect Thoughts", 1)

class Tiefling_Fierna():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Legacy of Minauros")
        level = gLevel()
        if level >= 1:
            ensure_ability_extend("Legacy of Minauros", "Mage Hand")
        if level >= 3:
            ensure_ability_extend("Legacy of Minauros", "Tensers Floating Disk")
            fill_uses_extend("Legacy of Minauros", "Tensers Floating Disk", 1)
        if level >= 5:
            ensure_ability_extend("Legacy of Minauros", "Arcane Lock")
            fill_uses_extend("Legacy of Minauros", "Arcane Lock", 1)

class Tiefling_Glasya():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Legacy of Cania")
        level = gLevel()
        if level >= 1:
            ensure_ability_extend("Legacy of Cania", "Mage Hand")
        if level >= 3:
            ensure_ability_extend("Legacy of Cania", "Burning Hands")
            fill_uses_extend("Legacy of Cania", "Burning Hands", 1)
        if level >= 5:
            ensure_ability_extend("Legacy of Cania", "Flame Blade")
            fill_uses_extend("Legacy of Cania", "Flame Blade", 1)

class Tiefling_Levistus():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Legacy of Stygia")
        level = gLevel()
        if level >= 1:
            ensure_ability_extend("Legacy of Stygia", "Ray of Frost")
        if level >= 3:
            ensure_ability_extend("Legacy of Stygia", "Armor of Agathys")
            fill_uses_extend("Legacy of Stygia", "Armor of Agathys", 1)
        if level >= 5:
            ensure_ability_extend("Legacy of Stygia", "Darkness")
            fill_uses_extend("Legacy of Stygia", "Darkness", 1)

class Tiefling_Mammon():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Legacy of Minauros")
        level = gLevel()
        if level >= 1:
            ensure_ability_extend("Legacy of Minauros", "Mage Hand")
        if level >= 3:
            ensure_ability_extend("Legacy of Minauros", "Tensers Floating Disk")
            fill_uses_extend("Legacy of Minauros", "Tensers Floating Disk", 1)
        if level >= 5:
            ensure_ability_extend("Legacy of Minauros", "Arcane Lock")
            fill_uses_extend("Legacy of Minauros", "Arcane Lock", 1)

class Tiefling_Mephistopheles():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Legacy of Cania")
        level = gLevel()
        if level >= 1:
            ensure_ability_extend("Legacy of Cania", "Mage Hand")
        if level >= 3:
            ensure_ability_extend("Legacy of Cania", "Burning Hands")
            fill_uses_extend("Legacy of Cania", "Burning Hands", 1)
        if level >= 5:
            ensure_ability_extend("Legacy of Cania", "Flame Blade")
            fill_uses_extend("Legacy of Cania", "Flame Blade", 1)

class Tiefling_Zariel():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        ensure_ability("Legacy of Avernus")
        level = gLevel()
        if level >= 1:
            ensure_ability_extend("Legacy of Avernus", "Thaumaturgy")
        if level >= 3:
            ensure_ability_extend("Legacy of Avernus", "Searing Smite")
            fill_uses_extend("Legacy of Avernus", "Searing Smite", 1)
        if level >= 5:
            ensure_ability_extend("Legacy of Avernus", "Branding Smite")
            fill_uses_extend("Legacy of Avernus", "Branding Smite", 1)
            
            
class Harengon():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        gSpeed()["Walk"]["Race"] = 30
        gSkill()["Race"].append("Perception")
        gProf()["Race"]["Lang"].append("Common")
        gInitiative()["Race"] = gPB()
        
        set_static_speed("Walk", 30)
        extend_skill(["Perception"])
        extend_prof("Lang", ["Common", "Elvish"])
        set_static_initiative(gPB())
        subrace_Select()
    def Upd(self):
        ensure_ability("Rabbit Hop")
        fill_uses("Rabbit Hop", gPB())
        subrace_Update()

class Harengon_Standard():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        pass

race_registry["Empty"] = Empty
race_registry["Human"] = Human
race_registry["Elf"] = Elf
race_registry["Dwarf"] = Dwarf
race_registry["Halfling"] = Halfling
race_registry["Gnome"] = Gnome
race_registry["Dragonborn"] = Dragonborn
race_registry["HalfOrc"] = HalfOrc
race_registry["Tiefling"] = Tiefling
race_registry["Harengon"] = Harengon

subrace_registry["Human_Standard"] = Human_Standard
subrace_registry["Human_Variant"] = Human_Variant
subrace_registry["Elf_High"] = Elf_High
subrace_registry["Elf_Wood"] = Elf_Wood
subrace_registry["Elf_Drow"] = Elf_Drow
subrace_registry["Elf_ShadarKai"] = Elf_ShadarKai
subrace_registry["Dwarf_Hill"] = Dwarf_Hill
subrace_registry["Dwarf_Mountain"] = Dwarf_Mountain
subrace_registry["Halfling_Lightfoot"] = Halfling_Lightfoot
subrace_registry["Halfling_Stout"] = Halfling_Stout
subrace_registry["Gnome_Forest"] = Gnome_Forest
subrace_registry["Gnome_Rock"] = Gnome_Rock
subrace_registry["Dragonborn_Black"] = Dragonborn_Black
subrace_registry["Dragonborn_Blue"] = Dragonborn_Blue
subrace_registry["Dragonborn_Brass"] = Dragonborn_Brass
subrace_registry["Dragonborn_Bronze"] = Dragonborn_Bronze
subrace_registry["Dragonborn_Copper"] = Dragonborn_Copper
subrace_registry["Dragonborn_Gold"] = Dragonborn_Gold
subrace_registry["Dragonborn_Green"] = Dragonborn_Green
subrace_registry["Dragonborn_Red"] = Dragonborn_Red
subrace_registry["Dragonborn_Silver"] = Dragonborn_Silver
subrace_registry["Dragonborn_White"] = Dragonborn_White
subrace_registry["HalfOrc_Standard"] = HalfOrc_Standard
subrace_registry["Tiefling_Asmodeus"] = Tiefling_Asmodeus
subrace_registry["Tiefling_Baalzebul"] = Tiefling_Baalzebul
subrace_registry["Tiefling_Dispater"] = Tiefling_Dispater
subrace_registry["Tiefling_Fierna"] = Tiefling_Fierna
subrace_registry["Tiefling_Glasya"] = Tiefling_Glasya
subrace_registry["Tiefling_Levistus"] = Tiefling_Levistus
subrace_registry["Tiefling_Mammon"] = Tiefling_Mammon
subrace_registry["Tiefling_Mephistopheles"] = Tiefling_Mephistopheles
subrace_registry["Tiefling_Zariel"] = Tiefling_Zariel
subrace_registry["Harengon_Standard"] = Harengon_Standard