---
layout: post
title: Writing Tools
date: 2017-02-28 11:26:23
categories: ['writing']
tags: ['narrative', 'novel', 'writing', 'theory']
comments: true
published: true
---

Here's a quick rundown on my writing environment, just because I'm super pleased with it. I use a Mac, so some of these are mac or linux only, but the basic flow is pretty universal.

<!--more-->

My goal is to have a working environment where everything I need is right in front of me, so I can't tab away and get lost on TV Tropes or something. I also want my text to be as close to plain as I can get it -- I just had to take an 88K novel out of odt format and it was a pain (though less of a pain than some other conversions I've made over the years, that's for sure).

I'm using Atom.io as the main working platform. It's customizable, clean, loads fast, and supports gruvbox. What more could you want? Besides, it's a time-honored tradition to work on getting your working environment *just right* instead of, you know, actually working on writing.

I have a "novel" template that has my folders and subfolders, along with my LaTex templates and utility scripts.

I copy it into my Writing folder, which lives on my Google Drive, then rename it with a working title. I use the terminal to navigate to that new directory, initialize a git repo and do my first commit, then enter "atom ." to bring atom up in the current directory, turn the watcher on, make a new chapter file in the "Working" directory, and I'm good to go.

From this point forward, the only thing I need to do is write markdown chapters in the "Working" directory. I use LaTex commands when I want scene breaks, for notes, and to title the chapter, and markdown for italics, all in the same markdown file.

If I want to see what the manuscript will look like (roughly!) as a finished ebook, it takes seconds -- just flip to the ebook template (still in atom) and hit cmd+s. Same with the manuscript template, which mimics an old school ms submission.

If I want a word count, I flip to wordcount.py (again, still in atom), and hit cmd+i. This shows me how many words I've written today and logs it to a json file.

When I'm done, usually at the end of the day, I run wordcount.py, then close down atom and do a quick commit to the repository.

Why Google Drive AND git? Google Drive is my backup. Git is my version control.

If my hard drive dies (again) I'll be back up and running exactly where I am now in the time it takes to set Google Drive to download my content and to reinstall my atom extensions.

If I accidentally delete an entire scene and don't notice for a week, git is how I get it back. If I totally blow a find and replace and end up with "dawizard" level issues but don't notice until I've done two days of further editing, it's fixable. If I want to see the difference between today's edits and yesterday's final, it's all there.

I should mention, I don't really use the LaTex-produced pdfs for working; it's much easier to edit the raw markdown files. But sometimes it's nice to see how a section "plays" in a typset form, or to be able to set aisde the "editing" part of my brain so I can focus on the plot and structure.

I also keep Pythia open on a desktop to the left of my writing desktop, where I can flip over to ask a question as needed.

Other things I could do in atom (but usually don't):

* run spotify through atom
* run youtube through atom
* run an rss feed in the status bar

Finally, a special mention for MacDown. Pretty much my go-to text-edit replacement. It's beautiful, functional, stylish, and lets me just write some damn notes. I don't use it so often when writing, because I have atom already open, but for just taking quick notes or jotting down ideas? Perfect.
