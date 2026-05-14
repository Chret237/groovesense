import time
import pygame

def crossfade_transition(
    duration=5
):

    steps = 20

    delay = duration / steps

    for i in range(steps):

        volume = 1 - (i / steps)

        pygame.mixer.music.set_volume(
            volume
        )

        time.sleep(delay)

channel_a = pygame.mixer.Channel(0)

channel_b = pygame.mixer.Channel(1)