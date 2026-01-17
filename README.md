Note that on a RPi 2b I had to install all the requirements line by line to make it work.
Probably something with not enough memory. My guess, I didn't do any investigation.

```
# Essentials
sudo apt install sense-hat python3-pygame pulseaudio python3-fastapi python3-requests

# We want to run this using cron
crontab -e
# At the top of the cron file we need to set the XDG_RUNTIME_DIR for sound to happen.
XDG_RUNTIME_DIR=/run/usr/1000
# Every 15 minutes the bell rings.
0,15,30,45 * * * * /usr/bin/python3 /home/space/belltower/cron_triggered.py > tower.log
```

```
cp belltower.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable belltower
# systemctl status belltower
```

```
cp belltower_joystick.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable belltower_joystick
# systemctl status belltower_joystick
```
