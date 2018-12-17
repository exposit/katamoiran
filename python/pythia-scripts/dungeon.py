# this is ported from Pythia Oracle
# it is MIT licensed like Pythia Oracle
# https://github.com/exposit/pythia-oracle
import random
import time
import string
import sys

if len(sys.argv) > 1:
    try:
        area_count = int(sys.argv[1])
    except:
        area_count = 5
else:
    area_count = 5

dungeon_stocking_method = "Gygax" # anything else here besides "Gygax" will do Moldovay

past_dungeon_areas = []

def getFullDungeonArea():

    current_dungeon_name = "Dungeon!"

    dungeon_area_themes = ['Treasure', 'Stone', 'Lust', 'Pain', 'Ice', 'Fire', 'Water', 'Sorrow', 'Grief', 'Respite', 'Forsaken', 'Fury', 'Violence', 'Spite', 'Gold', 'Silver', 'Jewels', 'Fungus', 'Plants', 'Garden', 'Magic', 'Study', 'Home', 'Maze', 'Library', 'Clockwork', 'Demonic', 'Hellish', 'Chaotic', 'Malice' ]

    dungeon_area_types = ['Dungeon', 'Dwelling', 'Lair', 'Temple', 'Caverns', 'Caves', 'Tunnels', 'Wilderness', 'Crypts', 'Catacombs', 'Lab', 'Fortress', 'Mine', 'City', 'Garden' ]

    dungeon_area_activity_level = ['Deserted', 'Infested', 'Swarming', 'Inactive', 'Active', 'Busy', 'Desolate', 'Abandoned', 'Empty', 'Haunted', 'Quiet', 'Heavily Trafficked', 'Contested', 'Contested', 'Contested' ]

    dungeon_theme_randomness = 85
    dungeon_type_randomness = 30
    dungeon_activity_randomness = 50

    backtrack_chance = 10

    if len(past_dungeon_areas) > 0:
        current_theme = past_dungeon_areas[-1][0]
        current_type = past_dungeon_areas[-1][1]
        current_activity = past_dungeon_areas[-1][2]
    else:
        current_theme = random.choice(dungeon_area_themes)
        current_type = random.choice(dungeon_area_types)
        current_activity = random.choice(dungeon_area_activity_level)

    room_count = str(random.randint(1, 4) * 2)

    backtrack_roll = random.randint(1, 100)

    theme_change_roll = random.randint(1, 100)
    type_change_roll = random.randint(1, 100)
    activity_change_roll = random.randint(1, 100)

    # is this area the same type as the last?
    if theme_change_roll <= dungeon_theme_randomness:
        possible_themes = random.sample(dungeon_area_themes, 2)
        if possible_themes[0] != current_theme:
            new_theme = possible_themes[0]
        else:
            new_theme = possible_themes[1]
    else:
        new_theme = current_theme

    if type_change_roll <= dungeon_type_randomness:
        possible_types = random.sample(dungeon_area_types, 2)
        if possible_types[0] != current_type:
            new_type = possible_types[0]
        else:
            new_type = possible_types[1]
    else:
        new_type = current_type

    if activity_change_roll <= dungeon_activity_randomness:
        possible_activity = random.sample(dungeon_area_activity_level, 2)
        if possible_activity[0] != current_activity:
            new_activity = possible_activity[0]
        else:
            new_activity = possible_activity[1]
    else:
        new_activity = current_activity

    # now, see if the new stuff takes effect or if we're going back to an existing area
    if backtrack_roll <= backtrack_chance and len(past_dungeon_areas) > 1:
        index = random.randint(0, len(past_dungeon_areas)-1)
        new_theme = past_dungeon_areas[index][0]
        new_type = past_dungeon_areas[index][1]
        new_activity = past_dungeon_areas[index][2]
        result = "You've found a connection to an already explored area [%s]. You can explore %s more rooms in the old area or continue into a new one." % (str(index+1), room_count)
    else:
        past_dungeon_areas.append([new_theme, new_type, new_activity])
        new_area = new_type + " (" + new_theme + ", " + new_activity + ")"
        result = "%s %s. %s rooms." % (str(len(past_dungeon_areas)), new_area, room_count)

    return result, int(room_count)

# dress some rooms
def roomLike(area_index,room_index):

    oppositesChart = [
        ["rough", "smooth"],
        ["gleaming", "dull"],
        ["slick", "dry"],
        ["crumbling", "intact"],
        ["extreme", "mild"],
        ["cared for", "disused"],
        ["stone", "metal"],
        ["wood", "brick"],
        ["wood", "metal"],
        ["stone", "brick"],
        ["painted", "bare"],
        ["finished", "unfinished"],
        ["ostentatious", "spartan"],
        ["bare", "stuffed"],
        ["worn", "new-looking"],
        ["expansive", "miserly"],
        ["lavish", "spare"],
        ["bright", "dim"],
        ["pristine", "dirty"],
        ["faded", "vibrant"],
        ["slippery", "sticky"],
        ["broken", "unmarred"],
    ]
    descChart = []
    for pairList in oppositesChart:
        descChart.append(random.choice(pairList))

    roll = random.randint(1, 3)
    descList = random.sample(descChart, roll)
    desc = ', '.join(descList)

    shapeChart = [
        "round", "square", "oval", "elongated", "rectangular", "trapezoidal",
    ]

    roll = random.choice([1,1,1,2])
    shapeList = random.sample(shapeChart, roll)
    shape = ', '.join(shapeList)

    sizeChart = [
        "large", "small", "average", "standard", "medium", "cubby", "alcove", "cavern", "nook", "chamber", "vault", "great", "negligible", "brief", "vast", "expansive", "extensive", "double-size",
    ]
    size = random.choice(sizeChart)

    purposeChart = [
        "sleeping", "eating", "bathing", "bodily functions", "imprisoning", "killing", "disposal", "studying", "reading", "working", "crafting", "disassembling", "assembling", "interrogating", "relaxing", "recuperating", "mending", "rending", "cooking", "exercise", "planning", "plotting", "praying", "keeping", "displaying", "storing", "feasting", "resting", "meditating", "confining", "stashing", "protecting"
    ]

    roll = random.choice([1,2])
    purposeList = random.sample(purposeChart, roll)
    purpose = ', '.join(purposeList)

    result = "[%s-%s] %s [Purpose] %s [Size] %s [Shape] %s" % (area_index, room_index, desc, purpose, size, shape)

    return result

def getRoomContents():

    if dungeon_stocking_method == "Gygax":

        chart = { "Empty": 12, "Monster Only": 2, "Monster & Treasure": 3, "Special or Stairway": 1, "Trick/Trap": 1, "Treasure": 1 }

        contents = random.choice([k for k in chart for dummy in range(chart[k])])

    else:

        chart = { "Monster": 2, "Trap": 1, "Special": 1, "Empty" : 2 }
        contents = random.choice([k for k in chart for dummy in range(chart[k])])

        troll = random.randint(1,6)

        treasure = ""
        if contents == "Monster" and troll <= 3:
            treasure = "Treasure!"
        elif contents == "Trap" and troll <= 2:
            treasure = "Treasure!"
        elif contents == "Empty" and troll == 1:
            treasure = "Treasure!"
        else:
            treasure = "No Treasure!"

        contents = contents + ". " + treasure

    return "[Room Contents] " + contents

def getDungeonEncounter():

    subjectchart = [
    "big monster", "small monster", "harmless monster", "pitiful monster", "bold monster", "deadly monster", "dangerous monster", "guard", "helpless victim", "lost person", "adventurer", "predator", "warrior", "thief", "scout", "cleric", "mage", "scholar", "priest"
    ]

    verbchart = [
    "fighting", "engaging", "killing", "menacing", "administering to", "aiding", "fleeing", "chatting with", "talking up", "admiring", "eating", "devouring", "chasing", "egging on"
    ]

    objectchart = subjectchart + ["item"]

    result = "[Dungeon Encounter] " + random.choice(subjectchart) + " " + random.choice(verbchart) + " " + random.choice(objectchart)

    return result

def getSpecialFeature():

    qty = random.randint(1,3)

    chart = ["strange glyphs", "blacksmith tools and forge", "an old wagon", "grates in the wall along the floor", "grates up high near the ceiling", "an adventurer's discarded pack", "broken furniture", "an adventuring party", "phosphorescent lichen", "a sprung trap", "a spring", "a river or stream", "a trickle of water", "a lake or pool", "a draft from somewhere", "wine casks", "barrels", "smoke", "murals on the walls", "a dire warning", "cages", "a statue", "an unconscious person", "a person in stasis", "a petrified statue", "an altar", "glowing mushrooms", "a weapon rack", "an armor rack", "a pile of refuse", "a pile of rubble", "a fallen pillar", "a vat of liquid", "round smooth crystals embedded in the floor", "a lichen. mold, and fungi farm", "a fountain", "a pile of books", "webs", "an imprisoned demon", "footprints in the dust", "faded banners and pennants", "a throne", "a body with crude challenge on it", "scavengers feeding on a corpse", "a balcony or ledge", "a coffin", "a shattered brick arch with stone behind it", "one of the floor slabs is loose", "a faded mosaic on the floor", "a smashed mirror", "a skull", "a pedestal", "misspelled graffiti", "articulate scrawling", "a fissure a foot wide", "an iron brazier", "a row of manacles", "a weathered journal", "an iron cage suspended from the ceiling", "a grate in the floor", "shadowy alcoves", "a dark niche", "a shrine", "several shrines", "a painting face down on the floor", "a dozen extremely well-wrought statues", "a wounded creature", "broken statues", "a pristine square of floor", "a number of piles of dirty hay and refuse", "a chest", "an ornate wardrobe", "an ornate desk", "an ornate bed", "a row of cots", "signs of an animal", "a sign", "a tiled floor", "a makeshift camp", "a stockpile", "a cauldron", "a hole in the wall", "a hole in the floor", "scratch marks on wall", "very cold", "very warm", "steps down to recessed area", "a rickety bridge", "something that gleams high up on the wall", "twisted wreckage", "a hole in the ceiling", "stairs", "a ladder", "a tree", "an immediately detectable overt magical effect", "a sudden chill in the air", "a blast of heat", "a fire", "spoor", "a discarded lunch", "a blood stain", "blood spatter", "a makeshift alchemy lab", "a pile of alchemical cast-off items", "a discarded backpack", "a torn and battered satchel", "a round sphere hovering in mid-air", "a crystal ball", "cards scattered on the floor", "clothes scattered on the floor", "a tangle of armor and weapons and bones", "bones", "armor", "weapons", "a weapon", "grass", "the sun", "a will-o-wisp", "a bowl of fruit", "a basket", "an esoteric theorum", "glowing runes", "a bucket", "the scent of soft perfume", "a posed diorama", "bones sorted by type", "artfully arranged body parts", "art pieces on display", "numerous pedestals and alcoves", "a pattern of nails in the wall", "furniture", "refuse", "a nest", "a sleeping pallet", "a camp", "a person in a trap", "a person who is stuck", "a monster who is stuck", "a monster in a trap", "a wounded monster", "someone who is occupied", "the floor is wet", "the floor is slippery", "there's a narrow ledge", "a coffin; something is banging on the inside of the lid", "a golem that appears to be half-buried in the floor", "a sack", "a box", "an iron-banded chest", "a rusty metal box", "a wooden crate with the lid nailed on", "a leather satchel", "a pile of provisions", "a suit of armor", "a destroyed camp", "a make-shift shrine", "a mosaic on the ceiling", "a gallery of paintings", "a faceless statue", "a golem made of unusual materials", "a book", "a pile of scrolls", "a stack of books", "a shattered iron cage", "a handful of brass tacks", "a waterfall", "glass stairs", "a large mirror", "a painting that takes up the entire wall", "a row of jars", "a bed", "a hammock", "a tent", "the remains of a bloody conflict", "corpses strewn about", "corpses hung on hooks", "torture devices", "a bloodstained table", "a butcher block", "a pile of rusty metal",  ]

    special = random.sample(chart, qty)

    result = "[In the Room] " + ", ".join(special)

    return(result)

def getRooms(area, room_index):

    # parse out area number
    try:
        area_index = str(int(area.split(' ')[0]))
    except:
        area_index = area.split(']')[0].split('[')[1]

    exits = random.randint(0,4)
    if random.randint(0,100) < 10:
        secret = ", %s secret" % random.randint(0,exits)
    else:
        secret = ''

    exits = "[Exits] %s exits%s" % (exits, secret)

    encounter = ''
    contents = getRoomContents()
    if "Monster" in contents:
        encounter = getDungeonEncounter()

    features = getSpecialFeature()

    contents = [contents, encounter, features, exits]

    aggregate = "\n\t%s" % roomLike(area_index, room_index)
    for item in contents:
        if not item == '':
            aggregate = "%s \n\t\t%s" % (aggregate, item)

    return aggregate

# make that dungeon
dungeon = []
for i in range(0,area_count):
    area, room_count = getFullDungeonArea()
    rooms = []
    for room_index in range(1, room_count+1):
        rooms.append(getRooms(area, room_index))

    dungeon.append({})
    dungeon[i][area] = rooms

# now print or save it
print_dungeon = []
for area in dungeon:
    for key,value in area.items():
        print(key)
        print_dungeon.append("\n%s" % (key))
        for item in value:
            #print(item)
            print_dungeon.append(item)

# could save as json but let's just save for use for now
dungeon = "%s.md" % time.time()
with open(dungeon, 'w') as f:
    f.write(''.join(print_dungeon))
