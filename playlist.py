
import time
import requests
import re
import pynput

keyboard = pynput.keyboard.Controller()


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
    keyboard.type(";;play "+el)
    keyboard.press(pynput.keyboard.Key.enter)
    keyboard.release(pynput.keyboard.Key.enter)
    time.sleep(3.2)

keyboard.type(";;repeat all")
keyboard.press(pynput.keyboard.Key.enter)
keyboard.release(pynput.keyboard.Key.enter)
