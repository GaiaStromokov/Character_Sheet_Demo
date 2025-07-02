import shared
from Sheet.get_set import *
from dictionary_data.import_central import *
from .registry import background_registry



    


def extend_prof(cat, items):
    index = "Tool" if cat in ["Game", "Music", "Job"] else cat
    gProf()["Background"][index].extend(items)

def fill_prof_select(name, num):
    
    past = gBackground_data()["Prof"].get(name, {}).get("Select", [])
    gBackground_data()["Prof"].setdefault(name, {})["Select"] = (past + [""] * num)[:num]
    
    items = []
    for idx,val in enumerate(gBackground_data()["Prof"][name]["Select"]):
        if val:
            items.extend([val])
    extend_prof(name, items)
        
        
    
def extend_skill(items):
    gSkill()["Background"].extend(items)

def clear_background():
    for i in Prof_L: gProf()["Background"][i] = []
    gSkill()["Background"] = []
    
class Acolyte():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Insight", "Religion"])
        fill_prof_select("Lang", 2)
        

        
class Charlatan():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Deception", "Sleight of Hand"])
        extend_prof("Tool", ["Disguise", "Forgery"])

class Criminal():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Deception", "Stealth"])
        extend_prof("Job", ["Thief"])
        fill_prof_select("Game", 1)

class Entertainer():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Acrobatics", "Performance"])
        extend_prof("Job", ["Disguise"])
        fill_prof_select("Music", 1)

class FolkHero():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Animal Handling", "Survival"])
        fill_prof_select("Job", 1)

class GuildArtisan():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Insight", "Persuasion"])
        extend_prof("Job", ["Tinker"])
        fill_prof_select("Job", 1)
        fill_prof_select("Lang", 1)

class Hermit():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Medicine", "Religion"])
        extend_prof("Job", ["Herbalism Kit"])
        fill_prof_select("Lang", 1)

class Noble():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["History", "Persuasion"])
        fill_prof_select("Lang", 1)
        fill_prof_select("Game", 1)

class Outlander():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Athletics", "Survival"])
        fill_prof_select("Music", 1)
        fill_prof_select("Lang", 1)

class Sage():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Arcana", "History"])
        fill_prof_select("Lang", 2)

class Sailor():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Athletics", "Perception"])
        extend_prof("Job", ["Navigator"])

class Soldier():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Athletics", "Intimidation"])
        fill_prof_select("Game", 1)

class Urchin():
    def __init__(self):
        pass
    def Create(self):
        clear_background()
        extend_skill(["Sleight of Hand", "Stealth"])
        extend_prof("Tool", ["Disguise", "Thief"])



background_registry["Acolyte"] = Acolyte
background_registry["Charlatan"] = Charlatan
background_registry["Criminal"] = Criminal
background_registry["Entertainer"] = Entertainer
background_registry["FolkHero"] = FolkHero
background_registry["GuildArtisan"] = GuildArtisan
background_registry["Hermit"] = Hermit
background_registry["Noble"] = Noble
background_registry["Outlander"] = Outlander
background_registry["Sage"] = Sage
background_registry["Sailor"] = Sailor
background_registry["Soldier"] = Soldier
background_registry["Urchin"] = Urchin