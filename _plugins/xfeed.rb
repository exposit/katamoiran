# So here's how this pain in the ass works. You add your feeds to the blogs array. Then you run jekyll locally, visit your site locally to make sure it looks okay, and then continue as normal.
# No, it won't update automatically. So post more frequently!
#
require 'feedjira'
require 'time'
require 'action_view'

include ActionView::Helpers::DateHelper

module Jekyll
  class RSSPostDisplay < Generator
    safe true
    priority :high
  def generate(site)
      #jekyll_coll = Jekyll::Collection.new(site, 'externalfeed')
      #site.collections['externalfeed'] = jekyll_coll

    t = File.ctime("./_includes/side_roll.html")

    if Time.now.utc - t > 500000000000

      blogs = [  'http://udan-adan.blogspot.com/feeds/posts/default?alt=rss',
            'https://coinsandscrolls.blogspot.com/feeds/posts/default?alt=rss',
            'http://www.bastionland.com/feeds/posts/default?alt=rss', 'http://falsemachine.blogspot.com/feeds/posts/default',
            'http://goblinpunch.blogspot.com/feeds/posts/default?alt=rss',
            'http://hackslashmaster.blogspot.com/feeds/posts/default',
            'http://necrotic-gnome-productions.blogspot.com/feeds/posts/default?alt=rss',
        ]

      fileHtml = File.new("./_includes/side_roll.html", "w+")
      fileHtml.puts '<section id="sidebar-roll" class="color2 rounded side">'
      fileHtml.puts '<div>'
      fileHtml.puts '<header class="major">'
      fileHtml.puts '<h3>Blogs I Read</h3>'
      fileHtml.puts '</header>'
      fileHtml.puts '<ul>'

      blogs.each do |e|
          feed = Feedjira::Feed.fetch_and_parse(e)
          title = feed.title
          guid = feed.url
          entry = feed.entries.first
          etitle = entry.title
          etitle = etitle.split[0...7].join(' ')
          eurl = entry.url
          pub = entry.published
          now = Time.now.utc
          #elapsed = time_ago_in_words(pub ) + ' ago' # out-dated almost immediately
          elapsed = pub.strftime("%b %d, %Y") # use the publication time instead

          fileHtml.puts '<li><a href="%s" target="_new">%s</a> | <a href="%s" target="_new">%s</a> | <cite>%s</cite></li>' % [guid, title, eurl, etitle, elapsed]


        end

        fileHtml.puts '</ul><div class="total-posts">... and about 300 more on <a href="https://www.inoreader.com/u/alto.dizi">innoreader</a></div></div></section>'

      end
    end
  end
end
