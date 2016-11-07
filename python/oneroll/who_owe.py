import random

# not fancy; just goes down the list and prints each choice, handling the exceptions in a minimal way

roll = []

print("\nYou owe the money to...")
roll.append(random.randint(0,11))
print(["1. a sibling or close relative", "2. a noble", "3. a government body", "4. a church", "5. a gangster", "6. an outcast or monster", "7. a warlord or barbarian", "8. a wizard", "9. a thief", "10. a merchant", "11. a spymaster", "12. a courtesan"][roll[-1]])

print("\nYou owe the money because...")
roll.append(random.randint(0,8))
print(["1. of gambling", "2. of an expensive vice", "3. of someone else", "4. of a joke or prank gone wrong", "5. they trusted you and you messed up", "6. you trusted a pretty face", "7. you stole it and they know", "8. it wasn't your fault but they hold you accountable anyway"][roll[-1]])

print("\nIf you don't pay up they'll...")
roll.append(random.randint(0,5))
print(["1. take it out of your hide (possibly not fatal but you like both of your arms)", "2. make an example out of you (fatal and messy)", "3. have a legal claim to something you value", "4. take everything, including your person", "5. send a really skilled assassin out looking for you", "6. hurt people you care about"][roll[-1]])

print("\nYou have...")
roll.append(random.randint(0,3))
print(["1. until they notice you're not dead yet", "2. until you want to go back to your home town", "3. as long as you can keep dealing with the hired thugs they keep sending", "4. a bargain buying you time but you'd better deliver"][roll[-1]])

print("\nYou know that one path to freedom is to...")
roll.append(random.randint(0,9))
print(["1. retrieve something the one you owe values higher than the debt", "2. confront the one you owe directly", "3. pay it back in full", "4. convince someone to sacrifice for you", "5. flee far enough that they can't reach you", "6. find a powerful patron", "7. find a powerful item of protection", "8. turn the tables on them, but you're going to need allies", "9. lay low, attracting no attention, for a long, long time", "10. become someone else"][roll[-1]])

print("\nFinally, there's a wrinkle.")
chart = ["1. Everybody you used to know knows you're toxic now.", "2. There's a price out on your head and even if you satisfy the debt it'll take time for word to get out.", "3. The law is looking for you but it's a total frame job.", "4. The law is looking for you, and you can totally explain...", "5. You did something terrible that you never thought you were capable of to escape.", "6. Someone you cared about betrayed you to them but you escaped.", "7. They actually killed you, or near enough, and think you're (still) dead.", "8. One of your former lovers or allies is working for them and they know you *very* well.", "9. They have a lackey who isn't directly dangerous, but follows you from place to place making sure everyone knows you owe.", "10. An ancestral spirit only you can see is attached to you. It's disappointed with you and finds everything about you depressing and repugnant and tells you what a failure you are whenever it thinks of it, which is all the time.", "11. You're cursed and slowly wasting away. Only collecting towards repayment of your debt eases the symptoms.", "12. You're cursed; at night your Shadow possesses your body and makes it do things you'd never do normally.", "13. The debt has a component you can't repay with money, only with blood -- or perhaps not at all.", "14. The person you owe money to will forgive the debt if you do something for them that is a. horrifying, b. extremely dangerous, c. illegal. Choose two.", "15. An innocent paid a terrible price when you incurred the debt and their family will do something about it. Roll again on the d6 chart and on the d4 chart to see what.", "16. Someone who didn't deserve it was ruined or suffered terribly because of your actions or lack of action.", "17. You're wracked with terrible nightmares about the money and you don't know why.", "18. You've been framed for the most heinous crime you can think of -- not just larceny or petty theft. The person you owe is just that vindictive.", "19. Roll until you have two results and combine them.", "20. You actually owe money to 1+1d4 different groups. Roll a d4, then roll up that many more groups."]
roll.append(random.randint(0,19))
wrinkle = chart[roll[-1]]

if "19" in wrinkle:
    chart = chart[:-2]
    wrinkle = " AND ".join(random.sample(chart,2))

print(wrinkle)

print("\nThe amount you owe is %s" % (max(roll) * 1000))

print("\nYou owe something more difficult to repay than mere money. You owe...")
s = min(roll)
roll.remove(s)
ss = min(item for item in roll if item >= s)
total = s + ss
print(["2. A favor.", "3. A life. Yours, perhaps, or maybe a sacrificial victim's. Or a fellow debtor you could turn in...", "4. A rare spell component that's going to be hell to replace.", "5. A rare antique in a specific style.", "6. A rare animal. Don't even ask.", "7. A magic effect or power that you usurped from the expected owner. You can do something extraordinary now but have no control over it. And they're mad they lost out.", "8. An inconvenient magical animal that has imprinted on you instead of the intended owner (or died in your care if you don't want a pet).", "9. Your skin. Part of a powerful ritual is inked indelibly on your skin. You're the last copy.", "10. A powerful magical item, now bonded to you. Not necessarily a useful item, just a powerful one."][total])
