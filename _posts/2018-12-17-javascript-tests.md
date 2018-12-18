---
layout: post
title: Javascript Test
date: 2018-12-17 16:05:55
categories: ['mechanics']
tags: ['motifs', 'threads']
comments: true
published: true
---

<script>
var randomElement = function(){
  debugger;

  var base = new Array('ranelem','and','so','if','or','but','then');

  var his = Array.apply(null, Array(3)).map(String.prototype.valueOf,"hi");

  var final = base.concat(his);

  final.sample();

};

Array.prototype.sample = function(){
    var elem = this.shift()
    document.getElementById(elem).innerText = this[Math.floor(Math.random()*this.length)];
};

</script>

<button id="getrandom" value="Random" onclick="randomElement();">Random Element</button>
<p id="ranelem" ></p>

This is a test post. Ignore it!
