---
layout: post
title: Pythy Overview
date: 2017-07-16 10:46:29
imagefolder: 2017-07-17
categories: [pythia]
tags: [pythia, logs, screenshots, pythy]
published: true
comments: true
links:
  - url: https://exposit.github.io/pythia-oracle/
    title: Pythia-Oracle
    source: katamoiran
---

A while ago I was interested in how machine processing can help with the solo experience, so I added a panel to Pythia to handle that.

My approach is a little different than others I've seen.

<!--more-->

<center>
<a href="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/pythy-panel.png" target="new">
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/pythy-panel.png" alt="pythy panel">
</a><br>
</center>

Pythy is divided into two "sections"; Sentence Generation and Seed Generation.

If you click on a source in the sentence section, it will echo a sentence built from the source into your play log.

> Later, it seems, had quickly instituted a prodigiously far-flung body of inquires amongst nearly all the rules of matter and perspective seemed upset.

> It was, the professor carried in his dream-sculpture.

> This was that cult, and the sources scattered throughout the globe.

Any text file in a subfolder of your save game called "sources" becomes a source. I usually strip out the Project Gutenberg boilerplate but otherwise the files are as I downloaded them.

There are also a couple of built-in choices; "current play log" uses the current play log, while "recent play log only' just pulls the most recent four to seven blocks of text.

This only works if you have a substantial body of text already built up, but it can be surprisingly useful to get a "callback" to earlier work.

For example, in my paranormal detective AP (which is very, very fiction heavy), my object-reading hero passed on reading some minor items he was supposed to investigate. Later, when I wasn't sure what'd happen next, I clicked on "current play log" and got back:

> And, of course, his failure to perform his assigned trinket reading duties.

Which is similar to but not exactly the original sentence I wrote, and plenty of information to let me know that Pythia wants me to callback to that choice!

"Prediction Seeds" are intended to take the place of Mythic complex answers and to provide inspiration for what happens next. If auto-predict is on, it puts together two-word phrases from the source, based on the words you're typing into the text field.

Suggested next word just suggests a suitable next word, by looking at the last typed word and the source and determining which word should logically follow based on the frequency of the word you typed and the frequency of the words that usually follow it in the source.

So I type this:

> This is an auto predict based on this sentence. What I tend to do is write a sentence, then glance over at the prediction seeds for input.

And Pythy shows this:

<center>
<a href="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/seed.png" target="new">
<img src="{{ site.baseurl }}/img/posts/{{page.imagefolder}}/seed.png" alt="seed">
</a><br>
</center>

In this case, I'd probably use "voodoo meeting"!

It's not perfect. For one thing, you do have to manually push a button (or look over to the left) when you want more input. And it sometimes returns truly dazzling chunks of text.

> That was the document I read, and now the detective had come down from the stars came right again, and what was known of the manuscript records daily calls of the precise words of the dream-place he saw the city would rise again when I did not forget the mixed blood and marine pursuits of the men was of a 15 glimpse of forbidden eons which chills me when I did not forget the mixed blood and marine pursuits of the results of a daemon galleon.

But I think it's a valuable tool in the soloing arsenal.

Pythy is part of Pythia by default; if you've installed or updated to the latest version you have it. To activate it, you need to open a terminal and install markovify, textblob, and the nltk sources.

```SHELL
pip install markovify

pip install -U textblob

python -m textblob.download_corpora lite
```

It's all in the readme in the Pythia repo.
