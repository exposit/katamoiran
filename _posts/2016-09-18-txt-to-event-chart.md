---
layout: post
title: Creating Mythic-Style Charts From a Text File
modified: 2016-09-18
tags: [solo, mythic, python, tool, diy]
excerpt: Inspired by the slew of Mythic and similar style charts on the google+ community over the last few days, I wrote a simple script that takes a text file, sorts it by word type, and outputs each type as a separate, numbered chart.
comments: true
pinned: false
published: true
---

<div markdown="0"><a href="https://github.com/exposit/katamoiran/tree/master/python/seedparser" class="btn btn-info">text to event chart converter scripts</a></div>

Inspired by the slew of Mythic-style charts on the google+ community over the last few days, I wrote a simple script that uses nltk and python to take a text file, sort it by word type, and output each type as a separate, numbered chart.

It's not perfect; the resulting chart needs quite a bit of curation, but it's a lot easier than doing it manually!

<!--more-->

Installing nltk is pretty straightforward. Open a terminal and type:

~~~
 pip install -U nltk
 python
 import nltk
 nltk.download('wordnet')
~~~

Detailed instructions are [here](http://www.nltk.org/data.html).

Extremely brief research (I looked at the pdfs for a couple of seconds) and foggy grammar skills suggest that the Mythic pattern is "verb (or adjective) noun". Location Crafter uses "verb noun" for actions and "adverb adjective" for descriptions. Verbs tend to be in the concrete, present tense ("coerce", "demand", "mend"). Subjects can be any noun. Adverbs tend to end in "ly" but you'll probably need to convert some of the verbs manually to make up more than 50 or so suitable ones. And 100 elements seems pretty standard.

Word files can be weighted lists (run through, say, wordclouds.com) or raw text, doesn't really matter as long as it is plain text, though older files or ones with a lot of underscores and odd formatting might choke the script. Very long files (over ~165K words) take a while though.

Run the script in the same directory as your word file; it will output a .csv file and a .py file for each of the four required parts of speech (noun, adjective, adverb, verb). The .py is in python dictionary/list format and the csv has a comma-separated, numbered chart that should be straightforward to import into Google spreadsheets or a similar program.

For standard 100 element lists:

~~~
python seedparser.py <filename>
~~~

Flags:

* -x, --max	number
*    The max number of elements in each final list or chart. Should be 10% to 25% higher than your intended final total to give you spares to replace miscategorized or boring words. Default is 110.
* -f, --fill	True or False
*    Keep trying until the list is at the max number or a maximum number of tries is exceeded. Default is True.
* -c, --case	u[pper], l[ower]
*    Set the initial letter of each element of each list to uppercase or lowercase. Defaults to lowercase.
* -m, --min	number
*     Minimum length of words to include; default is 4, to eliminate things like "get", "got", "put", "say". If you lower this, increase the max elements substantially to compensate for the useless entries.
* -l, --lemmatize	True or False
*     Convert verbs to base form, ie, "asked" to "ask". Default is true.
* -p, --proper	True or False
*   Include proper nouns or not. Default is false.
* -p, --print	True or False
*    Print results to terminal. This makes it easy to copy and paste without having to open up the saved file. Default is False.

If you don't want to mess with this stuff, just do:

~~~
python seedparser.py <filename>
~~~

Finally, edit the resulting lists down, replacing any unsuitable words. You can import the csv into Google Spreadsheets (and likely other spreadsheet programs) as is or use the python code for further processing.

You can also just use the included seed.py to generate seeds immediately, if you'd like.

~~~
python seed.py <filename> -a verb -b noun
~~~

You can optionally specify an "-a" and a "-b" for which if the four parts of speech you want to grab. If they aren't specified they default to "verb" and "noun" for a Mythic-style result.

And there you go. A very simple, probably way more work to write than it would have been to just make a damn list by hand, unitasker script for turning texts into event lists.
