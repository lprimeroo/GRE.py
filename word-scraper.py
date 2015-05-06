import requests
from bs4 import BeautifulSoup

count = 0
r = requests.get("https://quizlet.com/58647605/kaplan-900-flash-cards/")
soup = BeautifulSoup(r.content)
for word in soup.find_all("div"):
	id = word.get("data-id") 
	if id is not None:
		count = count + 1
		print id
print "Count : " + str(count) 