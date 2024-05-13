```
# Essentials
sudo apt install sense-hat python3-pygame pulseaudio

# We want to run this using cron
crontab -e
# At the top of the cron file we need to set the XDG_RUNTIME_DIR for sound to happen.
XDG_RUNTIME_DIR=/run/usr/1000
# Every 15 minutes the bell rings.
*/15 * * * * /usr/bin/python3 /home/uruser/belltower/main.py
```
