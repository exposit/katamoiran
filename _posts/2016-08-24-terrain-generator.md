---
layout: post
title: Pointcrawl Terrain Generator
imagefolder: 2016-08-24
date: 2016-08-24 12:00:00
categories: ['random content', 'scripts', 'mechanics']
tags: [mapping, random generator, script, python, terrain, solo, mechanics, kyneros]
comments: true
published: true
links:
  - url: http://hillcantons.blogspot.com/2014/11/reader-query-random-solo-wilderness.html
    title: Random Solo Wilderness Generation?
    source: Hill Cantons
  - url: http://mmmnm.blogspot.com/2014/11/random-solo-hexless-wilderness.html
    title: Random Solo (Hexless/Mapless) Wilderness Generation
    source: Mazes, Monsters, Minions, and Madness
  - url: http://www.drivethrurpg.com/product/127180/Scarlet-Heroes
    title: Scarlet Heroes
  - url: http://www.drivethrurpg.com/product/124392/d30-Sandbox-Companion
    title: d30 Sandbox Companion
  - url: https://github.com/exposit/katamoiran/tree/master/python/terrain_generator
    title: terrain generator scripts
    source: katamoiran
redirect_from: "https://exposit.github.io/katamoiran/random%20content/scripts/mechanics/2016/08/24/terrain-generator.html"
---

For the Kyneros campaign I knew I wanted to do a lot of overland exploration, wilderness and dungeon crawls, and entirely oracle-generated world-building. I've always had a love for random generation, and it's an essential part of my solo adventuring experience -- but I know my limits, and when it comes to terrain I don't have the patience (or attention span) for a literal hexcrawl.

<!--more-->

Enter a ton of reading about pointcrawls that eventually led to a very simple and fluid system based partly on [Hill Cantons'](http://hillcantons.blogspot.com/2014/11/reader-query-random-solo-wilderness.html) incredibly useful posts on the subject, and partly on an idea inspired by them at [Mazes, Monsters, Minions, and Madness](http://mmmnm.blogspot.com/2014/11/random-solo-hexless-wilderness.html). When I saw the suggested items to define in the latter post my mind immediately went to the exploration lua game I've been working on, which uses a similar step by step generation method (only utilizing real world landmarks and terrain) to map out a huge area of land. The amount of bookkeeping as written was just too much to generate on the fly; I wanted to know where my heroes were and what they were facing, but I didn't want to generate anything superfluous that I'd then have to keep track of and refer back to.

So here's the method I've hashed out that works for me.

First, pull up your favorite blank map in your favorite mapping system. Or don't; this works equally well with plain text, jotting down each area as it is encountered, maybe making a rough grid with pipes and dashes. Either way, you're basically making a diagram dungeon (see [Scarlet Heroes](http://www.drivethrurpg.com/product/127180/Scarlet-Heroes) for an excellent tutorial).

Decide on a way to generate content for each square and if you're using weather and such. For the Kyneros campaign I am using Scarlet Heroes' wilderness travel for things like encounters, features, and events, and a weighted weather generator.

Now pick a starting square; in this example, I chose the capital city of Seraxis since my party was leaving there (headed to Helase, a city about which I knew very little). Each 'square' on your map is going to represent a block of terrain, generally the amount of terrain a normal human could cross in a single *time unit* if it were flat ground. What exactly a *time unit* is is up to you and your system. I use "the distance an uninjured, average human could travel in a single day over good terrain in nice weather" or roughly 30 miles.

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/seraxis.png" alt="Seraxis" style="width: 200px; height: 200px"/><br>
<i> the blue square means nothing</i>
</center>

Step 1. Roll up a current region using base.py, making a note of the resulting seed. You can go entirely random or select a starting seed and/or settlement density. There's other good information generated, too, like what's under the region, what type and how many ruins are present (with a little wiggle room for unknown ruins), and what type and how many settlements are present.

The settlement levels use the naming scheme from the [d30 Sandbox Companion](http://www.drivethrurpg.com/product/124392/d30-Sandbox-Companion), more or less (numbers are not related; I realized there were charts for this stuff in d30 after I'd already written this and was too lazy to rewrite it from scratch -- plus it'd be overkill) and terrain types are generally matched to Scarlet Heroes. Also, you will need to interpret the results (or edit the script) -- heavy forest in a tropical climate is jungle, for example, or plains might be badlands or steppes or taiga (or lava fields or something really weird).

><b>[Settled Level] Dense [Seed] 5<br>
>[Terrain Type] hills (1), heavy forest (2), light forest (3), plains (4)<br>
>[Settlements] ['Village', 'City']<br>
>[Beneath] Caves<br>
>[Known Ruins] ['habitation', 'fortress', 'sewer']</b><br>

Step 2. [Optional] If your characters are headed somewhere in particular, use distance.py, roll a die, or use an oracle to get an idea of how many *time units* separate your starting and ending points. If it's a long journey, roll multiple times and add the results together.

>"And finally let's get the distance to Helase from here."<br>
><b>[Time Units] 4 [Road?] No</b>

Step 3. Pick, roll up, or otherwise determine which direction your characters are headed. In my game, I knew they were headed to Helase, but nothing about Helase, not even the direction it lay from Seraxis, so I rolled for it and got "southeast". So my first square to fill in is to the southeast of Seraxis.

Step 4. Move your heroes in the direction indicated. As they move into a square, use next.py with the current seed to get the terrain and modify that square's *time unit* by this terrain. For example, if we moved to the southeast, and found Heavy Forest (we did) which has a value of half speed, the square will cost two *time units* to cross it. Jot down the terrain type (you can use the seed and sub-terrain index as shorthand) in the square.

>"Seraxis is terrain seed 5, so we'll use that as our starting seed."<br>
><b>[Terrain] heavy forest (2)</b>

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/seraxis_to_helase_leg1.png" alt="Seraxis to Helase, first leg" style="width: 200px; height: 200px"/>
</center>

Step 5. Handle all of your "enter a new hex" bookkeeping as your system indicates. Roll for encounters, features, events, weather changes. Dock rations. Run a scene if something interesting occurs. Mark off any time units spent in travel. Repeat this step for any additional time units spent in this square.

Now repeat steps three to five as many times as needed. If you're using a set number of *time units*, then when you run out of the original number of *time units* you've reached your destination. This means if the innkeeper tells you something is "three days away" he'll end up being generally accurate (unless he's lying or something). When you reach your destination, if it seems appropriate, roll up a new base region using base.py.

And that's about all there is to it; the goal is to have enough info for a decently repeatable experience if your heroes come this way again, but not have a ton of information to keep track of that you likely won't need. My heroes' four day journey to Helase took about five days (bad weather, bad GM forgetting to adjust for terrain difficulty, I mean, they found an unexpected road) and the final map looked like this:

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/seraxis_to_helase.png" alt="Seraxis to Helase" style="width: 350px; height: 300px"/>
</center>

<div id="button"><a href="https://github.com/exposit/katamoiran/tree/master/python/terrain_generator" class="btn btn-info">terrain generator scripts</a></div>
