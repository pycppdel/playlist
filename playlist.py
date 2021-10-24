import keyboard
import time
import requests
import re
time.sleep(2)

findstring = r"<p>(.*)</p>"

url = "https://pycppdel.github.io/playlist/"

playlist = []

text = requests.get(url).content
text = text.split(b"\n")
for el in text:

    matched = re.search(findstring, str(el))
    if matched:
        playlist.append(matched.groups()[0])


time.sleep(2)
for el in playlist:
    keyboard.write(";;play "+el)
    keyboard.press("enter")
    time.sleep(3.2)
