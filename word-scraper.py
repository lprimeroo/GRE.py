import requests
import os
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

rest_command = """'display notification "{}" with title "{}"'""".format(meaning[randint(0,737)],word[(randint(0,737))])
os.system("osascript -e "+ rest_command)
