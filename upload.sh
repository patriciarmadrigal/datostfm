
eval "$(ssh-agent -s)"
ssh-add /home/pi/.ssh/github
cd /home/pi/TFMPatri

git add --all
git commit -m "daily crontab backup `date`"
git push origin master
