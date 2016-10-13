import random 
import sys

print("")
print("4d6, drop lowest:")
print("")

def roll4d6():
    global threshold
    target_met = False
    total = []
    for attr in range(0,6):
        result = []
        raw = []
        for roll in range(0,4):
            dice = random.randint(1,6)
            result.append(dice)   
            raw.append(dice) 
        result.remove(min(result))
        print(raw, result, sum(result))
        total.append(sum(result))
        if sum(result) >= int(threshold):
            target_met = True
    print("------------------")
    print("Total: " + str(sum(total)))
    return sum(total), target_met
    
try:
    
    global target_met, threshold
    
    target = 0
    count = 1
    if "-" in sys.argv[1]:
        # count
        tag, threshold = sys.argv[1].split("-")
        for i in range(int(threshold)):
        
            print("")
            print("*******************")
    
            target, target_met = roll4d6()
    
            print("4d6 Total: " + str(target) + " Total " + str(threshold) + " Sets: " + str(threshold) + " Rolls: " + str(count))
            count = count + 1
            print("")
        
    elif "+" in sys.argv[1]:
        # at least one stat matches this number
        tag, threshold = sys.argv[1].split("+")
        target_met = False
        while target_met == False:
        
            print("")
            print("*******************")
    
            target, target_met = roll4d6()
    
            print("4d6 Total: " + str(target) + " Threshold (At Least): " + str(threshold) + " Rolls: " + str(count))
            count = count + 1
            print("")
    else:
        threshold = sys.argv[1]
        while int(target) <= int(threshold):
            print("")
            print("*******************")
    
            target, result = roll4d6()
    
            print("4d6 Total: " + str(target) + " Threshold: " + str(threshold) + " Rolls: " + str(count))
            count = count + 1
            print("")
except:
    threshold = 0
    roll4d6()
    print("4d6.py +<num> for at least one stat in a set at num or above")
    print("4d6.py -<num> will roll up that many stat sets")
    print("4d6.py <num> will roll until the total of a set meets or exceeds num")