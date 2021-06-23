import feedparser


d = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fnews.sina.com.cn%2F&in_id_or_class=linkNewsTopBold&max=5&order=document&guid=0')
print len(d['entries'])
print ()
for post in d.entries:
    print post.title + ": \n" + post.link + " \n "

raw_input("Press Enter to continue...")

e = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fnews.sina.com.cn%2F&in_id_or_class=list_14&max=5&order=document&guid=0')
print len(e['entries'])
print ()
for post in e.entries:
    print post.title + ": \n" + post.link + " \n "

raw_input("Press Enter to continue...")

f = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fnews.sina.com.cn%2F&in_id_or_class=list_14&max=5&order=document&guid=0')
print ()
for post in f.entries:
    print post.title + ": \n" + post.link + " \n "

raw_input("Press Enter to continue...")

g = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fnews.sina.com.cn%2F&in_id_or_class=dot+topli14&max=5&order=document&guid=0')
print len(g['entries'])
print ()
for post in g.entries:
    print post.title + ": \n" + post.link + " \n "

raw_input("Press Enter to continue...")

h = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fnews.sina.com.cn%2F&in_id_or_class=list_14_noBg&max=5&order=document&guid=0')
print len(h['entries'])
print ()
for post in h.entries:
    print post.title + ": \n" + post.link + " \n "

raw_input("Press Enter to continue...")

i = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fnews.sina.com.cn%2F&in_id_or_class=exclsv_hot_ls&max=5&order=document&guid=0')
print len(i['entries'])
print ()
for post in i.entries:
    print post.title + ": \n" + post.link + " \n "

raw_input("Press Enter to continue...")

j = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fnews.sina.com.cn%2F&in_id_or_class=list_12+link_c666&max=5&order=document&guid=0')
print len(j['entries'])
print ()
for post in j.entries:
    print post.title + ": \n" + post.link + " \n "
