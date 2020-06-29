"""
Caching web client

Go get URLs
Cache the result

Cache entries should timeout after 10 seconds - this keeps the website from being stale.



Things to do:
*Read data from URLs
*Have a CacheEntry object to hold data and timestamps
* Compute time differences against timestamps

great for demos:
http://www.example.com

you can collect data from your router
example: 192.168.100.1
"""
"""
Import Statements:
"""




import urllib.request
import time
class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = time.time()


# dictionary of cache entries
cache = {}
CACHE_TIMEOUT_SECONDS = 10


def get_data(url):
    current_time = time.time()

    if (url not in cache) or (current_time - cache[url].timestamp > CACHE_TIMEOUT_SECONDS):
        print("FECHING FROM SERVER")
        with urllib.request.urlopen(url) as f:
            # cache[url] = f.read().decode('utf-8', 'ignore')
            data = f.read().decode('utf-8',  'ignore')
            cache = [url] = CacheEntry(url, data)

    else:
        print('FETCHING FROM CACHE')
        age = time.time() - cache[url].timestamp
        print(f"Age: {age}")

    return cache[url]


def main():
    while True:
        print(cache)
        # get our input
        url = input("Enter URL: ")
        entry = get_data(url)
        print(entry.data[:40])

        # get data from cache or webserver
        # data = get_data(url)
        #
        # print(data)[:40]


if __name__ == "__main__":
    main()
