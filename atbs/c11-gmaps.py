import pyperclip
import webbrowser
import sys

if len(sys.argv) < 2 :
    url = pyperclip.paste()
    url = url.split(' ')
else:
    url = sys.argv[1:]

gUrl = "https://www.google.com/maps/search/"

for item in url:
    gUrl = gUrl + "+" + item

webbrowser.open(gUrl)
