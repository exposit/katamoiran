---
layout: post
title: Chained Plot Generator
date: 2016-12-09 14:03:08
categories: ['soloing', 'scripts']
tags: [solo, mythic, python, tool, mod, script]
comments: true
published: true
links:
  - url: https://github.com/exposit/pythia-oracle/blob/master/HELP.md#plot--monsters
    title: Pythia HELP
    source: Pythia-Oracle
  - url: https://github.com/exposit/pythia-oracle/blob/master/resources/panels/generators/plot.py
    title: Chained Plot Python Code
    source: Pythia-Oracle
---

Just a quick post to explain how I'm using a stack of chained plots in solo play.

This is part of Pythia's plot panel (in the generator stack). Essentially, when you click "make plot" it generates a handful of interrelated, very vague plot chains.

<!--more-->

For example, a chain might look like this, with events expected to happen in order from first to last:

["a punishment (ruins) defilement", "a spy (ruins) retreat", "a hero (undergoes) the strong", "a punishment defeated", "a spy wins", "a hero (of) ruin", "a hero wins"]

It's kept secret and saved with the game. When you start a new scene, you "pop" off the next scene in the stack to use as the inspiration for that scene. So in the example, my first scene would be all about how "a punishment ruins defilement", and my next would be about "a spy ruins retreat", and so on.

This is one of those ideas I feel is very useful, has some good work in it, but it could be *so much more*. And it's the closest I've come to a markov-generated plot. But I'm not sure where to go from here -- it's the usual balancing act between evocative enough to be interesting, vague enough to be useful.

Anyway, the plots are intertwined and the "bridges" in paranthesis are optional.

You'll notice that there's a built in "end" for each plot thread -- this shouldn't be construed as mandatory; you can interpret it as "what would have happened if my hero hadn't intervened" but I tend to interpret it more as the general "feel" of that plot's ending or things that are outside my hero's control.

In the example above, "hero wins" might mean that, depending on how the dice go, it's "a pyrrhic victory" or it might mean "what he thought he wanted but loses his hearts desire". Or if the hero loses, it might mean that the way he loses somehow causes the villain to lose too. Or maybe *my* hero wins or loses on the dice and cleverness, but the aging town hero he's fighting alongside has one last victory.

And if "a spy wins" comes up -- that's a single scene in the whole adventure. Perhaps a secret spy is unveiled, just a few minutes after we finish a drugged glass of wine, or perhaps he does, in fact "win" by getting the plans to his master, and now things are much harder for us.

### Pen & Paper

If you wanted to use these as lists it should be doable. Note I haven't playtested this suggestion, it's really very much off the cuff.

Roll up your initial actor, bridge, and object, then roll a d6 whenever a new scene starts. On a 2 or less, roll up a new actor, bridge, and object, otherwise, use one of your existing actors (picked at random from your existing actors) with a new bridge and new object.

After a d6 worth of scenes, pick an actor at random and roll on "plot end" to set the tone of the scene and wrap things up for that plot in it.

#### Subject (d20)

| : --- : | : --- : |  : --- : |  : --- : | : --- : | : --- : |  : --- : |  : --- : |
1 | a hero | 2 | the enemy | 3 | an ally | 4 | common folk
5 | a fire | 6 | the strong | 7 | the weak | 8 | a castle
9 | a spy | 10 | a reward | 11 | a punishment | 12 | a bargain
13 | a promise | 14 | a secret | 15 | a disaster | 16 | a lover
17 | a danger | 18 | a monster | 19 | magic | 20 | love

#### Object (d20)

| : --- : | : --- : |  : --- : |  : --- : | : --- : | : --- : |  : --- : |  : --- : |
1 | progress | 2 | setback | 3 | destruction | 4 | creation
5 | truth | 6 | falsity | 7 | love | 8 | hate
9 | twist | 10 | awaken | 11 | a celebration | 12 | ruin
13 | defilement | 14 | retreat | 15 | murder | 16 |
17 | passion | 18 | revenge | 19 | forgiveness | 20 |

#### Ending (d12)

| : --- : | : --- : |  : --- : |  : --- : | : --- : | : --- : |  : --- : |  : --- : |
1 | triumphs | 2 | lost | 3 | fails | 4 | overcomes
5 | wins | 6 | continues unchanged | 7 | endures | 8 | flees
9 | defeated | 10 | undefeated | 11 | destroyed | 12 | reborn

#### Bridge (d12)

| : --- : | : --- : |  : --- : |  : --- : | : --- : | : --- : |  : --- : |  : --- : |
1 | causes | 2 | is | 3 | ruins | 4 | makes
5 | regards | 6 | experience | 7 | of | 8 | against
9 | undergoes | 10 | overcome | 11 | twists | 12 | to
