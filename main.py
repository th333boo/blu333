#!/usr/bin/env python3
# coding: utf-8
from urllib.parse import urlparse

urlsearch = "https://packages.debian.org/search?keywords=tor&searchon=names&suite=stable&section=all"
url = "https://packages.debian.org/bullseye/amd64/tor/download"
parse = urlparse(url) 
print(parse.query)