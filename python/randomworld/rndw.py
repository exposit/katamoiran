#!/usr/bin/env python

# this is going to assume that the user has a copy of Simple World;
# the only content directly from SW is the six lines of Move templates

import random

# giant list of keywords
keywords = [
"plague", "searching", "keeping", "stealing", "rose", "honor", "locate", "chase", "explore", "deliver", "hunt", "befriend", "persuade", "barter", "protect", "collect", "sleuth", "respite", "restore", "destroy", "prepare", "interrupt", "return", "passion", "redemption", "justice", "attack", "resist", "future", "secret", "revenge", "distance", "anger", "supply", "power", "desire", "choice", "phobia", "ice", "lust", "dirt", "machinery", "pride", "love", "betrayal", "duty", "mistake", "debt", "fire", "air", "death", "pain", "history", "need", "flaw", "fear", "guilt", "purity", "vice", "artifice", "romance", "war", "fire", "air", "water", "earth", "stealth", "madness", "mobius", "time", "distance", "travel", "oration", "mind", "seduction", "deduction", "spirit", "shadow", "fanatic",
]

# remove duplicates so we can be free with adding keywords
keywords = list(set(keywords))

# giant list of class-type roles; needs more options for sure
roles = [
"druid",
"monk",
"thief",
"templar",
"cleric",
"bard",
"fighter",
"warrior",
"paladin",
"psion",
"mindblade",
"adept",
"mage",
"wizard",
"sorcerer",
"spellsword",
"arcane knight",
"berserker",
"ranger",
"spy",
]

# every role needs at least one specialty but more is better
specialties = {
"heal someone" : ["druid", "cleric", "paladin", "keeping", "respite", "restore", "passion" ],
"cure someone" : ["druid", "cleric", "paladin", "plague", "rose", "restore", ],
"deal damage" : ["fighter", "warrior", "templar", "bard", "cleric", "monk", 'berserker', "arcane knight", "spellsword", "mindblade", "rose", "ranger", "destroy", "attack", "anger", "death" ],
"inspire others" : ["bard", "cleric", "rose", "honor", "justice", "resist" ],
"strike a death blow" : ["fighter", "warrior", "templar", "bard", "cleric", "monk", 'berserker', "arcane knight", "spellsword", "mindblade", "rose", "ranger", "destroy", "attack", "anger", "death", "war" ],
"steal" : ["thief", "bard", "stealing", ],
"pick pockets" : ["thief", "bard", "stealing", ],
"hide in shadows" : ["thief", "stealth", "shadow", "spy", ],
"confront evil" : ["paladin", "templar", "keeping", "honor", "resist", "spirit", ],
"cleave foes" : ["fighter", "paladin", "warrior", 'berserker',],
"dodge out of the way" : ["thief", "mindblade", "interrupt", ],
"channel magic through a focus" : ["arcane knight", "spellsword", "mindblade",],
"cast a spell" : ["spellsword", "power", "choice", "madness" ],
"manipulate emotions" : ["psion", "love", "need", "lust", "fear", "desire", "anger", "guilt", "romance", "madness", "spirit" ],
"manipulate minds" : ["adept", "sorcerer", "psion", "madness", "mind"],
"change something into something else" : ["mage", "wizard", "sorcerer",],
"weave an illusion" : ["adept", "mage", "wizard", "sorcerer", "psion",],
"look into the unknown" : ["adept", "mage", "wizard", "sorcerer", "psion", "explore", "sleuth", "madness", "mind"],
"fly into a rage" : ['berserker', "power", ],
"protect someone else" : ["arcane knight", "protect", "paladin", "resist", "romance", "spirit"],
"manifest a weapon" : ["mindblade",],
"find something missing" : ["adept", "searching", "locate", "chase", "sleuth"],
"uphold a vow" : ["paladin", "templar", "honor", "deliver", "redemption", "revenge", "pride", "love", "duty", "purity", "romance", "fanatic", "spy" ],
"track a thing down" : ["ranger", "chase", "hunt", "spy"],
"run prey to ground" : ["ranger", "chase", "hunt", "spy", "sleuth"],
"socialize in a friendly way" : ["bard", "befriend", "persuade", "rose", "desire", "persuade"],
"use persuasion" : ["persuade", "rose", "oration", ],
"seduce someone" : ["bard", "desire", "rose", "lust", "love", "vice", "romance", "seduction" ],
"make a bargain" : ["bard", "barter", "collect", "supply", "debt", "vice", ],
"declare you planned for this" : ["psion", "mage", "bard", "prepare", "time", "mobius", "interrupt", "future", "past", "history", "secret", "revenge", "madness", "mind", "deduction", ],
"get back up after getting knocked down" : ["fighter", "warrior", "return"],
"bring wrongdoing to an end" : ["ranger", "paladin", "templar", "justice", "return", "revenge"],
"stubbornly refuse" : ["resist", "berserker", "madness", ],
"travel a long way" : ["distance", "ranger", ],
"inspire fear" : ["phobia", "wizard", "sorcerer", "adept", "mindblade", "psion" ],
"invoke ice or cold" : ["ice", "wizard", "mage", "adept", ],
"invoke fire or heat" : ["fire", "wizard", "mage", "adept", ],
"harness the wind or weather" : ["air", "wizard", "mage", "adept", ],
"command water" : ["water", "wizard", "mage", "adept", ],
"move earth" : ["dirt", "earth", "mage", "wizard", "adept", ],
"activate a gadget" : ["machinery", "artifice", ],
"engage in competition" : ["pride", "warrior", "berserker", ],
"betray someone" : ["betrayal", "thief", "spy", ],
"royally screw up" : ["mistake", "flaw", ],
"strike at a weakness" : ["flaw", "mistake", ],
"give someone power over you" : ["debt", ],
"cause unnecessary pain" : ["pain", "spy", "vice", ],
#"" : [],
}

premise = random.choice(keywords)

# number of playbooks
pcount = random.randint(3,6)

pbA = random.sample(roles, pcount)
pbB = random.sample(keywords, pcount)

playbooks = []
pbspecialties = []
for i in range(0, len(pbA)):
    subspecialties = []
    playbooks.append(pbB[i] + " " + pbA[i])
    for key,value in specialties.items():
        if pbA[i] in value:
            subspecialties.append(key)
    pbspecialties.append(subspecialties)

# and probably a core dichotomy, like honor vs discipline or something
cards = [
["Ace", "Hearts", "Fool", "Freedom", "Isolation"],
["2", "Hearts", "Messenger", "communication", "miscommunication",],
["3", "Hearts", "Spring", "Newness", "Corruption"],
["4", "Hearts", "Cross", "Belief", "Disbelief"],
["5", "Hearts", "Moon", "Enthusiasm", "Fickleness"],
["6", "Hearts", "Satyr", "Tolerance", "Indulgence"],
["7", "Hearts", "Crossroad", "choice", "restriction"],
["8", "Hearts", "Muse", "inspiration", "madness"],
["9", "Hearts", "Eros", "desire", "obsession"],
["10", "Hearts", "Feather", "hope", "despair"],
["Jack", "Hearts", "Lover", "love", "jilt"],
["Queen", "Hearts", "Priestess", "mysteries revealed", "reckless curiosity"],
["King", "Hearts", "Mentor", "sacrifice", "jealousy"],

["Ace", "Diamonds", "Tower", "Alliance", "Solitude"],
["2", "Diamonds", "Fox", "Cunning", "Cynicism"],
["3", "Diamonds", "Autumn", "abundance", "lack"],
["4", "Diamonds", "Status Quo", "Order", "Rebellion"],
["5", "Diamonds", "Succubus", "Power at a Cost", "Temptation"],
["6", "Diamonds", "Treasure", "windfall", "thieves"],
["7", "Diamonds", "Armor", "protection", "overprotection"],
["8", "Diamonds", "Key", "Open", "Close"],
["9", "Diamonds", "Magpie", "collect", "waste"],
["10", "Diamonds", "Peacock", "amusement", "vanity"],
["Jack", "Diamonds", "Merchant", "calculated risk", "debt"],
["Queen", "Diamonds", "Luck", "good fortune", "mischance"],
["King", "Diamonds", "Dragon", "self-interest", "hoarding"],

["Ace", "Spades", "Phoenix", "Rebirth", "Destruction"],
["2", "Spades", "Wolf", "Outsider", "Outcast"],
["3", "Spades", "Summer", "Passion", "Exhaustion"],
["4", "Spades", "Vampire", "Natural", "Supernatural"],
["5", "Spades", "Shadows", "justified caution", "fear of shadows"],
["6", "Spades", "Whip", "Pleasure", "Pain"],
["7", "Spades", "Ship", "journey", "shipwreck"],
["8", "Spades", "Crossed Swords", "combat", "subjugation"],
["9", "Spades", "Toy", "novelty", "recklessness"],
["10", "Spades", "Fertility", "Purposeful Growth", "Wantonness"],
["Jack", "Spades", "Soldier", "skill", "overspecialization"],
["Queen", "Spades", "Amazon", "power", "arrogance"],
["King", "Spades", "Death", "change", "stasis"],

["Ace", "Clubs", "Unicorn", "Innocence", "Ruse"],
["2", "Clubs", "Stars", "Insight", "Overreach"],
["3", "Clubs", "Winter", "Hard Choice", "Selfishness"],
["4", "Clubs", "Birds", "Intuition", "Logic"],
["5", "Clubs", "Sun", "revelation", "blindness"],
["6", "Clubs", "Trial", "truth", "falsehood"],
["7", "Clubs", "Child", "maturity", "childishness"],
["8", "Clubs", "Veil", "disguise", "self-deception"],
["9", "Clubs", "Anchor", "security", "weight"],
["10", "Clubs", "Palace", "luxury", "bureaucracy"],
["Jack", "Clubs", "Judge", "justice", "injustice"],
["Queen", "Clubs", "Empress", "generosity", "generosity with strings"],
["King", "Clubs", "Emperor", "authority", "tyranny"]
]

# Principles, Agenda, GM Moves
agenda = ["Challenge yourself; ask difficult questions.", "Play to find out what happens."]

agendalist = [
"Make the heroes' lives bold and full of larger than life dilemmas.",
"Fill the heroes' lives with darkness to throw the light into relief.",
"Fill the heroes' lives with dilemmas and wonder.",
"Fill the heroes' lives with tension and unexpected twists.",
"Fill the heroes' lives with risk and adventure.",
"Fill the heroes' lives with chivalry and romance.",
]

agenda.append(random.choice(agendalist))

principles = ["Be a fan of the heroes, but make them prove they deserve the role.",
"Nobody has plot immunity; nothing is safe. Build the world and mythos as you go.",
"Be honest, even when it hurts; follow the fiction where it leads.",]

principlelist = [
"Look for the extremes of good and evil but explore the gray areas in between.",
"Juxtapose the normal and the horrific, the mundane and the uneasily other.",
"The heroes are a wild card and people will look to them to solve their problems.",
"Sex is always a factor; everyone wants to consume the heroes.",
"The heroes are special; celebrate it but also make them prove it.",
"Seek out the exotic and strange but interject the familiar.",
"The truth is all-powerful; oaths and bargains have their own magic.",
]

principles = principles + random.sample(principlelist, random.randint(1,len(principlelist)))

# choose some stat names at random

# Reflexive/Graceful
reflex = ["Reflex", "Grace", "Cool", "Dexterity", "Quickness", "Grasp"]

# Persuasive/Assertive
social = ["Persuasion", "Assertiveness", "Hotness", "Charm", "Charisma", "Social", "Glib"]

# Aggressive/Forceful
force = ["Aggression", "Force", "Hardness", "Daring", "Combat", "Strength", "Attack"]

# Calculating/Methodical
mind = ["Calculation", "Precision", "Cunning", "Sharp", "Intelligence", "Mind", "Brains"]

# Inquisitive/Exploratory
explore = ["Inquisitiveness", "Curiousity", "Whim", "Weird", "Sensitive", "Wisdom", "Magic", "Spirit"]

# but just set them to recognizable defaults for now for sanity testing
reflex = ["Dexterity"]
social = ["Charisma"]
force = ["Strength"]
mind = ["Intelligence"]
explore = ["Magic"]
# end comment out block

stats = [
random.choice(reflex),
random.choice(social),
random.choice(force),
random.choice(mind),
random.choice(explore),
]

card = random.choice(cards)

print()
print("*** " + card[2] + " World ***")
print()

print("The theme of the setting is \"" + premise + "\".")

print()

print("The main struggle is between \"" + card[3].lower() + "\" and \"" + card[4].lower() + "\".")

print()

print("The Stats are: " + ", ".join(stats) + ".\n")

print("Your Agenda is:\n" + "\n".join(agenda))
print()
print("Your Principles Are:\n" + "\n".join(principles))

# generate a playbook for each of the premise playbooks, suggesting a stat but allowing the end user to customize it

movetypes = [
"When you do something relating to [specialty], add +1.",
"You have the ability to [do some sort of active special power]. It counts as a basic move using [statA].",
"You have [some passive special power that has a constant effect].",
"You have a [thing]. When applicable, it adds +1 to [statA] and [statB].",
"When you do [specialty], mark XP.",
"Add +1 to [statA].",
]

# these are the playbooks
count = 0
for item in playbooks:

    print("\n")

    moves = [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)] + [random.choice(movetypes)]

    movecats = random.sample(["Explore", "Fight", "Social", "Weird"], 2) + random.sample(["Explore", "Fight", "Social", "Weird"], 2)

    keyword = random.choice(keywords)

    kwspecialties = []
    for key,value in specialties.items():
        if keyword in value:
            kwspecialties.append(key)

    themespecialties = []
    for key,value in specialties.items():
        if premise in value:
            themespecialties.append(key)

    corespecialties = []
    for key,value in specialties.items():
        if item.split()[0] in value:
            corespecialties.append(key)

    for i in range(len(moves)):
        if "[statB]" in moves[i]:
            temp = random.sample(stats,2)
            moves[i] = moves[i].replace("[statA]", temp[0])
            moves[i] = moves[i].replace("[statB]", temp[1])
        if "[statA]" in moves[i]:
            moves[i] = moves[i].replace("[statA]", random.choice(stats))
        if "[specialty]" in moves[i] and i == 0:
            # core class move
            moves[i] = moves[i].replace("[specialty]", "\x1B[3m" + random.choice(corespecialties) + "\x1B[23m")
        if "[specialty]" in moves[i] and i == 4:
            # unique keyword move
            moves[i] = moves[i].replace("[specialty]", "\x1B[3m" + random.choice(kwspecialties) + "\x1B[23m")
        if "[specialty]" in moves[i] and i == 5:
            # theme move
            moves[i] = moves[i].replace("[specialty]", "\x1B[3m" + random.choice(themespecialties) + "\x1B[23m")
        if "[specialty]" in moves[i]:
            moves[i] = moves[i].replace("[specialty]", "\x1B[3m" + random.choice(pbspecialties[count]) + "\x1B[23m")

    print(item.upper())
    print()

    #print("Title")

    titlelist = ["Core Class Move", movecats[0] + " Move", movecats[1] + " Move", movecats[2] + " Move", keyword.title() + " Move (\x1B[3munique keyword for this playbook\x1B[23m)", random.choice([card[3],card[4]]).title() + " Move (\x1B[3mrelates to the core dilemma of the setting\x1B[23m)", premise.title() + " Move (\x1B[3mrelates to the theme of the setting\x1B[23m)" ]

    for x in range(len(titlelist)):
        print(titlelist[x])
        print(moves[x])
        print()

    count = count + 1
