import pysistence as immutable

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

paul_owen_us = immutable.make_list(
	'http://www.theguardian.com/uk',
	'http://www.theguardian.com/us',
	'http://www.theguardian.com/au',
	'http://www.theguardian.com/international',
	'http://www.nytimes.com',
	'http://www.washingtonpost.com',
	'http://www.bbc.com/news/',
	'http://www.latimes.com/',
	'http://www.buzzfeed.com/',
	'http://news.vice.com/',
	'http://www.nydailynews.com/',
	'http://www.ajc.com/',
	'http://www.cnn.com/',
	'http://www.realclearpolitics.com/',
	'http://fivethirtyeight.com')

sites = {
	'default' : list(default_list),
	'paul-owen' : list(default_list.concat(paul_owen)),
	'paul-owen-us': list(paul_owen_us),
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