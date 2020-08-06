# Command line program that repeatedly accepts URL as input and
# prints out the HTML data as output

import urllib.request
import datetime

class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()

cache = {}

TIMEOUT_SECONDS = 10

while True:

    url = input("Enter a URL: ")

    if url == "exit":
        break

    needs_refresh = False

    if url not in cache:
        needs_refresh = True
    else:
        # Did it timeout?
        cur_time = datetime.datetime.now().timestamp()
        diff_time = cur_time - cache[url].timestamp

        # if diff_time > TIMEOUT_SECOND:
        #     needs_refresh = True
        needs_refresh = diff_time > TIMEOUT_SECONDS

    if needs_refresh:
        print("GETTING FROM SERVER")
        response = urllib.request.urlopen(url)

        data = response.read()

        cache[url] = CacheEntry(url, data)

    # else:
    #     print("CACHE HIT")

    print(cache[url].data[:60])

    