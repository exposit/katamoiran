---
layout: post
title: LOUCHE Javascript Test
date: 2018-12-17 16:05:55
categories: ['mechanics']
tags: ['louche', 'javascript', 'random']
comments: true
published: true
redirect_to: 'https://www.hedonic.ink/louche-javascript-test'
---

A little proof of concept javascript thing to randomly pick an element from a list and display it. In this case, a complication from my [post](https://exposit.github.io/katamoiran/2018/11/29/complication-panic/) a couple of weeks ago.

<!--more-->

<script src="{{ site.baseurl }}/js/ran.js" type="text/javascript"></script>
<script>

var chart = ['Locality.~ Something specifically related to the current environment happens. The building\'s now on fire. The ground collapses. It\'s flooding. Moonquake!','Offer.~ Offer a bargain, an extra, or a perk for a cost. Offer a better position, with risk. Offer a temptation.','Unexpected danger.~ Make something up or roll it up at random. Tie it in if you want now or worry about how it fits in later.','Callback.~ Use something they\'ve given you. A backstory element. An off-handed comment. Gear. A character sheet aspect.','Harm.~ Deal damage, pain, or misery as the fiction dictates.','End something.~ End an ongoing effect, bonus, or fictional advantage. Take a resource away, with \"resource\" used in the Trollbabe sense -- something you possess, whether it\'s a piece of gear, an ability, or an ally.']

</script>

<button id="getrandom" value="Random" onclick="randomTwoPartElement('ranelem',chart);">I need a LOUCHE complication.</button>

<p><span id="ranelem_head" style="font-size:16px;font-weight:bold;"></span></p>
<p><span id="ranelem_body" style="font-size:14px;"></span></p>

... and that's all.
