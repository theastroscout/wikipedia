'''

Surfy Tests

'''

#pylint: disable=wrong-import-position

import sys
sys.path.append(sys.path[0]+'/..')

#pylint: enable=wrong-import-position

from wikipedia import Wiki


def test():

	'''
	
	Runs tests

	'''

	print(Wiki)
	wiki = Wiki()
	page = wiki.page('Eiffel Tower')
	# page = wiki.page('1900 Summer Olympics')
	print(page)
	if not page:
		print('Page Not Found')
		return False

	print(f'\nID: {page.id}')
	print(f'\nTitle: {page.title}')
	print(f'\nContent: {page.content[:250]}...')
	print(f'\nLinks: {page.links[:10]}...')
	print(f'\nSummary: {page.summary}')

	# Runs Tests

	# sqlite_test()

if __name__ == '__main__':
	test()
