'''

Wikipedia

'''

import json
from urllib.parse import quote as encode
import requests

class Wiki:

	'''

	Create Wikipedia Global

	'''

	def __init__(self, options=False):

		'''

		Initialisation

		'''

		if not options:
			options = {
				'lang': 'en',
				'redirect': 1
			}

		self.options = options

		if 'lang' not in options:
			self.options['lang'] = 'en'

		if 'redirect' not in options:
			self.options['redirect'] = 1

	def set_lang(self, lang):

		'''

		Set Global Lang

		'''

		self.options['lang'] = lang

	def page(self, addr, lang=False):

		'''

		Get Page Instance

		'''

		if not lang:
			lang = self.options['lang']

		if isinstance(addr, int):

			# Extract Title From ID

			url = f"http://{lang}.wikipedia.org/w/api.php?action=query&pageids={addr}&format=json"

			x = requests.get(url, timeout=5)
			data = json.loads(x.text)
			if not data['pages']:
				return False

			if str(addr) not in data['pages']:
				return False

			addr = data['pages'][str(addr)]['title']

		# Get Page

		url = f"https://{lang}.wikipedia.org/w/rest.php/v1/page/{encode(addr)}/bare"
		x = requests.get(url, timeout=5)
		data = json.loads(x.text)

		if 'httpCode' in data and data['httpCode'] == 404:
			return False

		page_options = self.options
		page_options['lang'] = lang
		return Page(data, page_options)


class Page:

	'''
	
	Create Wiki Page Instance

	'''

	def __init__(self, data, options):

		'''

		Initialisation

		'''

		self.options = options
		self.data = data
		self.id = data['id']
		self.title = data['title']
		self.key = data['key']
		self.html_url = data['html_url']

		self.get_content()

		self.summary = self.get_summary()

	def get_content(self):

		'''

		Get Cotent and Links

		'''

		url = f"https://{self.options['lang']}.wikipedia.org/w/api.php?action=query&format=json&titles={self.key}&prop=extracts|links&explaintext"

		# Request API
		x = requests.get(url, timeout=5)
		data = json.loads(x.text)

		# Page Not Found
		if '-1' in data['query']['pages']:
			return False

		# Get Plain Text Content

		self.content = data['query']['pages'][str(self.id)]['extract']

		# Get Links

		links = []
		for link in data['query']['pages'][str(self.id)]['links']:
			links.append(link['title'])
		self.links = links

		return True

	def get_summary(self):

		'''

		Get Summary

		'''

		url = f"https://{self.options['lang']}.wikipedia.org/w/api.php?format=json&action=query&redirects=1&titles={self.key}&prop=extracts&explaintext&exintro"

		# Request API
		x = requests.get(url, timeout=5)
		data = json.loads(x.text)

		# Page Not Found
		if '-1' in data['query']['pages']:
			return False

		# Get Plain Text Summary

		return data['query']['pages'][str(self.id)]['extract']
