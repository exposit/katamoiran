import random 

diceList = "4, 6, 8, 10, 12, 20, 30, 100".split(", ")

for roll in diceList:
    result = "d" + roll + ": " + str(random.randint(1,int(roll)))
    print result