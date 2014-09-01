#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rick Gilmore'
SITENAME = u"Rick Gilmore's Site"
SITEURL = 'http://rick-gilmore.org'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']

THEME = '/Users/rick/Sites/pelican/pelican-themes/tuxlite_tbs'
EXTRA_TEMPLATES_PATHS = ['/Users/rick/Sites/pelican/my-templates']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation
FEED_DOMAIN = SITEURL	
FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
# TRANSLATION_FEED_ATOM = None
# TAG_FEED_ATOM = 'feeds/%s.atom.xml'

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_ATOM = 'feeds/%.rss.xml'
# TRANSLATION_FEED_RSS = None
# TAG_FEED_RSS = 'feeds/%s.rss.xml'

# Templates
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'work', 'play', 'contact')

TEMPLATE_PAGES = {'/Users/rick/Sites/pelican/my-templates/work.html': '/Users/rick/Sites/pelican/output/work.html',
				  '/Users/rick/Sites/pelican/my-templates/play.html': '/Users/rick/Sites/pelican/output/play.html', 
				  '/Users/rick/Sites/pelican/my-templates/contact.html': '/Users/rick/Sites/pelican/output/contact.html'}

# Blogroll
LINKS = (('home', 'http://rick-gilmore.org/index.html'),
		 ('work', 'http://rick-gilmore.org/work.html'),
		 ('play', 'http://rick-gilmore.org/play.html'),
		 ('contact','http://rick-gilmore.org/contact.html'))

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/rogilmore'),
          ('GitHub', 'http://github.com/rogilmore'),
          ('LinkedIn', 'http://http://www.linkedin.com/pub/rick-gilmore/a/471/398'))

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
