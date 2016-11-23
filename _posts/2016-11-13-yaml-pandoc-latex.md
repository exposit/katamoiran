---
layout: post
title: Pretty PDFs From Play Logs
date: 2016-11-13 03:08:09
categories: [pythia]
tags: [pythia, tools, logs, formatting]
published: true
comments: true
links:
  - url: https://exposit.github.io/pythia-oracle/
    title: Pythia-Oracle
    source: katamoiran
  - url: https://tug.org/mactex/
    title: MacTex
    source:
  - url: http://pandoc.org/
    title: pandoc
    source:
  - url: https://en.wikibooks.org/wiki/LaTeX/Colors
    title: LaTex Colors
    source: wikibooks
  - url: https://fonts.google.com/
    title: Cormorant, Lora, or Trirong
    source: Google Fonts
---

I've been experimenting with logforms and the way the logs out of Pythia are displayed. I like being able to read my logs as pdfs, and pandoc makes a very pretty "book" almost by default out of markdown, but I wanted a couple of things that were much harder to accomplish than expected.

1. I wanted all the "mechanics" to be a lighter color than the "fiction". This is the same color pattern I use for logs I post on my blog, and it works really well for emphasizing the narrative while keeping the mechanics accessible.
2. I wanted it automated, or as automated as possible.

Turns out it's *hard* to figure LaTex out. Simple things like "make all italic and bold font a specific color" aren't trivial. It's a very oblique process where everyone seems to know the basics but nobody thinks to mention them. And where the documentation is as clear as mud and has lots and lots of curly brackets. So many curly brackets.


<!--more-->


"Automated" means Pythia pushing properly formatted text, with YML header. Then using pandoc to converts that markdown file to pdf. Also not trivial -- logforms are complicated and the more complicated they are, the more tedious to debug. I'm still working on the logform, in fact. It handles mechanics blocks properly and fiction blocks properly, but not sub-formatting in mechanics blocks. But it's good enough.

Anyway, this is what works.

#### How, or "that's eight hours I'm not getting back"

First, update your [Pythia](https://exposit.github.io/pythia-oracle/) to the latest commit (anything after 11/13 should work fine).

If you aren't using git, this means moving your saves and backups elsewhere, deleting your Pythia directory, downloading the zip from the repo, unzipping it, and copying your saves and backups back in. Usual install process applies, especially if you haven't updated in a while.  You mostly just need the *pdf.py file in resources/logforms and the config.py.

1. Download [MacTex](https://tug.org/mactex/) or BasicTex or whatever *tex your platform uses. Install.
2. Go to your Applications and open up Tex Live Utility and update everything that needs to be updated. Install xcolor if necessary.
3. Install [pandoc](http://pandoc.org/). This is trivial with homebrew.
4. Edit config.py's yaml variables to reflect your information and font and color preferences.
4. Open a game in Pythia. After you exit, all the new logs will be generated (alongside/over your old ones if any exist).

When that's all done, navigate to the log directory that has the log you want. Open it up. You should see something like the following header; the boilerplate can be edited in the main config.py.

You can also just copy-paste this into the head of any markdown file.

```yaml
---
fontsize: 10pt
sansfont: Ubuntu Mono
mainfont: Lora
title: your title
header-includes:
   - \usepackage{xcolor}
   - \usepackage{fontspec}
   - \definecolor{light-gray}{gray}{0.60}
   - \setmainfont[UprightFeatures = {Color=black}, ItalicFeatures = {Color=light-gray}, BoldFeatures = {Color=light-gray}, BoldItalicFeatures = {Color=light-gray} ] {Lora}
   - \setmonofont[UprightFeatures = {Color=light-gray}] {Ubuntu Mono}
   - \newfontfamily\plain[ItalicFeatures = {Color=black}, BoldFeatures = {Color=black}, BoldItalicFeatures = {Color=black}] {Lora}
---
```

That's what you put in the YAML header to make your pandoc-created Markdown-to-LaTex pdf out of one of Pythia's ".md" logs, with "black" colored fiction blocks and "light gray" everything else. Assuming your font supports it.

Basically, we're setting all the base fonts except the regular (non italic, non bold) to light gray (since Pythia outputs everything not tagged "plain" as italic, bold, or bold-italic), and then reverting any italics or bold inside the plain blocks back to black. It's not perfect, because we rely on the logform to tag exceptions with "\plain", and it completely ignores the case of differing formatting inside a single mechanics block, but it's pretty close.

Obviously you can change the colors around; define whatever colors you'd like to use, using any of the patterns here: [LaTex colors at wikibooks](https://en.wikibooks.org/wiki/LaTeX/Colors). Or just adjust the definition for "light-gray"; the closer the ".60" is to 1.0, the darker the color. I would suggest .30, .60, or .90.

Or just go html:

```tex
\definecolor{light-gray}{HTML}{c1c1c1}
```

Pick a different font if you'd like, too. Heck, pick ALL different fonts. I think you need it installed. For the main font, I'd suggest [Cormorant, Lora, or Trirong](https://fonts.google.com/), ordered from most "print-like" to most "modern" (not technical terms, ha).

This is the command in my terminal that I use to generate the actual pdf:

```bash
$pandoc -o test.pdf complete_yaml_pdf.md --latex-engine=xelatex
```

If your paths aren't set, you can try putting "/usr/local/texlive/2016basic/bin/universal-darwin/" between the words "engine=" and "xelatex".

---

Is this the best way? I don't know. It's the way I came up with. After eight bleepin' hours trying various things, well past the point where the drive behind the idle thought of "hey, I'd like to view my logs in pdf the same way I view them on my blog" turned into "I will conquer this &!#$!in' thing if it kills me".

And it is working. Fonts are displaying properly as far as I can see, just gray and black instead of all black. Which is all I wanted. So I could read nice pdfs of my play logs. Now it's too late to read anything. Goodnight.
