#!/usr/bin/python3


import urllib.request
with request.get('https://alx-intranet.hbtn.io/status') as response:
	data = response.raise_for_status()
	print(data)
