import sys

import pygame
from bullet import Bullet
from cat import Cat


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
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, spray, cats, bullets):
    """Обновляет изображение на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)

    # Все пули выводятся позади пульвика и кошек.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    spray.blitme()
    cats.draw(screen)
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


def update_bullets(ai_settings, cats,  bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиции пуль.
    bullets.update()

    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.x > ai_settings.screen_width:
            bullets.remove(bullet)

    # Проверка попаданий в котов.
    # При обнаружении попаданий удалить пулю и кота.
    collisions = pygame.sprite.groupcollide(bullets, cats, True, True)

def get_number_cat_y(ai_settings, cat_height):
    """Вычисляет количество котов в столбце."""
    available_spase_y = ai_settings.screen_height - 2 * cat_height
    number_cats_y = int(available_spase_y / (2 * cat_height))
    return number_cats_y

def get_number_columns(ai_settings, cat_width, spray_width):
    """Вычисляет количество котов в ряду."""
    available_space_x = ai_settings.screen_width - 3 * cat_width - spray_width
    number_columns = int(available_space_x / (2 * cat_width))
    return number_columns

def create_cat(ai_settings, screen, cats, cat_number, column_number):
    """Создает кота и размещает его в ряду."""
    cat = Cat(ai_settings, screen)
    cat_height = cat.rect.height
    cat.y = cat_height + 2 * cat_height * cat_number
    cat.rect.y = cat.y
    cat.rect.x = ai_settings.screen_width - cat.rect.width - 2 * cat.rect.width * column_number
    cats.add(cat)

def create_fleet(ai_settings, screen, spray, cats):
    """Создаем флот котов"""
    # Создание кота и вычисление количества котов в столбце.
    # Интервал между соседними котами равен высоте одного кота.

    cat = Cat(ai_settings, screen)
    number_cats_y = get_number_cat_y(ai_settings, cat.rect.height)
    number_columns = get_number_columns(ai_settings, cat.rect.width, spray.rect.width)

    # Создание первого столбца котов
    for column_number in range(number_columns):
        for cat_number in range(number_cats_y):
            create_cat(ai_settings, screen, cats, cat_number, column_number)

def check_fleet_edges(ai_settings, cats):
    """Реагирует на достижение пришельцем края экрана."""
    for cat in cats.sprites():
        if cat.check_adges():
            change_fleet_direction(ai_settings, cats)
            break

def change_fleet_direction(ai_settings, cats):
    """Перемещает влево весь флот и меняет направление флота."""
    for cat in cats.sprites():
        cat.rect.x -= ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_cats(ai_settings, cats):
    """Проверяет, достиг ли флот края экрана,
    после чего обновляет аозиции всех котов во фолоте."""
    check_fleet_edges(ai_settings, cats)
    cats.update()