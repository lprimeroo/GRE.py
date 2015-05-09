#GRE.py

A Python script that sends OSX notifications at regular intervals . Notifications include words and their
meanings scraped from Kaplan's 900 most common GRE vocabulary website.



##Installation

```
git clone https://github.com/saru95/GRE.py
cd GRE.py
```
###Do Not Skip :
Before executing `install.sh`, change all the `username` in `com.username.gre.plist` file to you Mac's username . Do the same for the file name , i.e, change `com.username.gre.plist` to `com.your_username.gre.plist` and all the username inside this file .

Once Done,
```
chmod +x install.sh
./install.sh
```

Now, you're good to go with a new word popping up in your notifications every 45 minutes . Time interval can be modified in`gre.py` file .



