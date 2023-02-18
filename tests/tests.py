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
	print(page)
	if not page:
		print('Page Not Found')
		return False

	print(f'ID: {page.id}')
	print(f'Title: {page.title}')
	print(f'Content: {page.content[:250]}...')

	# Runs Tests

	# sqlite_test()

if __name__ == '__main__':
	test()
