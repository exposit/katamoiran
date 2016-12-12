---
layout: post
title: Rolling d6s
date: 2016-12-10 12:07:22
categories: ['theory']
tags: ['trollbabe', 'stranger things', 'lady blackbird', 'narrative', 'd6s', 'probability']
comments: true
published: true
links:
  - url: http://www.onesevendesign.com/ladyblackbird/
    title: Lady Blackbird
    source: One Seven Design
  - url: http://www.lumpley.com/archive/148.html
    title: Otherkind Dice
    source: Lumpley
---

One thing I've been having a lot of trouble wrapping my brain around is the probabilities when rolling d6s and not adding them together, but looking at the face value of each. If I roll 2d6 and need a 5 or better to succeed, what are the odds I will? What if I manage to add another die? What if I need a 4 or better? What if "even" is what I want, not 4+?

<!--more-->

After confirming that 4+ is the same as "even" with someone more mathematically skilled than I am and a lot of googling that shows people are either only interested in sums or I'm missing an important keyword, I put together a simple anydice program to figure it out.

[anydice program](http://anydice.com/program/a0c8)

The number on the left is the number of dice that meet the criteria (in this case 4, 5, or 6) and the number on the right is the percent chance of that.

Numbers relevant to *Lady Blackbird* -- assuming a standard difficulty of "3", how likely am I to succeed on an "average" pool of 5 or 6? Around 50%, it looks like.

| --- | --- |
3d6 | 12.50%
4d6 | 31%
5d6 | 50%
6d6 | 66%
7d6 | 77%
8d6 | 85%
9d6 | 91%
10d6 | 94%
11d6 | 97%

Anyway, some fun stuff there, and more importantly, it caused me to reread the core rules and realize my errors -- I should have been getting back a die every time I failed, and I should have been treating Conditions as Obstacles to roll against or in the same way I handle Complications, not as an automatic worsening of the difficulty.

Now, part of the way I've been playing is adding on 2 more "optional" hits that make things more interesting for a solo gamer who doesn't have a GM to think up consequences. So the target DC is between 4 ("easy" 2 plus 2 optional) and 7 ("hard" 5 plus 2 optional).

Which I think is accounted for pretty well with high powered Tags that allow me to assemble comparatively large pools. I think I read that the expected pool for LB is 5 to 6. With my mod, the right Tags, and a Secret that lets them stack, I can pull a pool of 18 if I really, really want to (including a full reserve). But it's much more likely to be between 6 (65% chance of 3 hits, 30% of 4, 10% of 5) and 8 (85%/63%/36%) with the odd 11 (96%/88%/72%). That's with a target difficulty of 3; bumping the difficulty up by 1 to a 4 drops those odds by roughly 10% each.

So not bumping the difficulty up by one if Conditions apply will ease the odds in my hero's favor when he's low on resources but shouldn't make too much difference otherwise.

But I actually like how it plays with the slightly worsened DC. Means I should probably stop and try and deal with whatever Conditions rather than just push through! And that things get very exciting
