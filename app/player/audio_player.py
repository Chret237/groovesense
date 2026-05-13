import pygame


pygame.mixer.init()

def play_song(path):

    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        return True
    except pygame.error as e:
        print(f"Impossible de charger {path}: {e}")
        return False

def stop_song():

    pygame.mixer.music.stop()

def pause_song():

    pygame.mixer.music.pause()

def resume_song():

    pygame.mixer.music.unpause()

def is_playing():

    return pygame.mixer.music.get_busy()

