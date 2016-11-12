---
layout: post
title: Pythia Oracle Update 0.6.0
date: 2016-09-14T12:00:00ZUS
modified: 2016-09-14
categories: ['pythia']
tags: [pythia, python, tool, update]
comments: true
published: true
links:
  - url: https://exposit.github.io/pythia-oracle/
    title: Pythia Oracle
  - url: https://github.com/exposit/pythia-oracle/blob/master/CHANGELOG.md
    title: Pythia Oracle Changelog
  - url: http://www.drivethrurpg.com/product/127180/Scarlet-Heroes
    title: Scarlet Heroes
  - url: http://blog.trilemma.com/2015/10/the-oracles-decree.html
    title: Oracle's Decree (Trilemma)
---

Version 0.6.0 of [Pythia Oracle](https://exposit.github.io/pythia-oracle/) is up on github. This release comes with a whole bunch of new features. And bugfixes. See the [Changelog](https://github.com/exposit/pythia-oracle/blob/master/CHANGELOG.md) for a full (ish) list.

##### Highlights

First, I've cobbled up a [Scarlet Heroes](http://www.drivethrurpg.com/product/127180/Scarlet-Heroes) and *X10 Red Arrow, Black Shield* inspired diagram dungeon mapping panel. It's handled internally much the same as the oracle and generator panels are, so it gives a new place to stick user panels and also provides support for custom map panels.

Second, I've laid the foundations for scenario support in the classic style of CYOA books or solo gamebooks.

<!--more-->

At the most basic, Pythia has a lot in common with a CYOA or an old school gamebook framework. The big difference is that, instead of a static, author-written chunk of content being presented to you for you to respond to, you're expected to use the interpretive generators in Pythia (and outside it) to create that content yourself.

With this update, I've added in support for a scenario author to write up static chunks of text to present to a potential player using Pythia as the framework. Scenarios are written in blocks, and each block is shown to the player under the right circumstances (usually when a link is clicked). That's about all there is to it.

>"If you succeed, go to page 92, if you fail, go to page 18."

Pythia supports this approach painlessly with the core tools disabled, and I'd absolutely love to see some traditional gamebooks written with it! The built-in trackers and dice roller are really all that's needed. But this style is a lot of work for the author.

Core Pythia is built around asking questions and getting answers, generating content that is interpreted in the context of the adventure and your imagination, It should be possible to leverage this content in the context of a prewritten adventure to some extent -- though obviously it'd be virtually impossible to trap in a static content module for all the potential generated content:

> You are in a maze of twisty passages, all alike. Go left or right.

> \>go left

> You go left. You are in a maze of twisty passages. Go left or right.

> \>Consult Mythic, roll up a new NPC, chat with them, fall in love, get married, use their spaceship to escape.

> ...I have no idea what you're saying to me right now. Would you like to go left or right?


However, it should be very feasible to write scenarios with open-ended, guiding options in the style of old school gamebooks but taken up to 11 -- mixed with the interpretive content generation I think most solo gamers are very familiar with. Maybe even something like:

> "You encounter a new NPC; roll them up using the actor generator of your choice, and once you're done interacting with them, if they're your ally and can help you escape, click here. If they are your ally but can't help much, click here. If you're alone again, click here."

With this, the author-provided content is still interpreted in the context of the adventure, keeping the exit states in mind. And if the dragon is defeated but is referenced later, the player has to figure out how to make it work -- is it the original dragon, resurrected? A new dragon? A dragon-ish person or a metaphorical dragon? Or maybe they just switch to Edit mode and replace the word "dragon" with something else more appropriate.

Obviously the reader will still need to do a lot of interpreting and be very open about judging the results. But there's an enormous amount of flexibility here to mimic a MUD-style dungeon crawl, or a text adventure, or a gamebook, or an event-driven CYOA, or some sort of unique mad scientist hybrid thing that's not been done before (or even if it has, the more the merrier).

Anyway, I wrote up a sample tutorial dungeon using part of the one page [Oracle's Decree](http://blog.trilemma.com/2015/10/the-oracles-decree.html) (note, I did a really lackluster job, not even close to justice to the original piece). It's not worth rolling a character up for or anything but it does demonstrate the basics the system (but not very cleverly, due to my lack of imagination and a deep desire to get a working copy out).

If you can't tell, I'm very excited about the scenarios capability. I've been tinkering with interactive fiction for... ha, let's just say "a long time". My hope is to put together a scenario that's a lot more substantial and actually playable eventually.

As always, if you have any questions, comments, or suggestions, feel free to leave them here or in the github issues section of the Pythia repository!
