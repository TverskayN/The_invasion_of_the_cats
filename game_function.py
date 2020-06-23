import sys

import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, spray, bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_DOWN:
        # Переместить корабль вниз при удержании клавиши.
        spray.moving_down = True
    elif event.key == pygame.K_UP:
        # Переместить корабль вверх при удержании клавиши.
        spray.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, spray, bullets)


def fire_bullet(ai_settings, screen, spray, bullets):
    """Выпускает пулю, если максимум еще не достигнут."""
    # Создание новой пули и включение ее в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, spray)
        bullets.add(new_bullet)


def check_keyup_events(event, spray):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_DOWN:
        spray.moving_down = False
    elif event.key == pygame.K_UP:
        spray.moving_up = False


def check_events(ai_settings, screen, spray, bullets):
    """Обрабатывает нажатие клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, spray, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spray)


def update_screen(ai_settings, screen, spray, bullets):
    """Обновляет изображение на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)

    # Все пули выводятся позади пульвика и кошек.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    spray.blitme()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


def update_bullets(ai_settings, bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиции пуль.
    bullets.update()

    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.x > ai_settings.screen_width:
            bullets.remove(bullet)
