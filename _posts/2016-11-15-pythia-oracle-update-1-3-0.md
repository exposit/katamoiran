---
layout: post
title: Pythia Oracle Update 1.3.0
date: 2016-11-15 17:45:00

categories: ['pythia']
tags: [solo, pythia, python, tool, update]
comments: true
published: true
pinned: false
links:
  - url: https://exposit.github.io/pythia-oracle/
    title: Pythia Oracle
  - url: https://github.com/exposit/pythia-oracle/blob/master/CHANGELOG.md
    title: Pythia Changelog v. 1.3.0
  - url: https://github.com/josdejong/jsoneditor
    title: json editor
---

Version 1.3.0 of [Pythia Oracle](https://exposit.github.io/pythia-oracle/) is up on github. Not too many new features, but some major tweaks under the hood. I rewrote the core display routine, ripped out the concept of "modes" entirely, and made a bunch of convenience tweaks.

As always, see the [Changelog](https://github.com/exposit/pythia-oracle/blob/master/CHANGELOG.md) for a full (ish) list.

<!--more-->

NOTE: If you need to edit your Pythia save files, please consider using a json editor like [this one](https://github.com/josdejong/jsoneditor) instead of editing the files manually. There's an online version, or you can download the release, unzip, and open example #4 in the examples directory in a modern browser to use it locally.

This is much safer and more effective than mucking around with the raw json and much less likely to ruin your game because of a missed comma.

##### Highlights

* Instead of modes, we've moved entirely to tagging blocks with their function and letting the formatting flow from that. You can use markdown inside your blocks as well. To edit a block, just click on it. This makes things much quicker to load and more efficient to edit, because you just change the block you want to change, not all of them.

* You can now use keywords in the main text input to trigger Pythia to respond to the entered text. Entering a dice notation string first or using the keyword "roll" will trigger a dice roll (or multiple dice rolls if you have more than one dice string in your text input). "??" will return an oracle result. And starting or ending your block of text with either "-p" or "-a" will set the format for that block to plain or aside, respectively. So if you're doing a big stretch of asides, and are in "aside" mode, you can easily insert a plain block without needing the mouse.

* I've updated all the logforms, turning off most of them, and adding one prepped for turning your logs into a pdf with pandoc. It's a little obsessive but I'm *almost* happy with them.

* Upgrading should be very easy now; Pythia will (hopefully) insert any missing variables into your config instead of requiring you to make a new one.

I've updated the documentation yet again, as well.

As always, if you have any questions, comments, or suggestions, feel free to leave them here or in the github issues section of the Pythia repository!
