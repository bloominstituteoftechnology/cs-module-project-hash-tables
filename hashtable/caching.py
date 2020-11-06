
# Web client cache

# "client" gets whatever URL we provide

# this client should cache the web page

# on first request, the client fetches the web page
# on subsequent requests, the client gives you what it previously fetched

# why?
## speed
### especially for large pages or on a slow connection

## avoid database hits
### don't overpay for services
### countries that charge by download

# how to use hash tables to create a web client cache?
## (aka proxy server)

## what should be the key, what should be the value?
### value: the returned HTML/JS/CSS - the dom
### key: fetch date?, or URL

# thefacebook.com, google.com

import urllib.request

cache = {}
def web_client(URL):

    # check if the URL is in cache
    if URL in cache:
        print('found locally, saving time!!')
        return cache[URL]

    # otherwise, fetch and put in cache
    else:
        print("did not find, going out over the interwebs")
        response = urllib.request.urlopen(URL)

        data = response.read()

        response.close()

        cache[URL] = data

        return cache[URL]

web_client('https://www.google.com')
web_client('https://www.google.com')

# what if the web page changes? data in cache would be stale!
# Won't cache grow without end?