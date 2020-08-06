# Class IV

## Examples

**webcache**
- Stale cache:
```py
# Command line program that repeatedly accepts URL as input and
# prints out the HTML data as output

import urllib.request

cache = {}

while True:

    url = input("Enter a URL: ")

    if url == "exit":
        break

    if url not in cache:
        print("CACHE MISS")
        response = urllib.request.urlopen(url)

        data = response.read()

        cache[url] = data

    else:
        print("CACHE HIT")

    print(cache[url][:60])
```