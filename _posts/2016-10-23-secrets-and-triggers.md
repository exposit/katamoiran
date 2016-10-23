---
layout: post
title: Secrets and Triggers
modified: 2016-10-23
tags: [solo, pythia, python, tool, tutorial]
comments: true
published: true
---

I wanted to highlight one of my favorite parts of Pythia today! The <a href="https://github.com/exposit/pythia-oracle/blob/master/HELP.md#secrets--triggers">"Secrets & Triggers"</a> panel in the Oracle Stack.

Essentially, it's a way to inject a bit of the suspense and action that occur when a GM calls for a Perception or similar check, and to add more random events, into a GM-less game. Well, technically Pythia is kind of filling that role, but you know what I mean.

<!--more-->

There are two types of triggers - "Custom" and "Preset". Preset triggers fire randomly after a certain number of fiction blocks have been added to the main display. What this means is you start a scene, add a handful of preset triggers, and start playing.

Sooner or later, you'll get a message like this:

>*[Trigger (2DA8X2SF)] Random Event, Action*

Or this:

>*[Trigger (3Z60F3GH)] Test of Perception, difficulty, easy*

Now make the roll at the requested difficulty or press the requested generator button with the specified settings. If it's a roll, you can just ask the oracle what the roll means and if something is really there, based on the type of test and the difficulty.

>She looked down at the floor for a moment. "We're going to impose on a-- a friend," she said.<br>
>*[Trigger (3Z60F3GH)] Test of Perception, difficulty, easy*<br>
>*Hmm, interesting. Fortunately that's a good skill for him.*<br>
>*Rolling 2d8 1 times.*<br>
>*[  8 4  ] 12*<br>
>*Made it on the roll alone, since easy is a 9 in SH terms. He's good at that sort of thing, which means if the GM's calling for a check it's something outside the ordinary, but a DC9 means it wasn't that hard to notice.*<br>
>**Did he spot some sort of trap?**<br>
>**_[0: 2 ] Yes, but..._**<br>
>*He's not sure what it is at first. So magic.*<br>

In the example above, if the oracle had said "no" I likely would have asked if someone were hiding nearby. If it still said no I'd ask if it were a false alarm. You could also just ask about the false alarm up front (but in play I thought it was a good time for action so I went from the other end).

If you'd prefer a little more ambiguity or nothing immediately leaps to mind or you've failed the roll and want consequences, you can set up a custom trigger as a follow up. In the example above, I could have, instead of asking what it was or if something was there, set a custom trigger with a name of "perc, apt" or something similar and a parameter of "success".

You can also set a Custom trigger whenever it seems logical to call for a check (or it's likely something's going on the in background but your hero wouldn't have a chance to notice). For example, say your hero enters a new area where bandits are known to lurk in ambush and he made a check earlier to learn this fact. You can attempt a Perception check or not, depending on if your hero would know to do so, then set the followup trigger accordingly to see if there's anything nearby you should be worried about, assuming on a "something there" it's likely bandits lying in ambush.

The custom trigger works in a similar way to the preset triggers -- give it a name, set any parameters to sensible values, then go back to what you were doing. You'll eventually (or right away, on a success) see something like this if something is there:

> *[listen, library] There's something there!*

At this point, you have two options. If it seems logical that whatever it is will come to light or bite your hero in the ass (say, bandits are probably lurking in ambush), this is when it will, right this moment. If you succeeded, you might be advantaged, if you failed, disadvantaged. But it comes into play now.

If you can't think of how that Search check two rooms ago will help or hinder you now, ignore it as meta-knowledge; as a player, you now know there was something there, but your character doesn't. If there's nothing there, the trigger will go away silently when it expires.

You can also delete custom triggers that are no longer relevant (like the aforementioned Search check) if you really don't want to know, and delete preset ones if you want to do a rest scene or something.

In my play-testing, in an action-noir game with lots of fists and vampires and monsters, three random preset triggers per scene leads to just about the right amount of action for, well, an action-noir game with lots of fists and vampires and monsters. In a more stately modern mystery game, three in a scene about broke my poor hero (and really taxed my ability to come up with reasons to call for all those checks). So I would suggest only doing one random preset trigger per scene until you get a feel for it, and giving yourself permission to ignore triggers that don't make sense.

As always, rule of nonsense applies.

---

If anyone has any suggestions for adding more secrets and surprises into the game, please let me know, I'd love to expand the panel further!
