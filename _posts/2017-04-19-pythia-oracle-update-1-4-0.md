---
layout: post
title: Pythia Oracle Update 1.4.0
date: 2017-04-19 14:01:27
categories: ['pythia']
tags: [solo, pythia, python, tool, update]
comments: true
published: true
pinned: true
links:
  - url: https://exposit.github.io/pythia-oracle/
    title: Pythia Oracle
  - url: https://github.com/exposit/pythia-oracle/blob/master/CHANGELOG.md
    title: Pythia Changelog v. 1.4.0
  - url: https://github.com/josdejong/jsoneditor
    title: json editor
---

Version 1.4.0 of [Pythia Oracle](https://exposit.github.io/pythia-oracle/) is finally finalized. Ha. No changes from the last commit except to update the various tags and markers to the current version number -- make it official, so to speak.

As always, see the [Changelog](https://github.com/exposit/pythia-oracle/blob/master/CHANGELOG.md) for a full (ish) list of changes from the last version.

This will probably be the "stable" version for the foreseeable future, as I've simply run out of things I want to add or change!

<!--more-->

NOTE: If you need to edit your Pythia save files, please consider using a json editor like [this one](https://github.com/josdejong/jsoneditor) instead of editing the files manually. There's an online version, or you can download the release, unzip, and open example #4 in the examples directory in a modern browser to use it locally.

This is much safer and more effective than mucking around with the raw json and much less likely to ruin your game because of a missed comma.

##### Highlights

* I moved some stuff in the footer around. Now you can "pick one" through "pick five" which is handy for narrowing down lists.

* New character sheet mode to support narratively described characters. Pretty much just alternating big and small boxes. See the config and help for details.

* Re-arranged the generators and split them up in a more logical way, with Dungeon having its own panel now. Added some zone-based pointcrawl stuff.

* Added a new panel (disabled by default) that has predictive text and markov chain generators to mimic a GM. It's extremely alpha and requires more libraries (Textblob and markovify) to be installed than usual.

As always, if you have any questions, comments, issues, or suggestions, feel free to leave them here or in the github issues section of the Pythia repository!
