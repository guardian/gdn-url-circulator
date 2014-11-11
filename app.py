import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode
from google.appengine.api import urlfetch

import pysistence as immutable

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

class MainPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		
		template_values = {}

		self.response.out.write(template.render(template_values))

class CirculatorDisplay(webapp2.RequestHandler):
	def get(self, slug):
		template = jinja_environment.get_template('circulator.html')
		template_values = {}

		self.response.out.write(template.render(template_values))

class PercolatorDisplay(webapp2.RequestHandler):
	def get(self, name):
		template = jinja_environment.get_template('percolater.html')

		default_list = immutable.make_list(
				'http://gu-front-checker.appspot.com/',
				'http://www.bbc.co.uk/news/',
				"http://www.thetimes.co.uk/",
				"http://www.telegraph.co.uk",
				"http://www.ft.com",
				"http://m.sky.com/skynews/news",
				"http://www.dailymail.co.uk/",
				"http://m.independent.co.uk",
				"http://www.mirror.co.uk",
				"http://www.aljazeera.com/",
				"http://www.cnn.com/",
			)

		paul_owen = immutable.make_list(
			'http://www.theguardian.com/au',
			'http://www.theguardian.com/us',
			'http://www.buzzfeed.com/',
			'https://news.vice.com/',
			'http://www.nytimes.com/',
			)

		sites = {
			'default' : list(default_list),
			'paul-owen' : list(default_list.concat(paul_owen)),
			'au-nf' : [
				'http://gu-front-checker.appspot.com/au',
				"http://www.sbs.com.au/news/",
				"http://www.news.com.au",
				"http://www.abc.net.au/news/nsw/",
				"http://www.theage.com.au",

				"http://www.afr.com",
				"http://www.smh.com.au",
				"http://www.theaustralian.com.au",
				"http://www.couriermail.com.au",

				"http://www.dailytelegraph.com.au/",
				"http://www.heraldsun.com.au/",
				"http://www.ntnews.com.au/",
				"http://www.perthnow.com.au/",

				"http://www.sbs.com.au/news/latest-news",
				"http://www.theage.com.au/news-wire",
				"http://www.theaustralian.com.au/news/latest-news",
				"http://www.news.com.au/breaking-news",

			],
		}

		template_values = {
			"sites" : sites.get(name, json.dumps(sites['default']))
		}

		self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
	('/', MainPage),
	webapp2.Route(r'/circulator/<slug>', handler=CirculatorDisplay),
	webapp2.Route(r'/percolator/<name>', handler=PercolatorDisplay),
	webapp2.Route(r'/percolater/<name>', handler=PercolatorDisplay),
	],
                              debug=True)