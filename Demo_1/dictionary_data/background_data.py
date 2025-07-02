# from dictionary_data.prof_data import *

# dict_Background = {
#     "Acolyte": {
#         "Given": {
#             "Skill": ["Insight", "Religion"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": [],
#                 "Lang": [],
#             },
#             "Equipment": {"Holy symbol": 1, "Prayer book": 1, "Stick of incense": 5, "Vestments": 1, "Common clothes": 1},
#             "Money": {"GP": 15}
#         },
#         "Feature": "Shelter of the Faithful",
#         "Choice": {
#             "Lang": {
#                 "Num": 2, 
#                 "Opt": list(dict_Lang.keys())
#             }
#         }
#     },
#     "Charlatan": {
#         "Given": {
#             "Skill": ["Deception", "Sleight of Hand"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": ["Disguise", "Forgery"],
#                 "Lang": [],
#             },
#             "Equipment": {"Fine clothes": 1, "Disguise kit": 1, "Tools of the con": 1},
#             "Money": {"GP": 15}
#         },
#         "Feature": "False Identity",
#         "Choice": {}
#     },
#     "Criminal": {
#         "Given": {
#             "Skill": ["Deception", "Stealth"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": ["Thief"],
#                 "Lang": [],
#             },
#             "Equipment": {"Crowbar": 1, "Dark common clothes with hood": 1},
#             "Money": {"GP": 15}
#         },
#         "Feature": "Criminal Contact",
#         "Choice": {
#             "Tool": {
#                 "Num": 1, 
#                 "Opt": list([k for k,v in dict_Tool.items() if v['Tag']=='Game'])
#             }
#         }
#     },
#     "Entertainer": {
#         "Given": {
#             "Skill": ["Acrobatics", "Performance"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": ["Disguise"],
#                 "Lang": [],
#             },
#             "Equipment": {"Admirers' favor": 1, "Costume": 1},
#             "Money": {"GP": 15}
#         },
#         "Feature": "By Popular Demand",
#         "Choice": {
#             "Tool": {
#                 "Num": 1, 
#                 "Opt": list([k for k,v in dict_Tool.items() if v['Tag']=='Music'])
#             }
#         }
#     },
#     "Folk Hero": {
#         "Given": {
#             "Skill": ["Animal Handling", "Survival"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": [],
#                 "Lang": [],
#             },
#             "Equipment": {"Shovel": 1, "Iron pot": 1, "Common clothes": 1},
#             "Money": {"GP": 10}
#         },
#         "Feature": "Rustic Hospitality",
#         "Choice": {
#             "Tool": {
#                 "Num": 1,
#                 "Opt": list([k for k,v in dict_Tool.items() if v['Tag']=='Job'])
#             }
#         }
#     },
#     "Guild Artisan": {
#         "Given": {
#             "Skill": ["Insight", "Persuasion"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": ["Tinker"],
#                 "Lang": [],
#             },
#             "Equipment": {"Letter of introduction": 1, "Traveler's clothes": 1},
#             "Money": {"GP": 15}
#         },
#         "Feature": "Guild Membership",
#         "Choice": {
#             "Tool": {
#                 "Num": 1,
#                 "Opt": list([k for k,v in dict_Tool.items() if v['Tag']=='Job'])
#             },
#             "Lang": {
#                 "Num": 1, 
#                 "Opt": list(dict_Lang.keys())
#             }
#         }
#     },
#     "Hermit": {
#         "Given": {
#             "Skill": ["Medicine", "Religion"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": ["Herbalism Kit"],
#                 "Lang": [],
#             },
#             "Equipment": {"Scroll case": 1, "Blank paper": 1, "Winter blanket": 1, "Common clothes": 1},
#             "Money": {"GP": 5}
#         },
#         "Feature": "Discovery",
#         "Choice": {
#             "Lang": {
#                 "Num": 1, 
#                 "Opt": list(dict_Lang.keys())
#             }
#         }
#     },
#     "Noble": {
#         "Given": {
#             "Skill": ["History", "Persuasion"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": [],
#                 "Lang": [],
#             },
#             "Equipment": {"Fine clothes": 1, "Signet ring": 1, "Scroll of pedigree": 1},
#             "Money": {"GP": 25}
#         },
#         "Feature": "Position of Privilege",
#         "Choice": {
#             "Lang": {
#                 "Num": 1, 
#                 "Opt": list(dict_Lang.keys())
#             },
#             "Tool": {
#                 "Num": 1, 
#                 "Opt": list([k for k,v in dict_Tool.items() if v['Tag']=='Game'])
#             }
#         }
#     },
#     "Outlander": {
#         "Given": {
#             "Skill": ["Athletics", "Survival"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": [],
#                 "Lang": [],
#             },
#             "Equipment": {"Staff": 1, "Hunting trap": 1, "Trophy": 1, "Traveler's clothes": 1},
#             "Money": {"GP": 10}
#         },
#         "Feature": "Wanderer",
#         "Choice": {
#             "Tool": {
#                 "Num": 1,  
#                 "Opt": list([k for k,v in dict_Tool.items() if v['Tag']=='Music'])
#             },
#             "Lang": {
#                 "Num": 1,  
#                 "Opt": list(dict_Lang.keys())
#             }
#         }
#     },
#     "Sage": {
#         "Given": {
#             "Skill": ["Arcana", "History"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": [],
#                 "Lang": [],
#             },
#             "Equipment": {"Bottle of ink": 1, "Quill": 1, "Notebook": 1, "Parchment": 1, "Small bag": 1},
#             "Money": {"GP": 10}
#         },
#         "Feature": "Researcher",
#         "Choice": {
#             "Lang": {
#                 "Num": 2,  
#                 "Opt": list(dict_Lang.keys())
#             }
#         }
#     },
#     "Sailor": {
#         "Given": {
#             "Skill": ["Athletics", "Perception"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": ["Navigator"],
#                 "Lang": [],
#             },
#             "Equipment": {"Belaying pin": 1, "50 feet of rope": 1, "Lucky charm": 1, "Common clothes": 1},
#             "Money": {"GP": 10}
#         },
#         "Feature": "Ship's Passage",
#         "Choice": {}
#     },
#     "Soldier": {
#         "Given": {
#             "Skill": ["Athletics", "Intimidation"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": [],
#                 "Lang": [],
#             },
#             "Equipment": {"Rank insignia": 1, "Trophy": 1, "Dice or deck": 1, "Common clothes": 1},
#             "Money": {"GP": 10}
#         },
#         "Feature": "Military Rank",
#         "Choice": {
#             "Tool": {
#                 "Num": 1,  
#                 "Opt": list([k for k,v in dict_Tool.items() if v['Tag']=='Game'])
#             }
#         }
#     },
#     "Urchin": {
#         "Given": {
#             "Skill": ["Sleight of Hand", "Stealth"],
#             "Prof": {
#                 "Armor": [],
#                 "Weapon": [],
#                 "Tool": ["Disguise", "Thief"],
#                 "Lang": [],
#             },
#             "Equipment": {"Small knife": 1, "Map": 1, "Pet mouse": 1, "Token": 1, "Common clothes": 1},
#             "Money": {"GP": 10}
#         },
#         "Feature": "City Secrets",
#         "Choice": {}
#     }
# }



    
# dict_background_feature = {
#     "Shelter of the Faithful": {
#         "Desc": "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material components needed for spells. Those who share your religion will support you (but only you) at a modest lifestyle. You might also have ties to a specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This could be the temple where you used to serve, if you remain on good terms with it, or a temple where you have found a new home. While near your temple, you can call upon the priests for assistance, provided the assistance you ask for is not hazardous and you remain in good standing with your temple."
#     },
#     "False Identity": {
#         "Desc": "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy"
#     },
#     "Criminal Contact": {
#         "Desc": "You have a reliable and trustworthy contact who acts as your liaison to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."
#     },
#     "By Popular Demand": {
#         "Desc": "You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a town where you have performed, they typically take a liking to you."
#     },
#     "Rustic Hospitality": {
#         "Desc": "Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you."
#     },
#     "Guild Membership": {
#         "Desc": "As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings. Guilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild's coffers. You must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild's good graces."
#     },
#     "Discovery": {
#         "Desc": "The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion. It might be a great truth about the cosmos, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that has long been forgotten, or unearthed some relic of the past that could rewrite history. It might be information that would be damaging to the people who or consigned you to exile, and hence the reason for your return to society."
#     },
#     "Position of Privilege": {
#         "Desc": "Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to."
#     },
#     "Wanderer": {
#         "Desc": "You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth."
#     },
#     "Researcher": {
#         "Desc": "When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign."
#     },
#     "Ship's Passage": {
#         "Desc": "When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you're calling in a favor, you can't be certain of a schedule or route that will meet your every need. Your Dungeon Master will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage."
#     },
#     "Military Rank": {
#         "Desc": "You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized."
#     },
#     "City Secrets": {
#         "Desc": "You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow."
#     }
# }
