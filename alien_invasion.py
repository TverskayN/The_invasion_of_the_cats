import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

from spray import Spray
import game_function as gf



def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Cat Invasion")

    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")

    # Создание экземпляра для хранения игровой статистики и scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

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
        gf.check_events(ai_settings, screen, stats, sb, play_button, spray, cats, bullets)

        if stats.game_active:
            spray.update()

            # При каждом проходе цикла перерисовывается экран.
            gf.update_bullets(ai_settings, screen, stats, sb,  spray, cats, bullets)
            gf.update_cats(ai_settings, stats, screen, spray, cats, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, spray, cats, bullets, play_button)


run_game()
