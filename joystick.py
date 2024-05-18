from signal import pause

import requests
from sense_hat import ACTION_PRESSED, SenseHat

# Create a SenseHat object
sense = SenseHat()


def ring():
    requests.get(
        "http://localhost:8456/api/ring/",
        params={"times": 4, "hour_times": 2, "volume": 0.2},
        timeout=30,
    )


# Define the functions to run when joystick events occur
def pushed(event):
    if event.action != ACTION_PRESSED:
        ring()


# Associate the functions with joystick events
sense.stick.direction_up = pushed
sense.stick.direction_down = pushed
sense.stick.direction_left = pushed
sense.stick.direction_right = pushed
sense.stick.direction_middle = pushed

# Wait for joystick events
pause()
