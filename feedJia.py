import feedparser


d = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=toronto.iask.ca%2F&in_id_or_class=h3title&max=5&order=document&guid=0')
print (len(d['entries']))
print ()
for post in d.entries:
    print (post.title + ": \n" + post.link + " \n ")

input("Press Enter to continue...")

e = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=toronto.iask.ca%2F&in_id_or_class=main-title&max=5&order=document&guid=0')
print (len(e['entries']))
print ()
for post in e.entries:
    print (post.title + ": \n" + post.link + " \n ")
