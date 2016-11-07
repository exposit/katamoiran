---
layout: post
title: Stat Rolling With Python
modified: 2016-10-08
categories: ['scripts']
tags: [solo, cheating, python, script]
comments: true
pinned: false
published: true
---

<div markdown="0"><a href="https://github.com/exposit/katamoiran/tree/master/python/statrollers" class="btn btn-info">stat roller scripts</a></div>

I hate rolling stats. By the time I get to stat rolling, I've usually already got the character 'in mind' that I'm creating. Maybe I rolled up an interesting hook for the backstory, maybe I've got a mechanic I want to try out, maybe there's a class that inspired me, or maybe there's just a new supplement I want to explore. And then I get a 60 point dud stat array.

I hate rolling stats. So I invariably cheat. Here's how.

<!--more-->

Usage is straightforward. Decide what your limiter is. Do you want a minimum total? Do you want at least one of a specific stat, say, one 18? Or do you just want to roll five times and pick the best yourself?

~~~
4d6.py +<num> for at least one stat in a set at num or above
4d6.py -<num> will roll up that many stat sets
4d6.py <num> will roll until the total of a set meets or exceeds num
~~~

What I generally do is roll 1d50 and add it to a base 50 to get my minimum pool. Ultimately, however, I've moved away from stats entirely -- they're just too imprecise and fiddly and ultimately define the character in ways I don't necessarily like.

But anyway, here's a couple of scripts that, to be honest, if you're at the point of using, you should probably just make the stats up yourself. Hahaha. But useful for legitimate ACKs or rolling up multiple characters at once.
