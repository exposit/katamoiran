require 'feedjira'

module Jekyll
  class MediumPostDisplay < Generator
    safe true
    priority :high
  def generate(site)
      #jekyll_coll = Jekyll::Collection.new(site, 'externalfeed')
      #site.collections['externalfeed'] = jekyll_coll

  #Feedjira::Feed.fetch_and_parse("https://exposit.github.io/katamoiran/feed.xml").entries.each do |e|
  #feed = Feedjira::Feed.fetch_and_parse("https://exposit.github.io/katamoiran/feed.xml")

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

        # below this is assigning to a fake document; isn't useful because plugins are no bueno
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
