---
layout: post
title: Markov Name Generator
date: 2016-10-22T12:01:00ZUS
modified: 2016-10-22
categories: ['scripts']
tags: [tool, python, script]
comments: true
published: true
links:
  - url: https://www.samcodes.co.uk/project/markov-namegen/
    title: Procedural Name Generator
  - url: https://github.com/exposit/katamoiran/tree/master/python/markov
    title: Markov Name Generator script
    source: katamoiran
---

Similar in spirit to this [Procedural Name Generator](https://www.samcodes.co.uk/project/markov-namegen/) except much less sophisticated, far fewer data files, and, overall, much much less awesome. But the ability to run it locally is important to me and I didn't feel like reinstalling haxe or figuring it out. Now I will probably go reinstall haxe.

<!--more-->

The script is just a wrapper for an existing markov script name generator I found in the public domain (details in the markov.py file). The lists are from wikipedia and various baby name sites and such.

You can add more files in as many sub directories as you'd like. There's a rudimentary interface and you can also control things via command line. Try the default script with 'python markov.py' first to get a list of all valid files and their numbers.

```
-f <letters> to use those as the first letters of all generated names
-n <number> to make that many names (default 10)
-l to limit names to a maximum length (default is equal to the longest source word)
-m <number> will set a minimum name length (default is 3)
-d <n[,n,n]> to specify datafiles and skip input prompt
-k <word or phrase> will only grab files containing that word in the name. Note that 'male' would normally match 'female' or 'male' but I've given it a special clause.
```

You're likely better off using the linked generator if you don't need "local" and "add permanent source files".

<div id="button"><a href="https://github.com/exposit/katamoiran/tree/master/python/markov" class="btn btn-info">markov name scripts</a></div>
