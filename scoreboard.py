import pygame.font
from pygame.sprite import Group

from spray import Spray

class Scoreboard():
    """Класс для вывода игровой информации"""
    def __init__(self, ai_settings, screen, stats):
        """Инициализирует атрибуты подсчета очков."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # Настройки шрифта для вывода счета.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка изображений сетов.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_sprays()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        rounder_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounder_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                             self.ai_settings.bg_color)
        # Вывод счета в правой верхней части экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Выводит счет и уровень на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.sprays.draw(self.screen)

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        # Рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Преобразует уровень в графическое изображение."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                            self.ai_settings.bg_color)
        # Уровень выводится под текущим счетом.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_sprays(self):
        """Сообщает количество оставшихся кораблей."""
        self.sprays = Group()
        for spray_number in range(self.stats.sprays_left):
            spray = Spray(self.ai_settings, self.screen)
            spray.rect.x = 10 + spray_number * spray.rect.width
            spray.rect.y = 10
            self.sprays.add(spray)

