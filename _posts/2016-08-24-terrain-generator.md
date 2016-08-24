---
layout: post
title: Terrain Generator
excerpt: "Three part terrain generator for solo point crawls."
modified: 2016-08-23
tags: [mapping, random generator, script, python, terrain]
comments: true
pinned: true
published: true
---

#### [all your base scripts](https://github.com/exposit/katamoiran/tree/master/python/terrain_generator)

Yes, I went there. Ahem. So I've always had a love for random terrain generation, and it's an essential part of my solo adventuring experience. But I don't have the patience for hexcrawls or pre-generating lots of terrain. Or keeping track of exits for things like forests, or really more than "jot down general gist" and move on. After all, my heroes might travel through an area once, maybe twice if they're returning the same way, and I can always flesh things out more the second pass (if there even is one). Plus I hate getting up a good head of steam playing a scene and having to stop for more than a moment or two to jot down the next area.

Enter a ton of reading about pointcrawls that eventually led to a very simple and fluid system based partly on [this post on Hill Cantons](http://hillcantons.blogspot.com/2014/11/reader-query-random-solo-wilderness.html)
, and partly on an idea inspired by it at [this post on Mazes, Monsters, Minions, and Madness](http://mmmnm.blogspot.com/2014/11/random-solo-hexless-wilderness.html). When I saw the suggested items to define in the latter post my mind immediately flashed to the exploration lua game I've been working on, which uses a similar step by step generation method (only utilizing real world landmarks and terrain) to map out a huge area of land. However, I knew that it was just too precise and fiddly for me if I was generating it on the fly; I wanted to know where my heroes were and what they were facing, but I didn't want to generate anything superfluous to the mission at hand that I'd then have to keep track of and refer back to. So here's what works for me.

First, pull up your favorite blank map in your favorite mapping system. I suggest a diagram dungeon (see [Scarlet Heroes](http://www.drivethrurpg.com/product/127180/Scarlet-Heroes) for an excellent tutorial or google it). Decide on a way to generate content for each square and if you're using weather and such. For the *prince of stone* campaign, I am using Scarlet Heroes' wilderness travel for things like encounters, features, and events, and a weighted weather generator. Pick a starting square; in this example, I chose Seraxis since my party was leaving there and headed to Helase. (I rolled up which square Seraxis was in earlier.)

![Seraxis]({{ site.url }}/img/posted/seraxis.png =100x100)
{: .pull-right}

Step 1. Roll up a current terrain using base.py, making a note of the resulting seed. You can do entirely random or select a starting seed and/or settlement density. There's other good information there, too, like what's under the region, what types of ruins are present, and how many settlements you're likely to run into. It's all based on what feels right to me, so feel free to tailor the numbers to your tastes. Note that the settlement types are based on d30 Sandbox settlement levels and terrain types are generally matched to Scarlet Heroes, but they should be easily mappable to whatever system. Also, you will need to interpret the results (or edit the script for your world) -- heavy forest in a tropical climate is jungle, for example, or plains might be badlands or scrublands or steppes or taiga.

**__[Settled Level] Dense [Seed] 5\n[Terrain Type] hills (1) | heavy forest (2) | light forest (3) | plains (4)\n[Settlements] ['Village', 'City']\n[Beneath] Caves\n[Known Ruins] ['habitation', 'fortress', 'sewer']_**

Step 2. Use distance.py to get an idea of how many blocks separate your starting and ending squares. The number of *time units* should be interpreted as "in ideal terrain and conditions, a human could cover one *time unit* a day".

*And finally let's get the distance to Helase from here.*
**_[Time Units] 4 [Road?] No_**

Step 3. Pick, roll up, or otherwise determine which direction your characters are headed. In my game, I knew they were headed to Helase, but nothing about Helase, not even the direction it lay from Seraxis, so I rolled for it and got "southeast", so my first square to fill in is to the southeast of Seraxis.

![Seraxis to Helase, first leg]({{ site.url }}/img/posted/seraxis_to_helase_leg1.png  =100x100)
{: .pull-right}

Step 4. Move to the direction indicated. As your characters move into a square, using next.py with the current seed to get the terrain and modify *time units* by this terrain. For example, if we moved one *time unit* to the southeast, and got Heavy Forest (which we did) which has a value of -50% to speed, it'd take two time units to cross. I've built into the script a chance of a road or river, but you can interpret that as going your way or going across; it's up to you or your oracle. You might notice in the play log for this I had to oracle it; I added the road chance later.

If time is already set in the fiction, by the way -- for example, if you've determined it will take about six days to get there -- and roll up incompatible terrain ("That's the third mountain in a row, but that NPC told us it was a three day trip!"), perhaps your heroes stumble over a road or game trail, or a secret pass, or the weather is extremely favorable. Or maybe the NPC was just wrong.

*Ok, so, I've already plotted on the map the four blocks between Seraxis and Helase. Seraxis is terrain seed 5, so we'll use that as our starting seed.*
*[Terrain] heavy forest (2)", "Is there anything resembling a road?", "[very likely, 47<=85] YES*

Step 5. Handle all of your "enter a new hex" bookkeeping. Roll for encounters, features, events, weather changes. Dock rations. Run a scene if something interesting occurs. Repeat this step for any additional time units spent in this hex.

Now repeat steps three to five as many times as indicated by the original distance roll. If you know the ending terrain, check base.py for a suitable seed and fiat that the last leg of the journey is something compatible with the seed you're leaving and the seed you're entering instead of rolling.

And that's about all there is to it; the goal is to remain flexible but to have, in the end, a decently repeatable experience if your heroes come this way again. During my heroes' four time unit journey to Helase they encountered a lawman with a prisoner, a wounded bull, and ended up taking refuge from a thunderstorm in a haunted temple. It took about five days.

![Seraxis to Helase]({{ site.url }}/img/posted/seraxis_to_helase.png  =100x100)
{: .pull-right}