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

    # Запуск нового цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, spray, bullets)

        spray.update()
        # При каждом проходе цикла перерисовывается экран.
        bullets.update()

        # Удаление пуль, вышедших за край экрана.
        for bullet in bullets.copy():
            if bullet.x > ai_settings.screen_width:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, spray, bullets)


run_game()
