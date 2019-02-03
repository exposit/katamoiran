---
layout: post
title: What's About to Happen?
date: 2019-02-03 11:46:02
categories: ['mechanics']
tags: ['table', 'javascript', 'random']
comments: true
published: true
---

More fun with javascript. This one is a 100 element list of random things that can just happen while delving, exploring, or having a cup of tea.

<!--more-->

<script src="{{ site.baseurl }}/js/ran.js" type="text/javascript"></script>
<script>

var chart = ["someone with a devastating secret arrives", "an unexpected fall reveals a secret", "someone reveals a deep-seated desire", "guards burst in, chasing someone", "the subject of a medical experiment, broken", "an unexpected darkness falls", "someone reveals an ulterior motive", "something you're carrying reveals a new facet or use", "someone picks a fight", "a sudden flood", "someone reveals an unsavory heritage", "a misplaced item appears in an odd place", "the ground collapses", "the sword talks to you, offers you a deal", "the shadows are literally crawling", "a beloved thing is broken", "someone reveals a passionate, deep feeling", "a strange symptom is cause to worry", "a curse takes effect; you are different mentally now", "you can't smell", "someone reveals a lack or need", "a curse takes effect; you are different physically now", "an old enemy strolls in, with an offer", "a shriek of alarm goes up outside", "an abrupt message tells you someone is in danger", "the soft rustle of wings", "that's not their kid", "you've lost something you were carrying, but when?", "you develop an odd cough", "guards burst in, looking for you", "you feel very hungry", "that is absolutely their kid", "they were lying", "the howl of a hunting pack, in the distance", "the door is open; wasn't it closed before?", "something you're carrying is blemished", "someone isn't who you thought they were", "someone reveals an act that shaped them", "there's a low rumble", "a curse takes effect; you are different emotionally now", "someone strongly disagrees with this course of action", "a cry for help from an old rival", "reveal: a parent was something weird and reviled", "a medical condition makes reconciliation imperative", "an unexpected fall breaks something", "a mishap with an experiment", "a strength is immediately useful", "you feel itchy", "reveal: you are not the Chosen one", "a mysterious stranger arrives to tell you a secret", "an old friend asks for a private walk", "you're tired", "a sudden sting as something bites you", "a scream, cut off, from the shadows", "you can't hear", "someone collapses, pale and weak", "message scrawled in graffiti", "the worst possible outcome", "an old lover re-appears", "an inconvenient phobia", "someone reveals a weakness", "a weakness revealed at a bad time", "you don't feel well", "someone reveals a secret you wish they hadn't", "reveal: you are the Chosen one", "an earthquake", "sudden return of a forgotten memory", "someone who has given up arrives", "you're tipsy; check for fumes", "there's laughter somewhere nearby", "someone reveals a betrayal and offers a deal", "someone drops a bombshell", "a curse takes effect; you begin a slow slide", "a ghost haunts you; you can see them now", "a creature is enchanted and asks for help", "someone who never gives up arrives", "an abrupt message warns of imminent danger", "a sudden threat, from ambush", "there's a draft in here", "you're lost", "someone reveals a connection to the enemy", "you can't see", "the nearest plant starts to glow", "you're so thirsty", "rocks fall, everyone is in danger", "reveal: a parent was something weird and admired", "someone looking for a lost person arrives", "an inconvenient truth becomes apparent", "it's suddenly hotter", "something you're wearing is chafing a joint", "a perfectly reasonable phobia, given the circumstances", "someone who never grew up arrives", "you can manifest a specific thing, if you really try", "someone is weeping over a corpse", "someone reveals a selfless motive", "brown static, glimpsed out of the corner of your eye", "the phone rings; wrong number", "a pit opens under your feet", "it's suddenly colder", "the brightest light in the area goes out"]

</script>

<button id="getrandomelement" value="Random" onclick="randomPrefixElement('ranelem',chart);">I need to know!</button>

<p><span id="ranelem" style="font-size:16px;font-weight:bold;"></span></p>
