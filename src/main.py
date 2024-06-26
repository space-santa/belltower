"""
Church bell simulator.

Every quarter hour the bell rings. At the hour, the bell also rings according to the hour.
The sense hat displays the appropriate colour for the season.
"""

import os
import time

import pygame
import requests

from src.utils import determine_rings

try:
    from sense_hat import SenseHat

    sense = SenseHat()
except OSError as e:
    print(e)
    from src.sense_mock import SenseMock

    sense = SenseMock()

base_path = os.path.dirname(os.path.realpath(__file__))

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


async def main(times=0, hour_times=0, volume=0.2):
    current_time = time.localtime()

    if times == 0:
        times, hour_times = determine_rings()

    if times:
        colour_name = get_colour_name(
            f"{current_time.tm_year}-{current_time.tm_mon}-{current_time.tm_mday}"
        )
        pixels = get_pixelmap(colour_name)
        pixels.reverse()
        sense.set_pixels(pixels)
        pygame.mixer.init()
        quarter_bell_path = os.path.join(base_path, "assets", "quarter_bell.wav")
        pygame.mixer.music.load(quarter_bell_path)
        pygame.mixer.music.set_volume(volume)

        for _ in range(times):
            ring_bell()

        if hour_times:
            hour_bell_path = os.path.join(base_path, "assets", "hour_bell.wav")
            pygame.mixer.music.load(hour_bell_path)
            for _ in range(hour_times):
                ring_bell()

        time.sleep(1)
    sense.clear((0, 0, 0))


# Call the job function
if __name__ == "__main__":
    main()
