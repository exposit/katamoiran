#-------------------------------------------------------------------------------------------------------------------------------------------
# --> Terrain generator
#
#    Use this to get the overall terrain of a region.
#
#    Terrain types map to Scarlet Heroes and settlement levels match d30 Sandbox
#
#    Original inspiration here: 
#       http://hillcantons.blogspot.com/2014/11/reader-query-random-solo-wilderness.html 
#       http://mmmnm.blogspot.com/2014/11/random-solo-hexless-wilderness.html
#
#
#   seed 5 Frontier
#   seed <0 to 8> <Dense, Scattered, Frontier, Unsettled, Desolate>
#
#    Interpret each result in context of your area's climate; forest could be jungle, coast could be riverbank or lake shore, plains could be steppes.
#
#    Usage is straightforward; leave the seed empty or pick a seed based on the area you are leaving. When your character is ready to move to a new point,
#    use next.py to see what the terrain is like. When he's ready to move to a new region, use distance.py to get the number of terrain units
#    that must be crossed, generating terrain using next.py as he travels. Finally, use this script again with current seed to generate the new region and
#    new seed.
#
#
#-------------------------------------------------------------------------------------------------------------------------------------------

import random
import sys

# when moving into a new region, change these to reflect what you know about the region just exited or leave random to generate new terrain
try:
    seed = int(sys.argv[1])
except:
    seed = -9
    
try:
    settledlevel = str(sys.argv[2])
except:
    settledlevel = "Frontier"
        
terrain = [
    ["0", "coast (1)", "light forest (2)", "heavy forest (3)", "mountains (4)"],
    ["1", "coast (1)", "swamp (2)", "light forest (3)", "heavy forest (4)"],
    ["2", "heavy forest (1)", "light forest (2)", "plains (3)", "plains (4)"],
    ["3", "plains (1)", "plains (2)", "light forest (3)", "swamp (4)"],
    ["4", "plains (1)", "heavy forest", "light forest (3)", "hills (4)"],
    ["5", "hills (1)", "heavy forest (2)", "light forest (3)", "plains (4)"],
    ["6", "light forest (1)", "heavy forest (2)", "hills (3)", "mountains (4)"],
    ["7", "mountains (1)", "hills (2)", "light forest (3)", "deserts (4)"],
    ["8", "deserts (1)", "plains (2)", "hills (3)", "mountains (3)"],
]
    
def makeRegion(seed, settledlevel):

    if seed < 0:
        settledlevel = random.choice(["Dense", "Scattered", "Frontier", "Unsettled", "Desolate"])
        seed = random.randint(0,8)

    ruins = []
    if settledlevel == "Dense":
        target = 99
        count = random.randint(3,6)
        targetList = ["Town", "Town", "Village", "City", "City", "City"]
        rcount = random.randint(1,3)
        if random.randint(1,100) < 50:
            ruins.append("sewer")
        if random.randint(1,100) < 50:
            ruins.append("habitation")
    elif settledlevel == "Scattered":
        target = 90
        count = random.randint(1,5)
        targetList = ["Town", "Town", "Village", "Village", "City"]
        rcount = random.randint(1,3)
        if random.randint(1,100) < 50:
            ruins.append("fortress")
        if random.randint(1,100) < 50:
            ruins.append("habitation")
    elif settledlevel == "Frontier":
        target = 75
        count = random.randint(1,4)
        targetList = ["Town", "Town", "Town", "Village", "Village", "Village", "City"]
        rcount = random.randint(1,6)
        if random.randint(1,100) < 75:
            ruins.append("fortress")
    elif settledlevel == "Desolate":
        target = 15
        count = random.randint(1,2)
        rcount = random.randint(4,8)
        targetList = ["Town", "Village", "Village", "Village"]
    else:
        settledlevel = "Unsettled"
        target = 50
        count = random.randint(1,5)
        targetList = ["Town", "Village", "City"]
        rcount = random.randint(1,8)
        
    settlements=[]
    for i in range(count):
        if random.randint(1,100) < target:
            settlements.append(random.choice(targetList))
            if settlements[-1] == "City":
                if random.randint(1,100) > 75:
                    settlements[-1] = "Capital City"
        else:
            if settledlevel == "Dense":
                settlements.append("Decayed City")
            else:
                settlements.append("Abandoned")

    next_choice = seed
    if seed <= 8 and seed >= 0:
        next_choice = seed + random.choice([-3,-2,-1,0,1,2,3])
    
    if next_choice > 8:
        next_choice = 8 - random.randint(0,4)
    elif next_choice < 0:
        next_choice = 0 + random.randint(0,3)
        
    curr_terrain = terrain[next_choice]
    
    for i in range(rcount):
        ruins.append(random.choice(["cavern", "habitation", "fortress", "temple", "academy", "sewer"]))
    
    beneath = random.choice(["Ruins", "Caves", "Solid", "Solid", "Solid", "River"])
    
    # can use existing tools to get exits; then it's just a matter of generating distance and if there's a road or not
    print("[Settled Level] " + settledlevel + " [Seed] " + curr_terrain[0] + "\n[Terrain Types] " + curr_terrain[1] + " | " + curr_terrain[2] +  " | " + curr_terrain[3] + " | " + curr_terrain[4] + "\n[Settlements] " + str(list(settlements)) + "\n[Beneath] " + beneath + "\n[Known Ruins] " + str(list(ruins)))
        
makeRegion(seed, settledlevel)
