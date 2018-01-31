#-------------------------------------------------------------------------------
#
# --> Plot Problems from Deal-a-Plot Cards
#
# I pulled the plot problems off of the 1930s "Deal-a-Plot" cards.
# Useful when you need a random event or plot twist.
#
# Note, the source is really dated. These are unedited except for spelling
# (and I dropped some joining words like "to" and "for" because I'm lazy).
#
#-------------------------------------------------------------------------------


import random

plotproblem = ["Sacrifice", "Avert Revolt", "Escape Fear", "Prevent Obtaining", "Obtain", "Avert a Horror", "Surmount an Obstacle", "Overcome Jealousy", "Recognition", "Gain Love", "Perform a Duty", "Capture an Adversary", "Overcome Mockery", "Solve a Secret", "Against Deception", "Against Oppression", "Deliverance", "Recover Lost or Stolen Person", "Revolt", "Against Adversity", "Prevent Remorse", "of Hatreds", "Competition", "Wipe Out Stigma of Dishonor", "Overcome Act of Impudence", "Overcome the Ridiculous", "Solve a Problem", "Right an Error of Judgement", "Regain One Abducted", "Recover Lost or Stolen Article", "Avert a Murder", "Avert Cruelty", "Against Treachery", "Overcome a Hatred", "Protect Honor", "Maintain Chastity", "Reverse a Judgment", "Fair Judgment", "Overcome a Horror", "Against Subjection", "Supremacy", "Defeat Jealousy", "a Loved One", "an Ideal", "Adventure", "Prevent Abduction", "Regain Sanity", "Grant an Appeal", "For Courage", "Against Fate", "Escape a Passion", "Escape an Idealist", "Against Submission", "Avert Madness", "Regain a Loss", "Avenge", "Overcome Remorse", "Avert Disaster", "Overcome a Fear", "Overcome Ridicule", "Prevent a Loss", "Attain an Ambition", "Avoid an Unpleasant Duty", "Loyalty", "Solve a Murder", "Avert Vengeance", "Overcome Passion", "Escape Cruelty", "Thwart an Ambition", "Sacrifice", "Prevent Deliverance", "Outdistance"]

print("\n\n[Plot Problem] The Struggle is " + random.choice(plotproblem))
