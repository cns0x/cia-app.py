#!/usr/bin/python3

import requests
from sys import argv


for i in range(int(argv[1]),int(argv[2])):
	payload = {'telefon': "0"+str(i)}
	
	r = requests.post("http://www.beniarayan.kim/sorgulama.php", data=payload)
	r.encoding = "utf-8"
	
	if r.text.find("BU NUMARA KAYITLI DEGILDIR.") == -1:
		print(payload['telefon'] + " - " + r.text[22:r.text.find("</font>")])
