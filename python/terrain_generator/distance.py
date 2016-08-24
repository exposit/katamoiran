#-------------------------------------------------------------------------------------------------------------------------------------------
# --> Terrain generator
#
#    Simple script to get the distance between two regions in time units
#
#-------------------------------------------------------------------------------------------------------------------------------------------

import random

def getDistance():      
    distance = random.randint(1,6)
    road = random.choice(["Yes", "No"])
    river = random.choice(["Yes", "No", "No"])

    print("[Time Units] " + str(distance) + " [Road?] " + road + " [River?] " + river)
    
getDistance()        
