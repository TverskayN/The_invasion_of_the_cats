import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс сдля управления пулями, выпущенными кораблем."""
    def __init__(self, ai_settings, screen, spray):
        """Создает объект пули в текущей позиции корабля."""
        super().__init__()
        self.screen = screen

        # Создание пули в позиции (0, 0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = spray.rect.centerx * 2
        self.rect.top = spray.rect.top + 8

        # Позиция пули хранится в вещественном формате.
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Перемещает пулю вправо по экрану."""
        # Обновление позиции пули в вещественом формате.
        self.x += self.speed_factor
        # Обновление позиции прямоугольника.
        self.rect.x = self.x

    def draw_bullet(self):
        """Вывод пули на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)