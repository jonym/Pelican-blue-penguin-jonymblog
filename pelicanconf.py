#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jonym'
SITENAME = u"小马的杂货铺"
SITEURL = 'http://jonym.com'
TIMEZONE = 'Asia/Shanghai'

PATH = 'content'
DATE_FORMATS = {
    'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_LANG = u'zh_CN'
LOCALE = ('en_US')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = 'blue-penguin'

DISQUS_SITENAME = u"jonym"

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = False
DISPLAY_MENU   = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
#TAGS_URL           = 'tags'
#TAGS_SAVE_AS       = 'tags/index.html'
HOME_URL            = 'index'
HOME_SAVE_AS        = 'index.html'
ABOUT_URL           = 'pages/about-me'
ABOUT_SAVE_AS       = 'pages/about-me.html'
#AUTHORS_URL        = 'authors'
#AUTHORS_SAVE_AS    = 'authors/index.html'
#CATEGORIES_URL     = 'categories'
#CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL        = 'archives'
ARCHIVES_SAVE_AS    = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    #('Tags', TAGS_URL, TAGS_SAVE_AS),
    #('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
    #('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Home',HOME_URL,HOME_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
    ('About Me', ABOUT_URL, ABOUT_SAVE_AS),
)
# additional menu items
#MENUITEMS = (
#    ('GitHub', 'https://github.com/'),
#    ('Linux Kernel', 'https://www.kernel.org/'),
#)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
