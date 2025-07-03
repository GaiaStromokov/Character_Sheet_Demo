#get_set.py
from access_data.book import *
from access_data.color_reference import *
import shared






#ANCHOR - DB Getters

def gCore(): return shared.db.Core

def gLevel(): return shared.db.Core.L
def gPB(): return shared.db.Core.PB
def gProf():return shared.db.Prof
def gSkill():return shared.db.Skill
def gSpeed():return shared.db.Speed
def gVision():return shared.db.Vision
def gInitiative():return shared.db.Initiative
def gHP():return shared.db.HP
def gSavingThrow():return shared.db.SavingThrow
def gCondition():return shared.db.Condition

def gAtr():return shared.db.Atr

def gSpell():return shared.db.Spell
def gSpell_data():return shared.pc.spell_data

def gRace(): return shared.db.Core.R
def gSubrace(): return shared.db.Core.SR
def gRace_data(): return shared.db.Race
def gRace_abil(): return shared.db.Race["Abil"]


def gClass(): return shared.db.Core.C
def gSubclass(): return shared.db.Core.SC
def gClass_data(): return shared.db.Class
def gClass_abil(): return shared.db.Class["Abil"]
def gClass_Skill(): return shared.db.Class["Skill Select"]

def gBackground(): return shared.db.Core.BG
def gBackground_data(): return shared.db.Background.Data

def get_valid_class(): return bool(shared.db.Valid.Class)

def gMilestone(): return shared.db.Milestone
def gMcount(): return shared.pc.milestone_count

def gCharacteristic(): return shared.db.Characteristic
def gDescription(): return shared.db.Description

def can_cast(): return gClass() in spellcast_L or gSubclass() in spellcast_L

def get_cantrip_known(): return len(gSpell().Book[0])

def get_spell_known():
    num = 0
    for i in [1,2,3,4,5,6,7,8,9]:
        num += len(gSpell().Book[i])
    return num

def get_spell_prepared():
    num = 0
    for i in [1,2,3,4,5,6,7,8,9]:
        num += len(gSpell().Prepared[i])
    return num


#---------------- 
#TODO - Condition
#----------------

def get_condition(item): return gCondition()[item]

def get_conditionc(item): return c_item_true if get_condition(item) else c_item_false



#----------------
#ANCHOR -Initiative
#----------------

def get_Initiative():
    mod = gInitiative()["Val"]
    return f"{'+' if mod >= 0 else '-'}{abs(mod)}"





#----------------
#ANCHOR - Proficiency
#----------------

def get_profc(cat,item): return c_item_true if item in gProf()[cat] else c_item_false



#----------------
#ANCHOR - Skill
#----------------

def get_Skill_Mod(skill):
    mod=gSkill()[skill]["Mod"]
    return f"{'+' if mod >= 0 else '-'}{abs(mod)}"


#----------------
#ANCHOR - get DC
#----------------
def get_DC(atr):
    return 8 + gAtr()[atr]["Mod"] + gPB()

#----------------
#ANCHOR - get Fighting Style Description
#----------------

def get_Fighting_Style(Style):
    item_map = {
        "Archery": "You gain a +2 bonus to attack rolls you make with ranged weapons.",
        "Defense": "While you are wearing armor, you gain a +1 bonus to AC.",
        "Dueling": "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
        "Great Weapon Fighting": "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll. The weapon must have the two-handed or versatile property for you to gain this benefit.",
        "Protection": "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.",
        "Two Weapon Fighting": "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.",
        "Blind Fighting": "You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover.",
        "Interception": f"When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + {shared.db.Core.PB}. You must be wielding a shield or a simple or martial weapon to use this reaction.",
        "Thrown Weapon Fighting": "You can draw a weapon that has the thrown property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.",
        "Unarmed Fighting": f"Your unarmed strikes can deal bludgeoning damage equal to 1d6 + {gAtr()["STR"]["Mod"]}. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you."
    }
    return item_map[Style]

def get_Maneuver(Maneuver):
    item_map = {
        "Ambush": "When you make a Stealth check or roll initiative, Use 1 SD and add too roll, Not available when incapacitated.",
        "Bait and Switch": "on turn, if withen 5 ft of a willing creature with more then 5t of movement, Use 1SD too switch places with the creature, this doesn't provoke OA, until the start of your next turn, you and the creature gains AC equal too roll.",
        "Brace": "When creature moves into melee reach, use reaction and 1 SD too make attack, add SD too damage.",
        "Commander's Strike": "Replace one attack with bonus action, ally you can see makes weapon attack and adds SD too damage.",
        "Commanding Presence": "Use 1 SD on Intimidation, Performance, or Persuasion checks, add too roll.",
        "Disarming Attack": "On hit, use 1 SD, add too damage, target makes STR save or drops item.",
        "Distracting Strike": "On hit, use 1 SD, add too damage, next ally attack has advantage.",
        "Evasive Footwork": "When moving, use 1 SD and add too AC until you stop.",
        "Feinting Attack": "Bonus action, use 1 SD too gain advantage on next attack, add SD too damage if hit.",
        "Goading Attack": "On hit, use 1 SD, add too damage, target makes WIS save or has disadvantage attacking others.",
        "Grappling Strike": "After melee hit, use 1 SD and bonus action too grapple, add SD too Athletics check.",
        "Lunging Attack": "Use 1 SD too increase melee reach by 5 ft, add too damage if hit.",
        "Maneuvering Attack": "On hit, use 1 SD, add too damage, ally moves half speed without provoking OA from target.",
        "Menacing Attack": "On hit, use 1 SD, add too damage, target makes WIS save or frightened until next turn.",
        "Parry": "When hit by melee attack, use reaction and 1 SD too reduce damage by roll + DEX mod.",
        "Precision Attack": "Use 1 SD too add too attack roll before or after rolling.",
        "Pushing Attack": "On hit, use 1 SD, add too damage, Large or smaller makes STR save or pushed 15 ft.",
        "Quick Toss": "Bonus action, use 1 SD too make thrown weapon attack, add too damage if hit.",
        "Rally": "Bonus action, use 1 SD, ally gains temp HP equal too roll + CHA mod.",
        "Riposte": "When enemy misses melee attack, use reaction and 1 SD too attack back, add too damage.",
        "Sweeping Attack": "On melee hit, use 1 SD, second creature within 5 ft takes SD damage if original roll hits.",
        "Tactical Assessment": "Use 1 SD on Investigation, History, or Insight checks, add too roll.",
        "Trip Attack": "On hit, use 1 SD, add too damage, Large or smaller makes STR save or knocked prone."
    }
    return item_map[Maneuver]






#----------------
#SECTION - SET 
#----------------


    
def set_Level(sender, data, user_data):
    gCore().L = int(data)
    gCore().PB = (int(data) - 1) // 4 + 2

def set_Race(sender, data, user_data):
    gCore().R = data

def set_Subrace(sender, data, user_data):
    gCore().SR = data

def set_Class(sender, data, user_data):
    gCore().C = data

def set_Subclass(sender, data, user_data):
    gCore().SC = data


def set_Background(sender, data, user_data):
    gCore().BG = data


def set_Rasi(sender, data, user_data):
    if user_data[0] == "Clear":
        gRace_data().Rasi=["",""]
    else:
        gRace_data().Rasi[user_data[0]]=data



    
def set_Race_Use(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    gRace_abil()[key]["Use"][index] = data


def set_Race_Spell_Use(sender, data, user_data):
    abil = user_data[0]
    spell = user_data[1]
    gRace_abil()[abil][spell]["Use"] = data

def set_Race_Spell_Select(sender, data, user_data):
    key=user_data[0]
    gRace_abil()[key]["Select"] = data


def set_Atr_Base(sender, data, user_data):
    gAtr()[user_data[0]].Base = int(data)





    
    # "Background": {
    #     "Data": {
    #         "Prof": {
    #             "Music": {
    #                 "Select": [
    #                     ""
    #                 ]
    #             }
    #         },

def set_Background_Prof_Select(sender, data, user_data):
    cat = user_data[0]
    index = user_data[1]
    
    if data != "Clear":
        gBackground_data()["Prof"][cat]["Select"][index] = data
    else:
        for key in gBackground_data()["Prof"]:
            plen = len(gBackground_data()["Prof"][key]["Select"])
            gBackground_data()["Prof"][key]["Select"] = [""] * plen

def set_Player_Prof_Select(sender, data, user_data):
    idx = user_data[0]
    cat = idx
    if idx in ["Artisan", "Gaming", "Musical"]: cat = "Tool"

    item = user_data[1]
    prof_list = gProf()["Player"][cat]
    master_list = gProf()[cat]
    
    if item in prof_list: prof_list.remove(item)
    else: prof_list.append(item)

def clear_Milestone_Level_Select(sender, data, user_data):
    index = user_data[0]
    
    if gMilestone()["Feat"][index]:
        prefeat = gMilestone()["Feat"][index]
        for key in list(gMilestone()["Data"].keys()):
            if prefeat == key:
                    gMilestone()["Data"].pop(key)
                    
    gMilestone()["Select"][index] = ""
    gMilestone()["Feat"][index] = ""
    gMilestone()["Asi"][index] = ["",""]

        
        
def set_Milestone_Level_Select(sender, data, user_data):
    index = user_data[0]
    gMilestone()["Select"][index] = data
    
    gMilestone()["Feat"][index] = ""
    gMilestone()["Asi"][index] = ["",""]



def set_Milestone_Feat_Select(sender, data, user_data):
    index = user_data[0]
    if data not in gMilestone()["Feat"]:
        gMilestone()["Feat"][index] = data
    
        if data in Feat_Select_L:
            gMilestone()["Data"][data] = {"Select": [""]}
        elif data == "Weapon Master":
            gMilestone()["Data"][data] = {"Select": ["","","",""]}
        else: 
            gMilestone()["Data"][data] = {}

def set_Milestone_Feat_Choice(sender, data, user_data):
    feat = user_data[0]
    index = user_data[1]
    if feat in list(gMilestone()["Data"].keys()):
        gMilestone()["Data"][feat]["Select"][index] = data 

def set_Milestone_Feat_Use(sender, data, user_data):
    feat = user_data[0]
    index = user_data[1]
    
    if feat in list(gMilestone()["Data"].keys()):
        gMilestone()["Data"][feat]["Use"][index] = data 

            
def set_Milestone_Asi_Select(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    gMilestone()["Asi"][key][index] = data











def set_Class_Use(sender, data, user_data):
    key=user_data[0]
    index = user_data[1]
    gClass_abil()[key]["Use"][index]=data


def set_Class_Skill_Select(sender, data, user_data):
    cat = user_data[0]
    if cat != "Clear":gClass_Skill()[cat]=data
    else: 
        for idx,val in enumerate(gClass_Skill()): gClass_Skill()[idx] = ""
        



def set_Class_select(sender, data, user_data):
    key = user_data[0]
    index = user_data[1]
    gClass_abil()[key]["Select"][index]=data



def set_Spell_Learn(sender, data, user_data):
    spell = user_data[0]
    level = user_data[1]
    cspell=gSpell()["Book"]
    sdata=gSpell_data()
    if level == 0:
        max_known = sdata['cantrips_available']
        current_known = get_cantrip_known()
        if spell not in cspell[level]: #add spell
            if current_known < max_known:
                cspell[level].append(spell)
        elif spell in cspell[level]:   #remove spell
            cspell[level].remove(spell)
    else:
        max_known = sdata['spells_available']
        current_known = get_spell_known()
        if spell not in cspell[level]: #add spell
            if current_known < max_known:
                cspell[level].append(spell)
        elif spell in cspell[level]:   #remove spell
            cspell[level].remove(spell)
            
            
            

def set_Spell_Prepare(sender, data, user_data):
    spell = user_data[0]
    level = user_data[1]
    
    cspell=gSpell()["Prepared"]
    sdata=gSpell_data()
    
    
    max_prep = sdata['prepared_available']
    current_prep = get_spell_prepared()

    if spell not in cspell[level]: #add spell
        if current_prep < max_prep:
            cspell[level].append(spell)
    elif spell in cspell[level]:   #remove spell
        cspell[level].remove(spell)
    
    


def set_Spell_Cast(sender, data, user_data):
    level = user_data[0]
    slots = gSpell()["Slot"][level]
    for i in range(len(slots)):
        if not slots[i]:
            slots[i] = True
            break

        

def set_Long_Rest(sender, data, user_data):
    if can_cast():
        for level in [1,2,3,4,5,6,7,8,9]:
            gSpell()["Slot"][level] = [False] * len(gSpell()["Slot"][level])




class_exception_map = {
    "Level 1": ["Cleric", "Warlock"],
    "Level 2": ["Wizard"]
}
def set_valid_class():
    Level = gLevel()
    Class = gClass()
    shared.db.Valid.Class = False
    if Level >=3:
        shared.db.Valid.Class = True
    elif Level == 2:
        if Class in class_exception_map["Level 2"]:
            shared.db.Valid.Class = True
    elif Level == 1:
        if Class in class_exception_map["Level 1"]:
            shared.db.Valid.Class = True
    else: print("error in valid class")


def set_spell_class():
    shared.db.Valid.Spell = gClass() in ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"]

def set_Health_Mod(sender, data, user_data):
    place, delta = user_data
    hp = gHP()
    
    if place == "Temp":
        if delta > 0 or hp["Temp"] > 0:
            hp["Temp"] += delta
            
            
            
    elif place == "HP":
        if delta < 0:
            if hp["Temp"] >= 1 and hp["Temp"] > 0:
                hp["Temp"] -= 1
            else:hp["Current"] -= 1
        else: hp["Current"] = min(hp["Current"] + 1, hp["Sum"])

def set_Arcane_Ward(sender, data, user_data):
    num = user_data[0]
    max_hp = gClass_abil()["Arcane Ward"]["HP"]["Max"]
    current_hp = gClass_abil()["Arcane Ward"]["HP"]["Current"]
    new_hp = current_hp + num
    new_hp = max(0, min(new_hp, max_hp))
    gClass_abil()["Arcane Ward"]["HP"]["Current"] = new_hp

def set_Player_Condition(sender, data, user_data):
    index = user_data[0]
    gCondition()[index] = data



def set_Characteristic_Input(sender, data, user_data):
    name = user_data[0]
    gCharacteristic()[name] = data

def set_Description_Input(sender, data, user_data):
    name = user_data[0]
    gDescription()[name] = data

#----------------
#SECTION - CLEAR
#----------------

