---
layout: post
title: Blogroll in Jekyll
date: 2018-11-16 11:09:00
categories: ['site']
tags: ['misc', 'python']
comments: true
published: true
---

I figured out a way to have a (somewhat) easy to keep current blogroll on Jekyll. The issue is that Jekyll is static -- the pages are generated when you upload them to github, and they don't change again until you update again, say, by pushing a new post or a typo fix.

I have a jekyll plugin that runs when I serve the site locally. It grabs the latest posts from the specified links, then updates one of the included sidebar pages with the latest information.

See example to your right, in the sidebar.

<!--more-->

So I write a post, run jekyll to make sure everything compiles and that there's no weird issues with the post (something I'll do anyway), and then push it to github as usual. Running jekyll locally refreshes the blogroll's links.

To use it yourself, put [xfeed.rb](https://github.com/exposit/katamoiran/blob/gh-pages/_plugins/xfeed.rb) in your _plugins directory, then work the code from [_includes/side_roll.html](https://github.com/exposit/katamoiran/blob/gh-pages/_includes/side_roll.html) into your layout in your preferred spot. or just include it as I've done on [_layouts/default.html](https://github.com/exposit/katamoiran/blob/gh-pages/_layouts/default.html).

Change the links in the "blog" variable in xfeed.rb, and change "./_includes/side_roll.html" in the next line down if necessary to the page you want to remake each time the plugin runs.

Also, you'll need to add feedjira to your config or to your gemfile.

From then on, before you push your site to github, run jekyll locally at least once to fetch new content.

I expect someone with better javascript knowledge than I have could do something more dynamic than this, but this works for my purposes.
