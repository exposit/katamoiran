---
layout: post
title: ASCII Megadungeon Generator Redux
date: 2018-11-18 22:38:07
imagefolder: 2018-11-18
categories: ['game design']
tags: ['dungeon world', 'world of dungeons', 'wodu', 'osr', 'megadungeon', 'python', 'random', 'procedural dungeon']
comments: true
published: true
extender: 'procedural dungeon'
links:
  - url: http://recedingrules.blogspot.com/2014/06/public-domain-dungeon-map-icons.html
    title: Public Domain Dungeon Map Icons
    source: Tenkar
---

I cleaned up my python projects folder, and in the process found four more random dungeon generators, one of which already outputs to ascii. So I made a few adjustments to bring it into line with the "convert to an image" script, and now I have two options when I want to generate a base map.

The big difference with this one over the one I posted a few days ago is this one picks random points instead of arranging the rooms inside a circle. Gives it a more "open" feel, though the rooms are less tightly packed in.

<!--more-->

<center>
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/1542574001.58-map.png" alt="Updated Version with Numbers " style="width: 50%; height: 50%"/><br>
<i> a numbered version with a more regular pattern</i>
</center>

It uses the same base ASCII schema as last time, more or less, though I've changed it so all uppercase letters represent numbers. To number the rooms you change a square to 0-9, then switch to A (10), B (11), C (12), and so on. This keeps the source lines the same length, which is important for adding in rooms and features.

So what do I do with it now that I've got a map? Answer -- randomly generate some dungeon content.

But not just any old random content. No, I need connected, coherent content. Content assembled in an interesting new way.

> 1 cathedral
> Concept: undead rise when you mess with their stuff
> Twist: doubled
> Feature: a pile of rusty metal

> 2 quarry
> Concept: blindness
> Twist: drugs
> Feature: a person in stasis

> 3 barracks
> Challenge: other monsters
> Concepts: undead rise when you mess with their stuff + blindness
> Twist: passage to new area
> Feature: a painting face down on the floor

This is a randomly generated riff on [this](http://www.bastionland.com/2018/10/three-step-dungeons.html). Read that, it explains it way better than I could.

To sum up, each dungeon consists of three rooms; two that introduce a concept, like petrification or mutation, with a twist or detail that makes it interesting, and one that combines both with a new twist.

In between you might have rooms with no new concepts.

> 4 catacombs
> Feature: a book
> Twist: fighting

Now, "concepts" in this case should probably mean things that the players should learn in a less dangerous context so they can then engage with them fairly in a more challenging one.

I'm broadening that out to encompass the idea of "themes" or "motifs" as well, because that's just how my brain works.

### Putting it into practice

The party has just stepped through a portal from the realms to the ruined city on the moon. Normally I would randomly generate each room as we visited it, tying it back in to the fiction as established.

The nice thing about having pre-generated content (aka "prep") is that you can tie things into the entire area, not just the last room or the next room.

The entrance room, #1, I generate as I'd normally do, grabbing a theme (City, Haunted, appropriately enough), a description (a sitting room with a map table), and a few items (a skull, a bloodstain).

While my player's fiddling with the maps and the skull I look at my dungeon elements.

> 1 cathedral
> Concept: undead rise when you mess with their stuff
> Twist: doubled
> Feature: a pile of rusty metal

When he moves west, to #18, I describe the "cathedral" -- it's a shrine, with a moon goddess statue and a headless metal golem clutching a belt kneeling in front of it.

The concept I'm supposed to be introducing here is "undead rise when you mess with their stuff". So here's the situation; you take the belt, the undead golem will go berserk. Place the skull on the golem's neck and the hands will open, allowing one to take the belt (a +1 armor device with a Jean Grey style forcefield 1/day).

Reviving the golem just takes casting a spell into him, were one so inclined. That's my "double" element; get the treasure from him, and he's treasure himself.

Onward! My player choose to explore further west, down the hall towards #17. I describe the alcove, and my hazard die suggests a local/dungeon effect, so it's time for a moonquake!

> 2 quarry
> Concept: blindness
> Twist: drugs
> Feature: a person in stasis

The next room in my sequence is a "quarry", with a person in stasis. The twist is "drugs" and the concept I'm supposed to introduce is "blindness".

Now, I could play this straight, maybe do a darkness effect, or literal blindness, but since the PC's already got some context -- he's here with an exiled prince -- I make the blindness metaphorical.

For "quarry" I interpret that as "a place where you can dig out things of value" and decide this is an emergency stasis pod chamber. Seven of them, but only two are occupied.

In one pod there's a skeleton, from the regalia likely the evil uncle who usurped the throne and blamed the prince for a massacre. In the other, they find a girl who claims to be the usurper's daughter. The blindness here is her inability to admit her father's wrongdoing.

Room 16 will combine the concepts with a new challenge.

> 3 barracks
> Challenge: other monsters
> Concepts: undead rise when you mess with their stuff + blindness
> Twist: passage to new area
> Feature: a painting face down on the floor

So our challenge is other monsters; some undead mages, I think, mindless ('blind') creatures stuck in a repetitive loop.

Earlier, down below, we found a quicksilver well that was actually a conduit between the world down below and the moon, with a monster stuck in it (trapped essentially in transit).

These guys are holding the other end of the portal shut with a ritual they perform over and over. The well's tainted; creatures that pass through it to the moon arrive as quicksilver demons, liquid nightmares that engulf and suffocate mages, trying to wear them like suits.

The "painting" is the conduit end; if it can be secured, it can be transported just like a regular painting (rolled up, folded) but used as a conduit back to the well room. Probably with a risky roll not to arrive as a puddle of malevolent liquid moonlight.

... and that's about it. I'll mix techniques for the rest of it, but I feel like this is a very satisfactory "seeding" method. And one I can use during downtime to prepare content quickly.
