---
layout: post
title: ASCII Megadungeon Generator
date: 2018-11-16 15:19:37
imagefolder: 2018-11-16
categories: ['game design']
tags: ['dungeon world', 'world of dungeons', 'wodu', 'osr', 'megadungeon', 'python', 'random']
comments: true
published: true
links:
  - url: http://recedingrules.blogspot.com/2014/06/public-domain-dungeon-map-icons.html
    title: Public Domain Dungeon Map Icons
    source: Tenkar
---

I'm making a megadungeon. I've written up seven pitches and pitched them to my potential players (more on this later). All solid pitches, too, gleaned from my campaign archives.

So obviously the next step is a random dungeon generator. *Obviously.*

<!--more-->

My plan is to randomly generate a small map (the images in this post are from a decent sized one) that's mostly empty, then fill it in as the players explore and I generate random content. With the occasional section pre-built to satisfy my desire to prep.

I've experimented with doing this in a completely randomly generated fashion before, of course, notably with Dunscaith (which also forms the core of pitch #1):

> 1 The Madfans

> Classic. The base is a small fishing village at the foot of a foreboding mountain riddled with old ruins.

> An entire island to explore, of ruins and small settlements, with a single large port city that does brisk trade with the distant, decadent Empire.

> Lots of firbolgs, elves, weird fae.

But I've been running parts of Stonehell, and I really like the concreteness a prebuilt map lends the proceedings. It feels somehow fairer to say, "there's a trap here and you missed it" when the trap is already established in my notes as, in fact, being there.

Now, in new WoDu terms, that's a piece of prep, and can be used not only on a miss or when it's the GM's turn in the conversation, but also on a *local effect* roll on the Hazard die.

... but I digress. Generator time!

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/generated-ascii-source.png" alt="Generated ASCII Source" style="width: 50%; height: 50%"/><br>
<i> what the program generates as source</i>
</center>

Just text. The uppercase letters represent rooms placed at different times. Vaults -- prefab rooms -- are laid down first, then randomly generated blocks are placed on top.

There are no corridors, because I haven't yet programmed them in, and it's really not that hard to add them manually. I might later.

A second script converts it to an old school style map.

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/generated-output.png" alt="Generated Output" style="width: 50%; height: 50%" /><br>
<i> and the generated source converted to a map</i>
</center>

ASCII is trivial to edit; there's software like Rex Editor, and just opening it up in a text editor with decent highlighting is often enough.

Anything lower case a map feature and will either be converted to an icon or, if there's no special icon defined, to a printed letter.

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/edited-ascii-source.png" alt="Edited ASCII Source" style="width: 50%; height: 50%" /><br>
<i> the same source, with some features added</i>
</center>

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/edited-output.png" alt="Edited Output" style="width: 50%; height: 50%" /><br>
<i> and the edited source converted to a map using icons from Tenkar's (pd)</i>
</center>

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/numbered-output.png" alt="Generated Output" style="width: 50%; height: 50%" /><br>
<i> this is a new map; it's numbered, though you have to add them in manually</i>
</center>

And that's about it, really. I need to draw some more icons -- Tenkar's set is great but missing a few things. I purchased a CC-BY licensed set I might use, too.

I doubt this will be one to release into the wild, as it's nothing you couldn't do with any number of online generators. For me, knowing that the resulting map is entirely mine is worth the effort.
