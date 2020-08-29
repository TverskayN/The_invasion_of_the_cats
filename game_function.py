import sys
from time import sleep

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


def check_events(ai_settings, screen, stats, play_button, spray, cats, bullets):
    """Обрабатывает нажатие клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, spray, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, spray)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, spray,
                              cats, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, spray, cats, bullets, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)
        # Сброс игровой статистики.
        stats.reset_stats()
        stats.game_active = True

        # Очистка списков пришельцев и пуль.
        cats.empty()
        bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        create_fleet(ai_settings, screen, spray, cats)
        spray.center_spray()


def update_screen(ai_settings, screen, stats, spray, cats, bullets, play_button):
    """Обновляет изображение на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)

    # Все пули выводятся позади пульвика и кошек.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    spray.blitme()
    cats.draw(screen)

    # Кнопка Play отображается в том случае, если игра неативна.
    if not stats.game_active:
        play_button.draw_button()
        pygame.mouse.set_visible(True)

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


def update_bullets(ai_settings, screen, spray, cats,  bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиции пуль.
    bullets.update()

    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.x > ai_settings.screen_width:
            bullets.remove(bullet)

    check_bullet_cat_collisions(ai_settings, screen, spray, cats, bullets)

def check_bullet_cat_collisions(ai_settings, screen, spray, cats, bullets):
    """Обработка коллизий пуль с котами"""
    # Удаление пуль и котов, учавствующих в коллизях.
    collisions = pygame.sprite.groupcollide(bullets, cats, True, True)
    if len(cats) == 0:
        # Уничтожение существующих пуль и создание нового флота.
        bullets.empty()
        create_fleet(ai_settings, screen, spray, cats)

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

def create_fleet(ai_settings: object, screen: object, spray: object, cats: object) -> object:
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


def spray_hit(ai_settings, stats, screen, spray, cats, bullets):
    """Обрабатывает столкновение пульвика с котами."""
    if stats.sprays_left > 0:
        # Уменьшение spray_left.
        stats.sprays_left -= 1

        # Очистка списков котов и пуль.
        cats.empty()
        bullets.empty()

        # Создание нового флота и размещения пульвика в в центре.
        create_fleet(ai_settings, screen, spray, cats)
        spray.center_spray()

        # Пауза.
        sleep(0.5)

    else:
        stats.game_active = False

def check_cats_left(ai_settings, stats, screen, spray, cats, bullets):
    """Проверяет, добрались ли пришельцы до левого края экрана."""
    screen_rect = screen.get_rect()
    for cat in cats.sprites():
        if cat.rect.left <= screen_rect.left:
            # Происходит то же, что и при столкновении с кораблем.
            spray_hit(ai_settings, stats, screen, spray, cats, bullets)
            break


def update_cats(ai_settings, stats, screen, spray, cats, bullets):
    """Проверяет, достиг ли флот края экрана,
    после чего обновляет позиции всех котов во фолоте."""
    check_fleet_edges(ai_settings, cats)
    cats.update()

    # Проверка коллизий "кот-пульвик".
    if pygame.sprite.spritecollideany(spray, cats):
        spray_hit(ai_settings, stats, screen, spray, cats, bullets)
    # Проверка котов, добравшихся до нижнего левого края экрана.
    check_cats_left(ai_settings, stats, screen, spray, cats, bullets)