#! /usr/bin/python

import requests
import os
import time
from random import randint
from bs4 import BeautifulSoup

word = []
meaning = []

r = requests.get("https://quizlet.com/58647605/kaplan-900-flash-cards/")
content = BeautifulSoup(r.content)
for words in content.findAll('span', attrs={'class':'qWord'}):
	word.append(words.text.encode("utf-8"))

for word_meanings in content.findAll('span', attrs={'class':'qDef'}):
	meaning.append(word_meanings.text.encode("utf-8"))

while(True):
	index = randint(0,737)
	rest_command = """'display notification "{}" with title "{}" sound name "Glass.aiff"'""".format(meaning[index],word[index])
	os.system("osascript -e "+ rest_command)
	time.sleep(2700)
