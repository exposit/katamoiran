---
layout: post
title: Pythia Dungeon Script
date: 2018-12-16 18:38:36
categories: ['mechanics']
tags: ['dungeon', 'random', 'python', 'pythia']
imagefolder: 2018-12-16
comments: true
published: true
links:
  - url: https://github.com/exposit/katamoiran/tree/master/python/pythia-scripts
    title: pythia scripts
    source: katamoiran
redirect_to: 'https://www.hedonic.ink/pythia-dungeon-script'
---

I pulled some of Pythia's dungeon building tools out and put them into a simple python script. The output is saved to a text file in the folder where you've got the script.

<!--more-->

You can specify how many areas in the dungeon.

```bash

$ python dungeon.py 10

```

And the output looks like this:

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/pythia-dungeon-script-screenshot.png" alt="Pythia Dungeon Script Screenshot " style="width: 75%; height: 75%"/><br>
</center>

This is more or less a direct dump from Pythia's dungeon panel, in the order I usually push the buttons. The exits line is custom for this script since I tend to either have an ascii map or use the exit generator built into Pythia, ignoring extra results.

I usually generate one area and then one room at a time, as needed, but doing them all at once at the command line keeps it persistent like it is in Pythia.

Area mechanic is inspired by Scarlet Heroes and Castle Gargantua. If you want to add more elements, most of the content is locked up in the "chart" variables.

Have fun!
