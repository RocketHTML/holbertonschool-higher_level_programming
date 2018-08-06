# urllib.request

## Preface
> **urllib.request** is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function. This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common situations - like basic authentication, cookies, proxies and so on. These are provided by objects called handlers and openers.
>
>urllib.request supports fetching URLs for many “URL schemes” (identified by the string before the ":" in URL - for example "ftp" is the URL scheme of "ftp://python.org/") using their associated network protocols (e.g. FTP, HTTP).
>
>For straightforward situations urlopen is very easy to use. But as soon as you encounter errors or non-trivial cases when opening HTTP URLs, you will need some understanding of the HyperText Transfer Protocol. The most comprehensive and authoritative reference to HTTP is [RFC 2616](https://tools.ietf.org/html/rfc2616.html). This is a technical document and not intended to be easy to read.
>[docs.python](https://docs.python.org/3/howto/urllib2.html)
>[url.request doc](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)

## Purpose
*To learn:*
  * How to fetch internet resources with the Python package urllib
  * How to decode urllib body response
  * How to use the Python package requests
  * How to make HTTP GET requests
  * How to make HTTP POST/PUT/etc. requests
  * How to fetch JSON resources
  * How to manipulate data from an external service

## Structure
HTTP is based on requests and responses - the client makes requests and servers send responses. urllib.request mirrors this with a Request object which represents the HTTP request you are making. In its simplest form you create a Request object that specifies the URL you want to fetch. Calling urlopen with this Request object returns a response object for the URL requested. This response is a file-like object, which means you can for example call .read() on the response

In the case of HTTP, there are two extra things that Request objects allow you to do: First, you can pass data to be sent to the server. Second, you can pass extra information (“metadata”) about the data or the about request itself, to the server - this information is sent as HTTP “headers”.

The response returned by urlopen (or the HTTPError instance) has two useful methods info() and geturl() and is defined in the module [urllib.response](https://docs.python.org/3/library/urllib.request.html#module-urllib.response)

### info and geturl
The response returned by urlopen (or the HTTPError instance) has two useful methods info() and geturl() and is defined in the module urllib.response..

geturl - this returns the real URL of the page fetched. This is useful because urlopen (or the opener object used) may have followed a redirect. The URL of the page fetched may not be the same as the URL requested.

info - this returns a dictionary-like object that describes the page fetched, particularly the headers sent by the server. It is currently an http.client.HTTPMessage instance.

Typical headers include ‘Content-length’, ‘Content-type’, and so on. See the Quick Reference to HTTP Headers for a useful listing of HTTP headers with brief explanations of their meaning and use.

##############################################################
# Requests