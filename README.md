#GRE.py

A Python script that sends OSX notifications at regular intervals . Notifications include words and their
meanings scraped from Kaplan's 900 most common GRE vocabulary website.

##Installation

###Manually Running Script :
```
git clone https://github.com/saru95/GRE.py
cd GRE.py
python gre.py
```
###Automating Script every time your Mac Starts :
```
git clone https://github.com/saru95/GRE.py
cd GRE.py
mv gre.py /Users/username/
sudo mv com.username.gre.plist /Library/LaunchAgents
```

###Further Installation Notes:
1. In `com.username.gre.plist` file, change `username` with your Mac's username including the file name.
2. Value under `StartInterval` is the time interval in seconds after which the script should automatically execute.
    Change it according to your prefence .
