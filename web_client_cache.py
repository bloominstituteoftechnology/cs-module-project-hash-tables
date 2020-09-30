#Make a web client that fetches URLS

## It should cache the results of the call

## On first request, client fetches the web page

## on any subsequent request, client returns from the cache
print("Hellocccc ")
print("Hellocccc ")
print("Hellocccc ")
print("Hellocccc ")
 
 
 
##Why would we make this?

### Speed don't have to reload the entire page
import urllib.request
import requests
cache = {}
def client_fetch(url):
    if url in cache:
        print("We already have this")
        return cache [url]
    
    else:
        data = urllib.request(url).text
  