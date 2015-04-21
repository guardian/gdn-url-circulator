import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode
from google.appengine.api import urlfetch

import pysistence as immutable

import sites

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

		template_values = {
			"sites" : sites.sites.get(name, json.dumps(sites.sites['default']))
		}

		self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
	('/', MainPage),
	webapp2.Route(r'/circulator/<slug>', handler=CirculatorDisplay),
	webapp2.Route(r'/percolator/<name>', handler=PercolatorDisplay),
	webapp2.Route(r'/percolater/<name>', handler=PercolatorDisplay),
	],
                              debug=True)