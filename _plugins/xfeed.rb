require 'feedjira'

module Jekyll
  class MediumPostDisplay < Generator
    safe true
    priority :high
  def generate(site)
      jekyll_coll = Jekyll::Collection.new(site, 'externalfeed')
      site.collections['externalfeed'] = jekyll_coll

  #Feedjira::Feed.fetch_and_parse("https://exposit.github.io/katamoiran/feed.xml").entries.each do |e|
        #feed = Feedjira::Feed.fetch_and_parse("https://exposit.github.io/katamoiran/feed.xml")

    blogs = [  'http://www.bastionland.com/feeds/posts/default?alt=rss', 'http://falsemachine.blogspot.com/feeds/posts/default',
    'http://goblinpunch.blogspot.com/feeds/posts/default?alt=rss',
    'http://hackslashmaster.blogspot.com/feeds/posts/default',
    'http://necrotic-gnome-productions.blogspot.com/feeds/posts/default?alt=rss']
    blogs.each do |e|
        feed = Feedjira::Feed.fetch_and_parse(e)
        title = feed.title
        guid = feed.url
        entry = feed.entries.first
        etitle = entry.title
        eurl = entry.url
        # below this is assigning to a fake document
        path = "./_externalfeed/" + title + ".md"
        path = site.in_source_dir(path)
        doc = Jekyll::Document.new(path, { :site => site, :collection => jekyll_coll })
        doc.data['title'] = title;
        doc.data['guid'] = guid;
        doc.data['etitle'] = etitle;
        doc.data['eurl'] = eurl;
        jekyll_coll.docs << doc
      end

    end
  end
end
