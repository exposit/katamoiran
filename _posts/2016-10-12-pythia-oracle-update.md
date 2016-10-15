---
layout: post
title: Pythia Oracle Update 1.0.0
modified: 2016-10-12
tags: [solo, pythia, python, tool]
comments: true
pinned: false
published: true
link: https://exposit.github.io/pythia-oracle/
share: true
---

Version 1.0.0 of [Pythia Oracle](https://exposit.github.io/pythia-oracle/) is up on github. This release comes with a whole bunch of new features. And bugfixes. See the [Changelog](https://github.com/exposit/pythia-oracle/blob/master/CHANGELOG.md) for a full (ish) list. (Yes, I know I haven't updated these notices between 0.6.0 and now).

##### Highlights

A ton of changes, tweaks, refinements. The changelog has it all. :) Mainly, I rolled back some changes I made to formatting (they're still there under the hood but no longer right in your face as you play). It should be much easier to hit the core format options of 'aside' (mechanics) and 'plain' (fiction). I also added a 'merge' mode so, if you're like me and tend to create lots of short blocks of the same type in a row, you can have those automatically combine down. The program tends to start getting a bit slow on my computer around ~800 blocks.

I also merged down the various main/status files so there's just one now, which should make it much easier to edit the raw files without loading them up in Pythia.

* image support -- you can now make an images subdirectory and drop image files in there, and view them in Pythia on the map stack. Pretty handy for character portraits (and maybe monsters?), or static maps.
* triggers -- want to be surprised by a perception check you-as-gm called for? or have Pythia call one for you? Triggers let you do this. Any suggestions for more stuff for the 'secrets & triggers' panel would be great. (Okay, okay, this is technically slightly post 1.0.0 but since it's working I decided just to add it to the 1.0.0 announcement.)

As always, if you have any questions, comments, or suggestions, feel free to leave them here or in the github issues section of the Pythia repository!
