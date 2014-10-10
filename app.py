import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode
from google.appengine.api import urlfetch

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

class PercolaterDisplay(webapp2.RequestHandler):
	def get(self, name):
		template = jinja_environment.get_template('percolater.html')

		sites = {
			'default' : ['http://www.bbc.co.uk/news/',
				"http://www.thetimes.co.uk/",
				"http://www.telegraph.co.uk",
				"http://www.ft.com",
				"http://m.sky.com/skynews/news",
				"http://www.dailymail.co.uk/",
				"http://m.independent.co.uk",
				"http://www.mirror.co.uk",
				"http://www.aljazeera.com/",
				"http://www.cnn.com/",],
		}

		template_values = {
			"sites" : sites.get(name, json.dumps(sites['default']))
		}

		self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage),
	webapp2.Route(r'/circulator/<slug>', handler=CirculatorDisplay),
	webapp2.Route(r'/percolater/<name>', handler=PercolaterDisplay),],
                              debug=True)