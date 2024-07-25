import pygame


def play_battle_theme():
    pygame.mixer.music.load("music/battle.ogg")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1, fade_ms=2000)


def play_game_over_theme():
    pygame.mixer.music.load("music/game_over.ogg")
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(loops=-1, fade_ms=2000)