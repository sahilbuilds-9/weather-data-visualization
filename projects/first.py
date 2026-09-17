from urllib.request import urlopen

# Download a web page
with urlopen("https://api.github.com") as response:
	print(response.status)  # Should print 200