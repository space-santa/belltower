"""
Church bell simulator.

Every quarter hour the bell rings. At the hour, the bell also rings according to the hour.
The sense hat displays the appropriate colour for the season.
"""

import time

import pygame
import requests
from sense_hat import SenseHat

sense = SenseHat()

COLOURS = {
    "green": (0, 128, 43),
    "purple": (179, 0, 179),
    "red": (255, 0, 0),
    "white": (255, 255, 255),
    "pink": (255, 102, 255),
    "brown": (204, 153, 0),
}


def get_colour_name(date_string: str):
    response = requests.get(
        "https://sharp.clau.space/api/colour-of-the-day/",
        params={"date_str": date_string},
        timeout=10,
    )
    return response.json()["colour"]


def get_pixelmap(colour_name):
    cr = COLOURS["brown"]
    bg = COLOURS[colour_name]
    # fmt:off
    return [
        bg, bg, bg, cr, cr, bg, bg, bg,
        bg, bg, bg, cr, cr, bg, bg, bg,
        cr, cr, cr, cr, cr, cr, cr, cr,
        cr, cr, cr, cr, cr, cr, cr, cr,
        bg, bg, bg, cr, cr, bg, bg, bg,
        bg, bg, bg, cr, cr, bg, bg, bg,
        bg, bg, bg, cr, cr, bg, bg, bg,
        bg, bg, bg, cr, cr, bg, bg, bg,
    ]
    # fmt:on


def ring_bell():
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() is True:
        continue


def main():
    current_time = time.localtime()
    minutes = current_time.tm_min
    hour = current_time.tm_hour

    if hour > 12:
        hour -= 12

    colour_name = get_colour_name(
        f"{current_time.tm_year}-{current_time.tm_mon}-{current_time.tm_mday}"
    )
    pixels = get_pixelmap(colour_name)

    hour_times = 0

    if minutes == 15:
        times = 1
    elif minutes == 30:
        times = 2
    elif minutes == 45:
        times = 3
    elif minutes == 0:
        times = 4
        hour_times = hour
    else:
        # times = 1
        return

    if times:
        pixels.reverse()
        sense.set_pixels(pixels)
        pygame.mixer.init()
        pygame.mixer.music.load("assets/quarter_bell.wav")

        for _ in range(times):
            ring_bell()

        if hour_times:
            pygame.mixer.music.load("assets/hour_bell.wav")
            for _ in range(hour_times):
                ring_bell()

    sense.clear((0, 0, 0))


# Call the job function
main()
