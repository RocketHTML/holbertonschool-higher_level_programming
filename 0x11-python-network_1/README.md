# Python Networking
## Purpose
*To learn:*
  * How to fetch internet resources with the Python package urllib
  * How to decode urllib body response
  * How to use the Python package requests
  * How to make HTTP GET requests
  * How to make HTTP POST/PUT/etc. requests
  * How to fetch JSON resources
  * How to manipulate data from an external service
>[url.request doc](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)

## urllib.request
> **urllib.request** is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function. This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on. These are provided by objects called handlers and openers.
>
>urllib.request supports fetching URLs for many “URL schemes” (identified by the string before the ":" in URL - for example "ftp" is the URL scheme of "ftp://python.org/") using their associated network protocols (e.g. FTP, HTTP).
>
>For straightforward situations urlopen is very easy to use. But as soon as you encounter errors or non-trivial cases when opening HTTP URLs, you will need some understanding of the HyperText Transfer Protocol. The most comprehensive and authoritative reference to HTTP is [RFC 2616](https://tools.ietf.org/html/rfc2616.html). This is a technical document and not intended to be easy to read.
>[docs.python](https://docs.python.org/3/howto/urllib2.html)
 
## Requests
[Quickstart](http://docs.python-requests.org/en/master/user/quickstart/#make-a-request)