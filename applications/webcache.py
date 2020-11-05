"""
1. Have a input loop that gets a URL from the user
2. Fetch the data at the URL and display it
3. Cache the data for subsequent lookups
4. Expire the cache entries after 10 seconds
"""
import urllib.request
import datetime​

CACHE_EXPIRATION_SECONDS = 10​

class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = get_timestamp()​

cache = {}​

def get_timestamp():
    return datetime.datetime.now().timestamp()​

def get_data(url):
    cur_time = get_timestamp()​

    if (url not in cache) or (cur_time - cache[url].timestamp > CACHE_EXPIRATION_SECONDS):
        print("CACHE MISS")
        resp = urllib.request.urlopen(url)​

        data = resp.read()​

        resp.close()​

        data = data.decode() # turns bytes into string​

        cache[url] = CacheEntry(url, data)​

    return cache[url].data
​

if __name__ == "__main__":
    while True:
        url = input("Enter a URL: ")
        print(get_data(url)[:100])