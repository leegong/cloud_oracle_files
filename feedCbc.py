import feedparser


d = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fwww.cbc.ca%2Fnews&in_id_or_class=feed-content+content&max=5&order=document&guid=0')
print len(d['entries'])
print ()
for post in d.entries:
    print post.title + ": \n" + post.link + " \n "


raw_input("Press Enter to continue...")


e = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fwww.cbc.ca%2Fnews&in_id_or_class=contentList+sclt-featurednewscontentlist&max=5&order=document&guid=0')
print len(e['entries'])
print ()
for post in e.entries:
    print post.title + ": \n" + post.link + " \n "
