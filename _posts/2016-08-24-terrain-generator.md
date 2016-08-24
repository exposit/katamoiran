---
layout: post
title: Terrain Generator
excerpt: "Three part terrain generator for solo point crawls."
imagefolder: 2016-08-24
modified: 2016-08-23
tags: [mapping, random generator, script, python, terrain]
comments: true
pinned: true
published: true
---

<div markdown="0"><a href="https://github.com/exposit/katamoiran/tree/master/python/terrain_generator" class="btn btn-info">terrain generator scripts</a></div>

For the Kyneros campaign I knew I wanted to do a lot of overland exploration, wilderness and dungeon crawls, and entirely oracle-generated world-building. I've always had a love for random generation, and it's an essential part of my solo adventuring experience -- but I know my limits, and when it comes to terrain I don't have the patience (or attention span) for a literal hexcrawl.

Enter a ton of reading about pointcrawls that eventually led to a very simple and fluid system based partly on [Hill Cantons'](http://hillcantons.blogspot.com/2014/11/reader-query-random-solo-wilderness.html) incredibly useful posts on the subject, and partly on an idea inspired by them at [Mazes, Monsters, Minions, and Madness](http://mmmnm.blogspot.com/2014/11/random-solo-hexless-wilderness.html). When I saw the suggested items to define in the latter post my mind immediately went to the exploration lua game I've been working on, which uses a similar step by step generation method (only utilizing real world landmarks and terrain) to map out a huge area of land. The amount of bookkeeping as written was just too much to generate on the fly; I wanted to know where my heroes were and what they were facing, but I didn't want to generate anything superfluous that I'd then have to keep track of and refer back to. So here's what I've hashed out that works for me.

First, pull up your favorite blank map in your favorite mapping system. I suggest a diagram dungeon (see [Scarlet Heroes](http://www.drivethrurpg.com/product/127180/Scarlet-Heroes) for an excellent tutorial or google it). Decide on a way to generate content for each square and if you're using weather and such. For the Kyneros campaign I am using Scarlet Heroes' wilderness travel for things like encounters, features, and events, and a weighted weather generator. Pick a starting square; in this example, I chose the capital city of Seraxis since my party was leaving there (headed to Helase, a city about which I knew very little).

Note, bolded text is taken from my play log; bold and italicized text denotes random results.

<center>
<img src="{{ site.url }}/img/posts/{{page.imagefolder}}/seraxis.png" alt="Seraxis" style="width: 200px; height: 200px"/><br>
<i> the blue square means nothing</i>
</center>

Step 1. Roll up a current terrain using base.py, making a note of the resulting seed. You can go entirely random or select a starting seed and/or settlement density. There's other good information there, too, like what's under the region, what type and how many ruins are present, and what type and how many settlements are present. The random parts are based on what feels right to me, so you should tailor the numbers to your tastes. 

Note that the settlement levels are based on d30 Sandbox settlement levels and terrain types are generally matched to Scarlet Heroes, but they should be easily mappable to whatever system. Also, you will need to interpret the results (or edit the script for your world) -- heavy forest in a tropical climate is jungle, for example, or plains might be badlands or scrublands or steppes or taiga.

<center>
<b><i>[Settled Level] Dense [Seed] 5</i></b><br>
<b><i>[Terrain Type] hills (1), heavy forest (2), light forest (3), plains (4)</i></b><br>
<b><i>[Settlements] ['Village', 'City']</i></b><br>
<b><i>[Beneath] Caves</i></b><br>
<b><i>[Known Ruins] ['habitation', 'fortress', 'sewer']</i></b>
</center>
    
Step 2. [Optional] If your characters are headed somewhere in particular, use distance.py, roll a die, or use an oracle to get an idea of how many *time units* separate your starting and ending squares. The number of *time units* should be interpreted as "in ideal terrain and conditions, a human could cover one *time unit* a day". Roll multiple times if necessary.

<center>
<b>And finally let's get the distance to Helase from here.</b><br>
<b><i>[Time Units] 4 [Road?] No</i></b>
</center>

Step 3. Pick, roll up, or otherwise determine which direction your characters are headed. In my game, I knew they were headed to Helase, but nothing about Helase, not even the direction it lay from Seraxis, so I rolled for it and got "southeast", so my first square to fill in is to the southeast of Seraxis.

Step 4. Move the direction indicated. As your characters move into a square, use next.py with the current seed to get the terrain and modify *time units* by this terrain. For example, if we moved one *time unit* to the southeast, and got Heavy Forest (which we did) which has a value of half speed, it'll take two time units to cross.

If time is already set in the fiction -- for example, if you've determined through roleplay that it will take about six days to get there -- and roll up incompatible terrain ("That's the third mountain in a row, but that NPC told us it was a three day trip!"), perhaps your heroes stumble over a road or game trail, or a secret pass, or the weather is extremely favorable. Or maybe the intel was just wrong.

<center>
<b>Ok, so, I've already plotted on the map the four blocks between Seraxis and Helase. Seraxis is terrain seed 5, so we'll use that as our starting seed.</b><br>
<b><i>[Terrain] heavy forest (2)</i></b><br>

<img src="{{ site.url }}/img/posts/{{page.imagefolder}}/seraxis_to_helase_leg1.png" alt="Seraxis to Helase, first leg" style="width: 200px; height: 200px"/>
</center>

Step 5. Handle all of your "enter a new hex" bookkeeping. Roll for encounters, features, events, weather changes. Dock rations. Run a scene if something interesting occurs. Repeat this step for any additional time units spent in this hex.

Now repeat steps three to five as many times as indicated by the original distance roll. If you know the ending terrain, you can check base.py for a suitable seed and fiat that the last leg of the journey is something compatible with the seed you're leaving and the seed you're entering instead of rolling. I don't bother.

And that's about all there is to it; the goal is to leave lots of options but to have enough info for a decently repeatable experience if your heroes come this way again. My heroes' four time unit journey to Helase took about five days (bad weather, bad GM forgetting to adjust for terrain difficulty, I mean, they found an unexpected road) and the final map looked like this:

<center>
<img src="{{ site.url }}/img/posts/{{page.imagefolder}}/seraxis_to_helase.png" alt="Seraxis to Helase" style="width: 200px; height: 200px"/>
</center>