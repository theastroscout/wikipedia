![Wikipedia](https://github.com/theastroscout/wikipedia/blob/main/imgs/cover.1.png?raw=true "Wikipedia")

# Wikipedia Python Library
<br/>

## Usage
```python

from wikipedia import Wiki
wiki = Wiki()

```
<br/>

### Get Page by Title or Page ID

```python

page = wiki.page('Eiffel Tower')

if not page:
	print('Page Not Found')
else:
	page.id # Page ID
	page.title # Page Title
	page.content # Page Plain Text Content
	page.links # All links from the page
	page.summary # Plain Text Summary

```

<br />
<br />

## MIT License

Alexander Yermolenko • [surfy.one](https://surfy.one)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.