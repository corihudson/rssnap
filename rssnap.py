import snapext
import feedparser
f = feedparser.parse('http://technoboy10.tk/rss')
handler = snapext.SnapHandler

@handler.route('/feed/set')
def setfeed(url):
	global f
	f = feedparser.parse(url)
@handler.route('/feed/title')
def ft():
	return f.feed.title
@handler.route('/feed/url')
def furl():
	return f.feed.link
@handler.route('/feed/desc')
def fdesc():
	return f.feed.description
@handler.route('/article/title')
def at(post):
	post -= 1
	return f.entries[post].title
@handler.route('/article/link')
def al(post):
	post -= 1
	return f.entries[post].link
@handler.route('/article/desc')
def at(post):
	post -= 1
	return f.entries[post].description
snapext.main(handler, 1819)
