#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#### Site Settings ####
# http://docs.getpelican.com/en/3.6.3/settings.html
AUTHOR = 'Bonaventura Del Monte'
SITENAME = 'Bonaventura Del Monte, M.Sc.'

# The published SITEURL is set in publishconf.py
SITEURL = 'https://www.user.tu-berlin.de/ventura-delmonte/'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#### Configure as static homepage without blog ####
# When using static page as index, move blog index
INDEX_SAVE_AS = 'index.html'

# Disable tag-related pages
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

#### Blog settings ####
DEFAULT_PAGINATION = False

#### Theme settings ####
# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = "pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "paper"
PYGMENTS_STYLE = "bw"
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

CUSTOM_CSS = 'static/custom.css'
# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'pdfs', 'extra']
# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

# Feed generation is usually not desired when developing
# Publish options are set in publishconf.py
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#### Social media settings ####

# GITHUB_USER = "lutzcle"
# GITHUB_REPO_COUNT = 3
# GITHUB_SKIP_FORK = True
# GITHUB_SHOW_USER_LINK = True


# Blogroll
LINKS = (('IAM | DFKI', 'http://www.dfki.de/web/research/iam'),
        ('DIMA | TU Berlin', 'http://www.dima.tu-berlin.de'),
        ('Google Scholar', 'https://scholar.google.de/citations?user=KxroUEUAAAAJ&hl=en'),
        ('Slideshare', 'https://www.slideshare.net/BonaventuraDelMonte'),
        ('Imprint & Data Privacy', 'https://www.user.tu-berlin.de/ventura-delmonte/imprint.html'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/bonaventuradelmonte'),
          ('github', 'https://github.com/VenturaDelMonte'),)

