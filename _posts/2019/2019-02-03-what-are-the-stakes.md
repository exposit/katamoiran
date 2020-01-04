---
layout: post
title: What Are the Stakes?
date: 2019-02-03 12:04:53
categories: ['mechanics']
tags: ['table', 'javascript', 'random']
comments: true
published: false
---

More fun with javascript. This one is a simple stakes generator, to tell you what's at risk in a conflict.

<!--more-->

<script src="{{ site.baseurl }}/js/ran.js" type="text/javascript"></script>
<script>

var a = ['my heart', 'my soul', 'my body', 'my self-esteem', 'my resource', 'my ally']
var b = ['divided', 'stolen', 'attacked', 'conflicted', 'compromised', 'damaged']
var c = ['by', 'by', 'by', 'with', 'for', 'from']
var d = ['creature', 'curse', 'rival', 'love', 'chaos', 'order']

</script>

<button id="getrandomstakes" value="Random" onclick="randomMultiElement('stakes',a,b,c,d);">What are the stakes?</button>

<p><span id="stakes" style="font-size:16px;font-weight:bold;"></span></p>
