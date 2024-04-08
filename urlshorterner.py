# Build a URL shortening service that converts long URLs into shorter ones. This project involves string manipulation and handling HTTP requests.

import random
import string
import pyshorteners

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.alphabet = string.ascii_letters + string.digits

    def generate_short_url(self, long_url):
        short_url = pyshorteners.Shortener().tinyurl.short(long_url)
        while short_url in self.url_map.values():
            short_url = pyshorteners.Shortener().tinyurl.short(long_url)
        self.url_map[short_url] = long_url
        return short_url

    def get_long_url(self, short_url):
        return self.url_map.get(short_url, None)

# Usage
shortener = URLShortener()
long_url = input("Enter a long URL: ")
short_url = shortener.generate_short_url(long_url)
print("Shortened URL:", short_url)
print("Long URL:", shortener.get_long_url(short_url))
