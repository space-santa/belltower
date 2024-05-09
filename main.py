"""
Church bell simulator.

Every quarter hour the bell rings. At the hour, the bell also rings according to the hour.
The sense hat displays the appropriate colour for the season.
"""

import time

import pygame
from sense_hat import SenseHat

sense = SenseHat()

green = (0, 128, 43)
purple = (179, 0, 179)
red = (255, 0, 0)
white = (255, 255, 255)
pink = (255, 102, 255)

brown = (204, 153, 0)

bg = pink
cr = brown

# fmt:off
pixels = [
    bg,bg,bg,cr,cr,bg,bg,bg,
    bg,bg,bg,cr,cr,bg,bg,bg,
    cr,cr,cr,cr,cr,cr,cr,cr,
    cr,cr,cr,cr,cr,cr,cr,cr,
    bg,bg,bg,cr,cr,bg,bg,bg,
    bg,bg,bg,cr,cr,bg,bg,bg,
    bg,bg,bg,cr,cr,bg,bg,bg,
    bg,bg,bg,cr,cr,bg,bg,bg,
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

    hour_times = 0

    if minutes == 15:
        times = 1
    elif minutes == 30:
        times = 2
    elif minutes == 45:
        times = 3
    elif minutes == 0:
        times = 4 + hour  # Play additional sounds according to the hour
        hour_times = hour
    else:
        times = 1

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
