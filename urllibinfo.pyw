import urllib.request # to connect python through internet

x =urllib.request.urlopen("https://www.google.com")
print(x.read())
