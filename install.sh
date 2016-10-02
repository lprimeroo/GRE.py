username=$(whoami)
mv gre.py ~$username/
sudo mv com.$username.gre.plist /Library/LaunchAgents
sudo chmod 600 /Library/LaunchAgents/com.$username.gre.plist 
sudo chown root /Library/LaunchAgents/com.$username.gre.plist 
chmod +x ~$username/gre.py
sudo launchctl load /Library/LaunchAgents/com.$username.gre.plist
