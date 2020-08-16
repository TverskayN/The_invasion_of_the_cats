import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from spray import Spray
import game_function as gf



def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Cat Invasion")

    # Создание пульвелизатора.
    spray = Spray(ai_settings, screen)

    # Создание группы для хранения пуль.
    bullets = Group()

    # Создание кота
    cats = Group()

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, spray, cats)

    # Запуск нового цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, spray, bullets)

        spray.update()

        # При каждом проходе цикла перерисовывается экран.
        gf.update_bullets(ai_settings, cats, bullets)
        gf.update_cats(ai_settings, cats)
        gf.update_screen(ai_settings, screen, spray, cats, bullets)


run_game()
