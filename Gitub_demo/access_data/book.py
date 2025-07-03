from .Grimoir import *
from .weapon_reference import *



Race_Options={
    "Human": ["Standard", "Variant"],
    "Elf": ["High", "Drow", "Wood", "ShadarKai"],
    "Dwarf": ["Hill", "Mountain"],
    "Halfling": ["Lightfoot", "Stout"],
    "Gnome": ["Forest", "Rock"],
    "Dragonborn": ["Black", "Blue", "Brass", "Bronze", "Copper", "Gold","Green","Red","Silver","White"],
    "HalfOrc": ["Standard"],
    "Tiefling": ["Asmodeus","Baalzebul", "Dispater", "Fierna", "Glasya", "Levistus", "Mammon", "Mephistopheles", "Zariel"],
    "Harengon": ["Standard"]
}


Class_Options = {
    "Fighter": ["Champion", "BattleMaster", "EldrichKnight"],
    "Wizard": ["Abjuration", "Conjuration",]
}
#"Enchantment", "Evocation", "Illusion", "Necromancy" 
Race_L=list(Race_Options.keys())
Class_L=list(Class_Options.keys())
Background_L = ["Charlatan","Criminal","Entertainer","Folk Hero","GuildArtisan","Hermit","Noble","Outlander","Sage","Sailor","Soldier","Urchin"]

spellcast_L = ["Wizard", "EldrichKnight"]


Feat_L= ["Actor", "Alert", "Athlete", "Charger", "CrossbowExpert", "DefensiveDuelist", "DualWielder", "DungeonDelver", "Durable", "ElementalAdept", "Grappler", "GreatWeaponMaster", "Healer", "HeavilyArmored", "HeavyArmorMaster", "InspiringLeader", "KeenMind", "LightlyArmored", "Lucky", "MageSlayer", "MartialAdept", "MediumArmorMaster", "Mobile", "ModeratelyArmored", "MountedCombatant", "PolearmMaster", "Resilient", "SavageAttacker", "Sentinel", "Sharpshooter", "ShieldMaster", "Skulker", "TavernBrawler", "Tough", "WarCaster", "WeaponMaster"]
Feat_Select_L= ["ModeratelyArmored","LightlyArmored","ElementalAdept","Athlete"]


Prof_L = ["Armor","Weapon","Tool","Lang"]



Level_L = [i for i in range(1, 21)]
Base_Atr_L = [i for i in range(1,19)]

Atr_L = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

Description_L = ["Gender", "Almnt", "Faith", "Size", "Age", "Hair", "Skin", "Eyes", "Height", "Weight"]

ideals_L = ["Traits", "Ideals", "Bonds", "Flaws"]
Condition_L = ["Blinded", "Charmed", "Deafened", "Frightened", "Grappled", "Incapacitated", "Invisible", "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious", "Exhaustion"]


Spell_Desc_L = ["Level","Casting Time", "Duration", "School", "Ritual","Range","Components","Desc", "At Higher Levels"]


#-------
## LINK - #! Spells
#-------

def spell_not_cantrip(spell_name):
    return Grimoir[spell_name]["Level"] != 0


def get_spell_list(Class, level):
    return [spell for spell, v in Grimoir.items() if v['Level'] == level and Class in v['List']]


#-------
## LINK - #! Class based shit
#-------



spell_default = {
    "Slot": [[],[],[],[],[],[],[],[],[],[]],
    "Book": [[],[],[],[],[],[],[],[],[],[]],
    "Prepared": [[],[],[],[],[],[],[],[],[],[]]
}


spell_data_default = {
    "Caster": "",
    "max_spell_level": [0,0,0,0,0,0,0,0,0,0],
    "cantrips_available": 0,
    "spells_available": 0,
    "slots": [[],[],[],[],[],[],[],[],[],[]],
    "abil": "",
    "mod": 0,
    "atk": "",
    "prepared_available": 0
    
}

dict_Feat_Count = {
    'Fighter': [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7],
    'Rogue': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6],
    'Wizard': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Ranger': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5],
    'Paladin': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5]
}




#ANCHOR - Speed Dict
dict_Speed = {
    "Walk": {},
    "Climb": {},
    "Swim": {},
    "Fly": {}, 
    "Burrow": {}
} 

#ANCHOR - Vision Dict
dict_Vision = {
    "Dark": {}, 
    "Blind": {},
    "Tremor": {},
    "Tru": {}
}


#ANCHOR - Speed Dict
dict_Skill = {
    "Acrobatics": {"Atr": "DEX", "Desc": "Balance, flips, and avoiding being knocked down."},
    "Animal Handling": {"Atr": "WIS", "Desc": "Control and calm animals or read their behavior."},
    "Arcana": {"Atr": "INT", "Desc": "Knowledge of magic, spells, and magical traditions."},
    "Athletics": {"Atr": "STR", "Desc": "Climbing, jumping, swimming, and grappling."},
    "Deception": {"Atr": "CHA", "Desc": "Lying, bluffing, and misleading others."},
    "History": {"Atr": "INT", "Desc": "Recall historical facts, people, and events."},
    "Insight": {"Atr": "WIS", "Desc": "Detecting lies, motives, and emotions."},
    "Intimidation": {"Atr": "CHA", "Desc": "Threatening or coercing others into compliance."},
    "Investigation": {"Atr": "INT", "Desc": "Finding hidden clues or analyzing scenes."},
    "Medicine": {"Atr": "WIS", "Desc": "Stabilize the dying and diagnose illnesses."},
    "Nature": {"Atr": "INT", "Desc": "Knowledge of plants, animals, and the environment."},
    "Perception": {"Atr": "WIS", "Desc": "Noticing hidden things or sudden changes."},
    "Performance": {"Atr": "CHA", "Desc": "Acting, singing, dancing, and entertaining."},
    "Persuasion": {"Atr": "CHA", "Desc": "Convincing others with logic or charm."},
    "Religion": {"Atr": "INT", "Desc": "Understanding deities, rites, and dogma."},
    "Sleight of Hand": {"Atr": "DEX", "Desc": "Pickpocketing or manipulating objects subtly."},
    "Stealth": {"Atr": "DEX", "Desc": "Sneaking, hiding, and moving silently."},
    "Survival": {"Atr": "WIS", "Desc": "Tracking, finding food, and navigating the wild."}
}

#ANCHOR - Proficiency Dict

#SECTION - Prof Armor
dict_Armor = {
    "Light": {},
    "Medium": {},
    "Heavy": {},
    "Shield": {}
}

#SECTION - Prof Tool
dict_Tool = {
    "Alchemist": {"Tag": "Job"}, "Brewer": {"Tag": "Job"}, "Calligrapher": {"Tag": "Job"}, "Carpenter": {"Tag": "Job"}, "Cartographer": {"Tag": "Job"}, "Cobbler": {"Tag": "Job"}, "Cook": {"Tag": "Job"}, "Glassblower": {"Tag": "Job"}, "Jeweler": {"Tag": "Job"}, "Leatherworker": {"Tag": "Job"}, "Mason": {"Tag": "Job"}, "Painter": {"Tag": "Job"}, "Potter": {"Tag": "Job"}, "Smith": {"Tag": "Job"}, "Tinker": {"Tag": "Job"}, "Weaver": {"Tag": "Job"}, "Thief": {"Tag": "Job"}, "Woodworker": {"Tag": "Job"}, "Navigator": {"Tag": "Job"}, "Disguise": {"Tag": "Job"}, "Forgery": {"Tag": "Job"},
    "Dice": {"Tag": "Game"}, "Dragonchess": {"Tag": "Game"}, "Cards": {"Tag": "Game"}, "Three-Dragon Ante": {"Tag": "Game"},
    "Bagpipes": {"Tag": "Music"}, "Drum": {"Tag": "Music"}, "Dulcimer": {"Tag": "Music"}, "Flute": {"Tag": "Music"}, "Lute": {"Tag": "Music"}, "Lyre": {"Tag": "Music"}, "Horn": {"Tag": "Music"}, "Pan Flute": {"Tag": "Music"}, "Shawm": {"Tag": "Music"}, "Viol": {"Tag": "Music"}
}


#SECTION - Prof Lang
dict_Lang = {
    "Common": {},
    "Dwarvish": {},
    "Elvish": {},
    "Giant": {},
    "Gnomish": {},
    "Goblin": {},
    "Halfling": {},
    "Orc": {},
    "Abyssal": {},
    "Celestial": {},
    "Draconic": {},
    "Deep Speech": {},
    "Infernal": {},
    "Primordial": {},
    "Sylvan": {},
    "Undercommon": {}
}



#!SECTION Data List
Armor_L = list(dict_Armor.keys())
Weapon_Simple_L = [k for k, v in dict_Weapon.items() if v["cat1"] == "Simple"]
Weapon_Martial_L = [k for k, v in dict_Weapon.items() if v["cat1"] == "Martial"]
Job_L = [k for k, v in dict_Tool.items() if v["Tag"] == "Job"]
Game_L = [k for k, v in dict_Tool.items() if v["Tag"] == "Game"]
Music_L = [k for k, v in dict_Tool.items() if v["Tag"] == "Music"]
Lang_L = list(dict_Lang.keys())
Skill_L = list(dict_Skill.keys())


Vision_L = list(dict_Vision.keys())
Speed_L = list(dict_Speed.keys())




dl = {
    "Cantrip": [spell for spell, v in Grimoir.items() if v['Level'] == 0 and 'Wizard' in v['List']],
    
    # Class Skills
    "Fighter Skills": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
    "Wizard Skills":  ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],

    # Feats
    
    "Athlete": ["STR", "DEX"],
    "LightlyArmored": ["STR","DEX"],
    "ModeratelyArmored": ["STR", "DEX"],
    "ElementalAdept": ["Acid", "Cold", "Fire", "Lightning", "Thunder"],
    "Resiliant": Atr_L,
    "WeaponMaster": list(dict_Weapon.keys()),
    
    # Backgrounds

    "Acolyte": {"Lang": Lang_L},
    "Charlatan": {},
    "Criminal": {"Game": Game_L},
    "Entertainer": {"Music": Music_L},
    "FolkHero": {"Job": Job_L},
    "GuildArtisan": {"Job": Job_L, "Lang": Lang_L},
    "Hermit": {"Lang": Lang_L},
    "Noble": {"Game": Game_L, "Lang": Lang_L},
    "Outlander": {"Music": Music_L, "Lang": Lang_L},
    "Sage": {"Lang": Lang_L},
    "Sailor": {},
    "Soldier": {"Game": Game_L},
    "Urchin": {},

    "Fighting Styles": ["Archery", "Defense", "Great Weapon Fighting", "Protection", "Two Weapon Fighting", "Blind Fighting", "Interception", "Thrown Weapon Fighting", "Unarmed Fighting"],
    "Maneuvers": ["Ambush", "Bait and Switch", "Brace", "Commander's Strike", "Commanding Presence", "Disarming Attack", "Distracting Strike", "Evasive Footwork", "Feinting Attack", "Goading Attack", "Grappling Strike", "Lunging Attack", "Maneuvering Attack", "Menacing Attack", "Parry", "Precision Attack", "Pushing Attack", "Quick Toss", "Rally", "Riposte", "Sweeping Attack", "Tactical Assessment", "Trip Attack"],
    "Student of War": {"Job": Job_L}
}




