---
layout: post
title: Some Pythia Screenshots
date: 2017-04-25 21:15:10
imagefolder: 2017-04-25
categories: [pythia]
tags: [pythia, logs, screenshots]
published: true
comments: true
links:
  - url: https://exposit.github.io/pythia-oracle/
    title: Pythia-Oracle
    source: katamoiran
  - url: https://exposit.github.io/katamoiran/dunscaith/
    title: Dunscaith
    source: katamoiran
  - url: https://exposit.github.io/katamoiran/noir/
    title: Noir Nights
    source: katamoiran
  - url: https://exposit.github.io/katamoiran/2016/12/14/6-hours-to-midnight-ap/
    title: 6 Hours to Midnight
    source: katamoiran
---

I thought it might be useful to put up some screenshots of Pythia with actual content. These are taken in Pythia, using the screenshot feature (triggered by being in debug mode and typing a tilde into the main text box).

All of these are using the kinda official Pythia palette *sin city*, which is black and white with splashes of red. I use *sin city*, *blackberries*, and *from hastings* the most, I think.

<!--more-->

A couple of caveats; first, these are all taken today, from game logs that are finished, so the tracker and threads will probably not be reflective of whatever section of the main panel is showing. Second, most, if not all, of these are posted on here as full APs. So probably mild spoilers ahead.

<center>
<a href="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/title_screen.png" target="new">
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/title_screen.png" alt="title screen">
</a><br>
<i>this is the only Mac screen capture</i>
</center>

This is the title screen, showing the games I've got in my saves right now. I tend to break up session logs pretty frequently, around 800 to 1000 blocks.

More than that gets unwieldy when scrolling or reviewing prior events -- it's much easier to pull up one of the automatically generated markdown or html logs if I need a recap later.

22 (23?) might seem like a lot, but I've actually retired quite a few games (Kyneros is one of them, for now) since I started.

The automatic backups make it easy to feel comfortable deleting games that aren't active -- after copying the backup to somewhere else, of course.

<center>
<a href="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/screenshot_2017-04-25-21-04-270001.png" target="new"><img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/screenshot_2017-04-25-21-04-270001.png" alt="dunscaith actor panel example"></a><br>
</center>

This is from Dunscaith, and shows an actor panel with content. The scrollable index at the lower right can be expanded or collapsed, and clicking on a name in the index jumps to that entry.

At the top you can also see tracked threads. And in the center panel is the beginning of the game -- Pythia-generated content will generally have a bracketed tag ("[tag]") to show its origin.

<center>
<a href="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/screenshot_2017-04-25-21-10-450001.png" target="new"><img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/screenshot_2017-04-25-21-10-450001.png" alt="diagram map and minimap example"></a><br>
</center>

Also from Dunscaith; this shows the diagram dungeon map on the left, with the minimap active. That's the first part of the entrance area to my megadungeon, which is entirely randomly generated in Pythia, during solo play.

The compass rose is for those of us on Mac affected by a bug in Kivy (meaning we can't scroll left and right -- two finger dragging works but is finicky).

On the right is an example of a filled tracker panel; NPC stats, bookkeeping for travel, bookkeeping for Scarlet Heroes (threat level), a note on some treasure I found, a couple of things I don't recall, and then a shorthand "cheat sheet" for running Scarlet Heroes.

Because otherwise, yes, I will be looking it up every single time I need to roll.

<center>
<a href="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/dd_Fort_Iseu.png" target="new"><img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/dd_Fort_Iseu.png" alt="map exporter example"></a><br>
</center>

This is the same map but using the map exporter (the "full map" button) to show the entire map.

Maps, like pretty much all user content in Pythia, are saved as json so the data's always retrievable and at least nominally human readable.

It would be entirely possible to scale up my rudimentary map code into a standalone program (or write one from scratch) for viewing, printing, and editing that data.

<center>
<a href="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/screenshot_2017-04-25-21-31-470001.png" target="new"><img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/screenshot_2017-04-25-21-31-470001.png" alt="standard character sheet example"></a><br>
</center>

This one has a few spoilers from Noir Nights in the "threads" box, but shows how threads keep track of stuff that's happened.

On the right, there's a "standard" style character sheet with stat boxes. You can customize how many "attribute" boxes there are; the default is about twice as many as shown. Or go with a narrative style sheet that's just alternating title/text boxes instead. Or just use the actor tracker for everyone, including the hero.

You can also reduce or increase the number of sheets displayed. I tend to use the character sheet panel sparingly, usually just my main protagonist, and everyone else goes in the actor tracker.

But I'm too lazy to toggle the number of sheets shown so I just leave it at two.

<center>
<a href="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/screenshot_2017-04-25-23-12-220001.png" target="new"><img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/screenshot_2017-04-25-23-12-220001.png" alt="the tracking panel and built-in marker"></a><br>
</center>

This is from my *6 Hours to Midnight* AP, and shows how the tracker can be used to track things like status and conditions that are toggleable in addition to jotting down notes.

I haven't yet figured out how to color the Xs based on palette so they're basically always bright red. I did try.

Hopefully this gives a good idea what Pythia look like when there's actual content!
