'''

Wikipedia

'''

import requests, json
from urllib.parse import quote as encode

class Wiki:

	def __init__(self, options={}):
		self.options = options
		if 'lang' not in options:
			self.options['lang'] = 'en'

	def page(self, addr):

		'''
	
		Get Page

		'''

		params = {}
		if isinstance(addr, int):

			# Extract Title From ID

			url = f"http://{self.options['lang']}.wikipedia.org/w/api.php?action=query&pageids={addr}&format=json"

			x = requests.get(url)
			data = json.loads(x.text)
			if not data['pages']:
				return False

			if str(addr) not in data['pages']:
				return False

			addr = data['pages'][str(addr)]['title']
		
		# Get Page

		url = f"https://{self.options['lang']}.wikipedia.org/w/rest.php/v1/page/{encode(addr)}/bare"
		x = requests.get(url)
		data = json.loads(x.text)
		
		if 'httpCode' in data and data['httpCode'] == 404:
			return False

		return Page(data, self.options)


class Page:

	def __init__(self, data, options):
		self.options = options
		self.data = data
		self.id = data['id']
		self.title = data['title']
		self.key = data['key']
		self.html_url = data['html_url']
		self.content = self.getContent()

	def getContent(self):
		url = f"https://{self.options['lang']}.wikipedia.org/w/api.php?action=query&format=json&titles={self.title}&prop=extracts&explaintext"

		x = requests.get(url)
		data = json.loads(x.text)
		if '-1' in data['query']['pages']:
			return False

		return data['query']['pages'][str(self.id)]['extract']




