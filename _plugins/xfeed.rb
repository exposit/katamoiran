# So here's how this pain in the ass works. You add your feeds to the blogs array. Then you run jekyll locally, visit your site locally to make sure it looks okay, and then continue as normal.
# No, it won't update automatically. So post more frequently!
require 'feedjira'

module Jekyll
  class MediumPostDisplay < Generator
    safe true
    priority :high
  def generate(site)
      #jekyll_coll = Jekyll::Collection.new(site, 'externalfeed')
      #site.collections['externalfeed'] = jekyll_coll

    blogs = [  'http://www.bastionland.com/feeds/posts/default?alt=rss', 'http://falsemachine.blogspot.com/feeds/posts/default',
    'http://goblinpunch.blogspot.com/feeds/posts/default?alt=rss',
    'http://hackslashmaster.blogspot.com/feeds/posts/default',
    'http://necrotic-gnome-productions.blogspot.com/feeds/posts/default?alt=rss']

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
        eurl = entry.url

        fileHtml.puts '<li><a href="%s" target="_new">%s</a> | <a href="%s" target="_new">%s</a></li>' % [guid, title, eurl, etitle]

        # assigning stuff to a fake document; isn't useful because plugins are no bueno on github pages
        # path = "./_externalfeed/" + title + ".md"
        # path = site.in_source_dir(path)
        # doc = Jekyll::Document.new(path, { :site => site, :collection => jekyll_coll })
        # doc.data['title'] = title;
        # doc.data['guid'] = guid;
        # doc.data['etitle'] = etitle;
        # doc.data['eurl'] = eurl;
        # jekyll_coll.docs << doc
        # so write a real document

      end

      fileHtml.puts '</ul></div></section>'

    end
  end
end
