# cia-app.py
Python script for collecting names from caller ID app [CIA](http://cia-app.com/)

##Requirements:
* Python3
* requests module ([Download](http://docs.python-requests.org/en/latest/user/install/))

##Usage:
Script takes 2 turkish mobile numbers(without 0) as arguments. As a result, numbers that are registered to cia-app between these two arguments will be shown on the screen. First mobile number must be bigger than the second number.

./cia-app.py 5XXXXXXXXX 5YYYYYYYYY

To delete your number from cia-app database, visit [this](http://cia-app.com/self-service/delist-number/) site.

![](http://cdn.meme.am/instances2/500x/1139657.jpg)
