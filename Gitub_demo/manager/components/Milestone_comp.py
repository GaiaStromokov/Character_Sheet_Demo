import shared
from Sheet.get_set import *
from access_data.book import *
from .registry import feat_registry

dict_Feat_Count = {
    'Empty': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Fighter': [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7],
    'Rogue': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6],
    'Wizard': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Ranger': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Paladin': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]
}
race_bonus_Feat_L = ["Variant"]


def fill_select(name, num):
    past = gMilestone()["Data"].get(name, {}).get("Select", [])
    gMilestone()["Data"][name]["Select"] = (past + [""] * num)[:num]

def fill_uses(name, num):
    past =  gMilestone()["Data"].get(name, {}).get("Use", [])
    gMilestone()["Data"][name]["Use"] = (past + [False] * num)[:num]
    


def set_static_atr(atr):
    gAtr()[atr]["Milestone"] += 1


def set_static_speed(speed, val):
    gSpeed()[speed]["Feat"] += val

def set_dynamic_hp(val):
    gHP()["Feat"] += val

def extend_prof(cat,items):
    gProf()["Feat"][cat].extend(items)
    

def set_atr_select(name):
    select = gMilestone()["Data"][name]["Select"][0]
    if select and name in list(dl.keys()): 
        gAtr()[select]["Milestone"] += 1
    
class Milestone_config():
    def __init__(self):
        pass
    def on_init(self):
        self.Upd()
    
    def Upd(self):

        self.Count()
        self.Clear()
        self.Create()
        self.Collate()
        
        
        
        
    def Count(self):
        num = dict_Feat_Count[gClass()][gLevel()]  
        if gSubrace() in race_bonus_Feat_L: num += 1
        shared.pc.milestone_count = num
    
    def Clear(self):
        count = shared.pc.milestone_count
        
        cdata = gMilestone()
        for i in range(count, len(cdata["Select"])):
            cdata["Select"][i] = ""
            cdata["Feat"][i] = ""
            cdata["Asi"][i] = ["", ""]
            
        current_feats = set(cdata["Feat"])
        for attr in list(vars(shared.pc)):
            if attr.startswith("Feat_"):
                feat = attr[5:]
                if feat not in current_feats:
                    delattr(shared.pc, attr)
        
        for key in list(cdata["Data"].keys()):
            if key not in cdata["Feat"]:
                cdata["Data"].pop(key)
        
        for atr in Atr_L: gAtr()[atr]["Milestone"]=0
        for i in Prof_L: gProf()["Feat"][i] = []
        gSkill()["Feat"] = []
        for speed in Speed_L: gSpeed()[speed]["Feat"] = 0
        for vision in Vision_L: gVision()[vision]["Feat"] = 0
        gInitiative()["Feat"] = 0
        gHP()["Feat"] = 0



    
    def Create(self):
        for feat in gMilestone()["Feat"]:
            if feat:setattr(shared.pc, f"Feat_{feat}", globals()[feat]())
    
    def Collate(self):
        for each in gMilestone()["Asi"]:
            for index in each:
                if index in Atr_L:
                    gAtr()[index]["Milestone"]+=1
        

class Actor():
    def __init__(self):
        self.Create()
    def Create(self):
        set_static_atr("CHA")
        
class Alert():
    def __init__(self):
        self.Create()
    def Create(self):
        gInitiative()["Feat"] += 5

class Athlete():
    def __init__(self):
        self.Create()
    def Create(self):
        feat="Athlete"
        fill_select(feat, 1)
        set_atr_select(feat)

        

class Charger():
    def __init__(self):
        self.Create()
    def Create(self):
        pass
            

class CrossbowExpert():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class DefensiveDuelist():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class DualWielder():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class DungeonDelver():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class Durable():
    def __init__(self):
        self.Create()
    def Create(self):
        set_static_atr("CON")

class ElementalAdept():
    def __init__(self):
        self.Create()
    def Create(self):
        fill_select("ElementalAdept",1)

class Grappler():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class GreatWeaponMaster():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class Healer():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class HeavilyArmored():
    def __init__(self):
        self.Create()
    def Create(self):
        set_static_atr("STR")
        extend_prof("Armor",["Heavy"])

class HeavyArmorMaster():
    def __init__(self):
        self.Create()
    def Create(self):
        set_static_atr("STR")

class InspiringLeader():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class KeenMind():
    def __init__(self):
        self.Create()
    def Create(self):
        set_static_atr("INT")

class LightlyArmored():
    def __init__(self):
        self.Create()
    def Create(self):
        feat = "LightlyArmored"
        
        extend_prof("Armor",["Light"])
        fill_select(feat, 1)
        set_atr_select(feat)

class Lucky():
    def __init__(self):
        self.Create()
    def Create(self):
        feat="Lucky"
        fill_uses(feat, 3)

class MageSlayer():
    def __init__(self):
        self.Create()
    def Create(self):
        pass


class MediumArmorMaster():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class Mobile():
    def __init__(self):
        self.Create()
    def Create(self):
        set_static_speed("Walk", 10)
    




class ModeratelyArmored():
    def __init__(self):
        self.Create()
    def Create(self):
        feat = "MediumArmorMaster"
        extend_prof("Armor", ["Medium", "Shield"])
        fill_select(feat, 1)
        set_atr_select(feat)

class MountedCombatant():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class PolearmMaster():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class Resilient():
    def __init__(self):
        self.Create()
    def Create(self):
        feat = "Resilient"
        fill_select(feat, 1)
        #set saving throw stuff when i get around to it

class SavageAttacker():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class Sentinel():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class Sharpshooter():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class ShieldMaster():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class Skulker():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class TavernBrawler():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class Tough():
    def __init__(self):
        self.Create()
    def Create(self):
        set_dynamic_hp(gLevel() * 2)


class WarCaster():
    def __init__(self):
        self.Create()
    def Create(self):
        pass

class WeaponMaster():
    def __init__(self):
        self.Create()
    def Create(self):
        feat = "WeaponMaster"
        fill_select(feat, 4)
        collection = []
        for i in gMilestone["Data"][feat]["Select"]:
            if i:
                collection.extend([i])
                
        extend_prof(collection)


feat_registry["Actor"] = Actor
feat_registry["Alert"] = Alert
feat_registry["Athlete"] = Athlete
feat_registry["Charger"] = Charger
feat_registry["CrossbowExpert"] = CrossbowExpert
feat_registry["DefensiveDuelist"] = DefensiveDuelist
feat_registry["DualWielder"] = DualWielder
feat_registry["DungeonDelver"] = DungeonDelver
feat_registry["Durable"] = Durable
feat_registry["ElementalAdept"] = ElementalAdept
feat_registry["Grappler"] = Grappler
feat_registry["GreatWeaponMaster"] = GreatWeaponMaster
feat_registry["Healer"] = Healer
feat_registry["HeavilyArmored"] = HeavilyArmored
feat_registry["HeavyArmorMaster"] = HeavyArmorMaster
feat_registry["InspiringLeader"] = InspiringLeader
feat_registry["KeenMind"] = KeenMind
feat_registry["LightlyArmored"] = LightlyArmored
feat_registry["Lucky"] = Lucky
feat_registry["MageSlayer"] = MageSlayer
feat_registry["MediumArmorMaster"] = MediumArmorMaster
feat_registry["Mobile"] = Mobile
feat_registry["ModeratelyArmored"] = ModeratelyArmored
feat_registry["MountedCombatant"] = MountedCombatant
feat_registry["PolearmMaster"] = PolearmMaster
feat_registry["Resilient"] = Resilient
feat_registry["SavageAttacker"] = SavageAttacker
feat_registry["Sentinel"] = Sentinel
feat_registry["Sharpshooter"] = Sharpshooter
feat_registry["ShieldMaster"] = ShieldMaster
feat_registry["Skulker"] = Skulker
feat_registry["TavernBrawler"] = TavernBrawler
feat_registry["Tough"] = Tough
feat_registry["WarCaster"] = WarCaster
feat_registry["WeaponMaster"] = WeaponMaster