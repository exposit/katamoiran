---
layout: post
title: Minor Python Tools
date: 2018-01-31 15:55:35
categories: ['mechanics']
tags: ['diedrop', 'random', 'deal-a-plot', 'complications', 'problems']
comments: true
published: true
links:
  - url: https://github.com/exposit/katamoiran/tree/master/python
    title: python scripts
    source: katamoiran
  - url: http://www.storyforgecards.com/DealAPlot.pdf
    title: Deal-a-Plot Cards
    source: Story Forge Cards
---

I dusted off a couple of scripts and pushed them to the repo. The first is a diedrop generator, for those times when you really need to drop a bunch of dice on a flat surface but can't do it physically. The second set creates plot problem and complications based on the (very dated) 1930s [deal-a-plot cards](http://www.storyforgecards.com/DealAPlot.pdf) found here.

<!--more-->

The die drop script takes number and faces of dice as arguments, rolls them -- you could use it as a die roller if you wanted pictures of all your rolls, I suppose, but it'd be really inefficient -- and scatters them around the virtual table.

```bash

$ python diedrop.py --d10 3 --d6 10

```

And the output looks like this:

<img src='https://raw.githubusercontent.com/exposit/katamoiran/master/python/diedrop/output/image_01.png'>

And the deal-a-plot cards:

```bash

$ python complication.py

How many complications?  2

...2 complications:

Complications: Trade, Repair

```

```bash

$ python plot.py

[Plot Problem] The Struggle is Protect Honor

```

The deal-a-plot cards actually have a ton more information that just plots and complications -- settings, people, jobs, emotions, just a ton of lists. I ran out of steam on them!
