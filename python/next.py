#-------------------------------------------------------------------------------------------------------------------------------------------
# --> Terrain generator
#
#    Given a seed generated by the base script, provides the next area's terrain for pointcrawling
#    For ease of use, you may enter the seed as the first command line argument
#
#-------------------------------------------------------------------------------------------------------------------------------------------

import random
import sys

try:
    seed = int(sys.argv[1])
except:
    seed = random.randint(0,8)

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

def upcomingTerrain(seed):
    
    curr_terrain = terrain[seed]
    roll = random.randint(1,100)
    
    if roll <= 10:    # 10% of the terrain
        result = curr_terrain[4]
    elif roll <= 30:  # 20% of the terrain
        result = curr_terrain[3]
    if roll <= 60:    # 30% of the terrain
        result = curr_terrain[2]
    else:             # 40% of the terrain
        result = curr_terrain[1]
    
    print("[Terrain] " + result)
    
upcomingTerrain(seed)