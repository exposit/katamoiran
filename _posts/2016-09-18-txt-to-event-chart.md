---
layout: post
title: Creating Mythic-Style Charts
date: 2016-09-18T12:00:00ZUS
modified: 2016-11-06
categories: ['soloing', 'scripts']
tags: [solo, mythic, python, tool, mod, script]
comments: true
published: true
links:
  - url: https://plus.google.com/u/0/communities/116965157741523529510
    title: Lone Wolf Roleplaying google+ community
  - url: http://textblob.readthedocs.io/en/dev/index.html
    title: TextBlob
  - url: http://www.wordclouds.com/
    title: Wordclouds.com
  - url: https://donatstudios.com/CsvToMarkdownTable
    title: csv to markdown table converter (Donat Studios)
  - url: https://github.com/exposit/katamoiran/tree/master/python/seedparser
    title: Mythic-style Seed Charts (katamoiran)
---

Inspired by the great Mythic-style charts on the [Lone Wolf Roleplaying google+ community](https://plus.google.com/u/0/communities/116965157741523529510) over the last few days, I wrote a simple script that uses <strike>nltk</strike> [TextBlob](http://textblob.readthedocs.io/en/dev/index.html) and python to take a text file, sort it by word type, and output each type as a separate, numbered chart.

It's not perfect; the resulting chart needs quite a bit of curation, but it's a lot easier than doing it manually!

<!--more-->

#### The Goal

Extremely brief research (I looked at the pdfs for a couple of seconds) and foggy grammar skills suggest that the Mythic pattern is "verb (or adjective) noun". Location Crafter (as near as I can tell) uses "verb noun" for actions and "adverb adjective" for descriptions.

Verbs tend to be in the concrete, present tense ("coerce", "demand", "mend"). Subjects can be any noun. Adverbs tend to end in "ly" but you'll probably need to convert some of the verbs manually to make up more than 50 or so suitable ones. And 100 elements seems pretty standard per list.

#### Using Seed Parser

If you have Python installed, it's pretty straightforward to use the seedparser. <strike>First, install nltk.</strike> Install TextBlob, which will install what you need from nltk automatically. Open a terminal and type:

~~~
$ pip install -U textblob
$ python -m textblob.download_corpora
~~~

Source text files can be weighted lists (run through, say, [wordclouds.com](http://www.wordclouds.com/)) or raw text. It doesn't really matter as long as it is plain text, though older files or ones with a lot of underscores and odd formatting might choke the script. Very long files (over ~165K words) take a while though. Note that it ignores word order, so if weighting is important to you, remove any low ranked words from the source before running the script.

Run the script in the same directory as your word file; it will output a .csv file and a .py file for each of the four required parts of speech (noun, adjective, adverb, verb). The .py is in python dictionary/list format and the csv has a comma-separated, numbered chart that should be straightforward to import into Google spreadsheets or a similar program.

For standard 100 element lists:

~~~
python seedparser.py <filename>
~~~

Flags:

* -x, --max,	number,
    The max number of elements in each final list or chart. Should be 10% to 25% higher than your intended final total to give you spares to replace miscategorized or boring words. Default is 110.
* -f, --fill,	True or False,
    Keep trying until the list is at the max number or a maximum number of tries is exceeded. Default is True.
* -c, --case,	u[pper], l[ower],
    Set the initial letter of each element of each list to uppercase or lowercase. Defaults to lowercase.
* -m, --min,	number,
     Minimum length of words to include; default is 4, to eliminate things like "get", "got", "put", "say". If you lower this, increase the max elements substantially to compensate for the useless entries.
* -l, --lemmatize,	True or False,
     Convert verbs to base form, ie, "asked" to "ask". Default is true.
* -p, --proper,	True or False,
   Include proper nouns or not. Default is false.
* -t, --print,	True or False,
    Print results to terminal. This makes it easy to copy and paste without having to open up the saved file. Default is False.
* -s, --second, True or False,
    Makes a second pass through the parts of speech filter. Also removes any adverbs not ending in 'ly'. Set to False if you're coming up short in the adverbs.

If you don't want to mess with this stuff, just do:

~~~
python seedparser.py <filename>
~~~

Finally, edit the resulting lists down, replacing any unsuitable words. You can import the csv into Google Spreadsheets (and likely other spreadsheet programs) as is or use the python code for further processing.

Here's an example from the first chapter of the Three Musketeers, completely uncurated (I can see at least a few that need to be swapped out), and copy pasted into a [csv to markdown converter](https://donatstudios.com/CsvToMarkdownTable) (don't forget to select "comma-separated" if you use it too).

|        |              |     |               |     |                |     |                |      |                |
|--------|--------------|-----|---------------|-----|----------------|-----|----------------|------|----------------|
| 1      |  accent      |  2  |  actor        |  3  |  addition      |  4  |  adversaries   |  5   |  attentions    |
|     6  |  calm        |  7  |  challenge    |  8  |  civilization  |  9  |  claim         |  10  |  complaints    |
|     11 |  conscience  |  12 |  contain      |  13 |  countries     |  14 |  dealer        |  15  |  desire        |
|     16 |  director    |  17 |  displeasing  |  18 |  doubts        |  19 |  effect        |  20  |  eminence      |
|     21 |  eyebrows    |  22 |  feather      |  23 |  fiery         |  24 |  foils         |  25  |  glass         |
|     26 |  godsend     |  27 |  group        |  28 |  hairs         |  29 |  half          |  30  |  haughty       |
|     31 |  haunting    |  32 |  heard        |  33 |  heron         |  34 |  hope          |  35  |  hostler       |
|     36 |  inclination |  37 |  influence    |  38 |  inquiring     |  39 |  insolence     |  40  |  interlocutors |
|     41 |  intrigue    |  42 |  look         |  43 |  love          |  44 |  lunge         |  45  |  masters       |
|     46 |  modesty     |  47 |  morbleu      |  48 |  mouth         |  49 |  muscles       |  50  |  necessity     |
|     51 |  newcomer    |  52 |  ninny        |  53 |  number        |  54 |  occasions     |  55  |  officer       |
|     56 |  openings    |  57 |  ordeal       |  58 |  organizations |  59 |  panics        |  60  |  passage       |
|     61 |  people      |  62 |  perspicacity |  63 |  physiognomy   |  64 |  piece         |  65  |  pink          |
|     66 |  places      |  67 |  protection   |  68 |  province      |  69 |  provinces     |  70  |  reason        |
|     71 |  regiment    |  72 |  remaining    |  73 |  remorse       |  74 |  riot          |  75  |  rosemary      |
|     76 |  s'blood     |  77 |  search       |  78 |  snare         |  79 |  society       |  80  |  soldiers      |
|     81 |  spit        |  82 |  stature      |  83 |  sticks        |  84 |  swordsmanship |  85  |  tender        |
|     86 |  thickness   |  87 |  things       |  88 |  tomorrow      |  89 |  tone          |  90  |  tones         |
|     91 |  tongue      |  92 |  valise       |  93 |  valor         |  94 |  visitor       |  95  |  waiter        |
|     96 |  waves       |  97 |  whence       |  98 |  wonder        |  99 |  world         |  100 |  wrist         |

##### Seed.py

You can also just use the included seed.py to generate seeds immediately, if you'd like. Drop it in the directory with your output files from running seedparser.py.

~~~
python seed.py <filename> -a verb -b noun
~~~

You can optionally specify an "-a" and a "-b" for which of the four parts of speech you want to grab. If they aren't specified they default to "verb" and "noun" for a Mythic-style result.

And there you go. A very simple, probably way more work to write than it would have been to just make a damn list by hand, unitasker script for turning texts into event lists.

<div id="button"><a href="https://github.com/exposit/katamoiran/tree/master/python/seedparser" class="btn btn-info">text to event chart converter scripts</a></div>
