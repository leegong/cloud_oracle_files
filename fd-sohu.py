import feedparser


d = feedparser.parse('https://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fnews.sohu.com%2F&in_id_or_class=block3&max=5&order=document&guid=0')
int (len(d['entries']))
print ()
for post in d.entries:
    print (post.title + ": \n" + post.link + " \n ")

input("Press Enter to continue...")

e = feedparser.parse('https://createfeed.fivefilters.org/extract.php?url=https%3A%2F%2Fwww.sohu.com%2Fxchannel%2Ftag%3Fkey%3D%25E6%2596%25B0%25E9%2597%25BB-%25E6%2597%25B6%25E6%2594%25BF%26scm%3D10000.457_14-201000.0.0.10005%26spm%3Dsmpc.channel_258.block2_225_ZJhqAx_1_nav.2.17034586650310eDBYRJ_1090&in_id_or_class=main&max=5&order=document&guid=0')
print (len(e['entries']))
print ()
for post in e.entries:
    print (post.title + ": \n" + post.link + " \n ")
