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

def fill_uses(name, num_uses):
    past = gRace_abil().get(name, {}).get("Use", [False])
    gRace_abil()[name] = {"Use": (past + [False] * num_uses)[:num_uses]}

def Wipe_Race():
    gProf()["Race"] = {"Armor": [],"Weapon": [],"Tool": [],"Lang": []}
    gSkill()["Race"] = []
    for speed in Speed_L: gSpeed()[speed]["Race"]=0
    for vision in Vision_L: gVision()[vision]["Race"]=0
    gInitiative()["Race"]=0
    gHP()["Race"]=0
    gSavingThrow()["Race"]=[]

class Human():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        gSpeed()["Walk"]["Race"] = 30
        gProf()["Race"]["Lang"].append("Common")
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
        gVision()["Dark"]["Race"] = 60
        gSpeed()["Walk"]["Race"] = 30
        gSkill()["Race"].append("Perception")
        gProf()["Race"]["Lang"].extend(["Common", "Elvish"])
        subrace_Select()

    def Upd(self):
        subrace_Update()

class Elf_High():
    def __init__(self):
        self.Select()
    def Select(self):
        gProf()["Race"]["Weapon"].extend(["Shortbow", "Longsword", "Shortsword", "Longbow"])
    def Upd(self):
        select = gRace_abil().get("Cantrip",{}).get("Select","")
        gRace_abil()["Cantrip"] = {"Select": select}

class Elf_Wood():
    def __init__(self):
        self.Select()
    def Select(self):
        gSpeed()["Walk"]["Race"] = 35
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
        gRace_abil()["Drow Magic"]={}
        if level >= 1:
            gRace_abil()["Drow Magic"]["Dancing Lights"] = {}
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
        gProf()["Race"]["Weapon"].extend(["Handaxe", "Light Hammer", "Battleaxe", "Warhammer"])
        gProf()["Race"]["Lang"].extend(["Common", "Dwarvish"])
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
        gProf()["Race"]["Armor"].extend(["Light", "Medium"])
    def Upd(self):
        pass

class Halfling():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        gSpeed()["Walk"]["Race"] = 25
        gSkill()["Race"].append("Stealth")
        gProf()["Race"]["Lang"].extend(["Common", "Halfling"])
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
        gVision()["Dark"]["Race"] = 60
        gSpeed()["Walk"]["Race"] = 25
        gProf()["Race"]["Lang"].extend(["Common", "Gnomish"])
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
        gProf()["Race"]["Tool"].append("Tinker")
    def Upd(self):
        pass

class Dragonborn():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        gSpeed()["Walk"]["Race"] = 30
        gProf()["Race"]["Lang"].extend(["Common", "Draconic"])
        subrace_Select()
    def Upd(self):
        subrace_Update()

class Dragonborn_Black():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class Dragonborn_Blue():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class Dragonborn_Brass():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class Dragonborn_Bronze():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class Dragonborn_Copper():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class Dragonborn_Gold():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class Dragonborn_Green():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class Dragonborn_Red():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class Dragonborn_Silver():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class Dragonborn_White():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        fill_uses("Breath Weapon", 1)

class HalfOrc():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        gVision()["Dark"]["Race"] = 60
        gSpeed()["Walk"]["Race"] = 30
        gSkill()["Race"].append("Intimidation")
        gProf()["Race"]["Lang"].extend(["Common", "Orc"])
        subrace_Select()
    def Upd(self):
        subrace_Update()

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
        gVision()["Dark"]["Race"] = 60
        gSpeed()["Walk"]["Race"] = 30
        gProf()["Race"]["Lang"].extend(["Common", "Infernal"])
        subrace_Select()
    def Upd(self):
        subrace_Update()

class Tiefling_Asmodeus():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        gRace_abil()["Infernal Legacy"] = {}
        level = shared.db.Core.L
        if level >= 1:
            gRace_abil()["Infernal Legacy"]["Thaumaturgy"] = {}
        if level >= 3:
            gRace_abil()["Infernal Legacy"]["Hellish Rebuke"] = {"Use": gRace_abil().get("Infernal Legacy", {}).get("Hellish Rebuke", {}).get("Use", False)}
        if level >= 5:
            gRace_abil()["Infernal Legacy"]["Darkness"] = {"Use": gRace_abil().get("Infernal Legacy", {}).get("Darkness", {}).get("Use", False)}

class Tiefling_Baalzebul():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        gRace_abil()["Legacy of Maladomini"] = {}
        level = shared.db.Core.L
        if level >= 1:
            gRace_abil()["Legacy of Maladomini"]["Thaumaturgy"] = {}
        if level >= 3:
            gRace_abil()["Legacy of Maladomini"]["Ray of Sickness"] = {"Use": gRace_abil().get("Legacy of Maladomini", {}).get("Ray of Sickness", {}).get("Use", False)}
        if level >= 5:
            gRace_abil()["Legacy of Maladomini"]["Crown of Madness"] = {"Use": gRace_abil().get("Legacy of Maladomini", {}).get("Crown of Madness", {}).get("Use", False)}

class Tiefling_Dispater():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        gRace_abil()["Legacy of Dis"] = {}
        level = shared.db.Core.L
        if level >= 1:
            gRace_abil()["Legacy of Dis"]["Thaumaturgy"] = {}
        if level >= 3:
            gRace_abil()["Legacy of Dis"]["Disguise Self"] = {"Use": gRace_abil().get("Legacy of Dis", {}).get("Disguise Self", {}).get("Use", False)}
        if level >= 5:
            gRace_abil()["Legacy of Dis"]["Detect Thoughts"] = {"Use": gRace_abil().get("Legacy of Dis", {}).get("Detect Thoughts", {}).get("Use", False)}

class Tiefling_Fierna():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        gRace_abil()["Legacy of Minauros"] = {}
        level = shared.db.Core.L
        if level >= 1:
            gRace_abil()["Legacy of Minauros"]["Mage Hand"] = {}
        if level >= 3:
            gRace_abil()["Legacy of Minauros"]["Tensers Floating Disk"] = {"Use": gRace_abil().get("Legacy of Minauros", {}).get("Tensers Floating Disk", {}).get("Use", False)}
        if level >= 5:
            gRace_abil()["Legacy of Minauros"]["Arcane Lock"] = {"Use": gRace_abil().get("Legacy of Minauros", {}).get("Arcane Lock", {}).get("Use", False)}

class Tiefling_Glasya():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        gRace_abil()["Legacy of Cania"] = {}
        level = shared.db.Core.L
        if level >= 1:
            gRace_abil()["Legacy of Cania"]["Mage Hand"] = {}
        if level >= 3:
            gRace_abil()["Legacy of Cania"]["Burning Hands"] = {"Use": gRace_abil().get("Legacy of Cania", {}).get("Burning Hands", {}).get("Use", False)}
        if level >= 5:
            gRace_abil()["Legacy of Cania"]["Flame Blade"] = {"Use": gRace_abil().get("Legacy of Cania", {}).get("Flame Blade", {}).get("Use", False)}

class Tiefling_Levistus():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        gRace_abil()["Legacy of Stygia"] = {}
        level = shared.db.Core.L
        if level >= 1:
            gRace_abil()["Legacy of Stygia"]["Ray of Frost"] = {}
        if level >= 3:
            gRace_abil()["Legacy of Stygia"]["Armor of Agathys"] = {"Use": gRace_abil().get("Legacy of Stygia", {}).get("Armor of Agathys", {}).get("Use", False)}
        if level >= 5:
            gRace_abil()["Legacy of Stygia"]["Darkness"] = {"Use": gRace_abil().get("Legacy of Stygia", {}).get("Darkness", {}).get("Use", False)}

class Tiefling_Mammon():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        gRace_abil()["Legacy of Minauros"] = {}
        level = shared.db.Core.L
        if level >= 1:
            gRace_abil()["Legacy of Minauros"]["Mage Hand"] = {}
        if level >= 3:
            gRace_abil()["Legacy of Minauros"]["Tensers Floating Disk"] = {"Use": gRace_abil().get("Legacy of Minauros", {}).get("Tensers Floating Disk", {}).get("Use", False)}
        if level >= 5:
            gRace_abil()["Legacy of Minauros"]["Arcane Lock"] = {"Use": gRace_abil().get("Legacy of Minauros", {}).get("Arcane Lock", {}).get("Use", False)}

class Tiefling_Mephistopheles():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        gRace_abil()["Legacy of Cania"] = {}
        level = shared.db.Core.L
        if level >= 1:
            gRace_abil()["Legacy of Cania"]["Mage Hand"] = {}
        if level >= 3:
            gRace_abil()["Legacy of Cania"]["Burning Hands"] = {"Use": gRace_abil().get("Legacy of Cania", {}).get("Burning Hands", {}).get("Use", False)}
        if level >= 5:
            gRace_abil()["Legacy of Cania"]["Flame Blade"] = {"Use": gRace_abil().get("Legacy of Cania", {}).get("Flame Blade", {}).get("Use", False)}

class Tiefling_Zariel():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        gRace_abil()["Legacy of Avernus"] = {}
        level = shared.db.Core.L
        if level >= 1:
            gRace_abil()["Legacy of Avernus"]["Thaumaturgy"] = {}
        if level >= 3:
            gRace_abil()["Legacy of Avernus"]["Searing Smite"] = {"Use": gRace_abil().get("Legacy of Avernus", {}).get("Searing Smite", {}).get("Use", False)}
        if level >= 5:
            gRace_abil()["Legacy of Avernus"]["Branding Smite"] = {"Use": gRace_abil().get("Legacy of Avernus", {}).get("Branding Smite", {}).get("Use", False)}

class Harengon():
    def __init__(self):
        Wipe_Race()
        create_subrace()

    def Select(self):
        gSpeed()["Walk"]["Race"] = 30
        gSkill()["Race"].append("Perception")
        gProf()["Race"]["Lang"].append("Common")
        gInitiative()["Race"] = gPB()
        subrace_Select()
    def Upd(self):
        fill_uses("Rabbit Hop", gPB())
        subrace_Update()

class Harengon_Standard():
    def __init__(self):
        self.Select()
    def Select(self):
        pass
    def Upd(self):
        pass

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