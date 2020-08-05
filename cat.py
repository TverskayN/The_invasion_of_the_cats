import pygame
from pygame.sprite import Sprite


class Cat(Sprite):
    """Класс, представляющий одного кота."""

    def __init__(self, ai_settings, screen):
        # Инициализирует кота и задает его начальное положение.
        super(Cat, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения кота и получение прямоугольника.
        self.image = pygame.image.load('images/cat.png')
        self.rect = self.image.get_rect()

        # Каждый новый кот появляется у правого края экрана.
        self.rect.x = self.ai_settings.screen_width - self.rect.width
        self.rect.y = 0
        # Сохранение точной позиции кота
        self.x = float(self.rect.x)



    def blitme(self):
        """Рисует кота в текущей позиции."""
        self.screen.blit(self.image, self.rect)



    def check_adges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True



    def update(self):
        """Перемещает пришельца вниз или вверх."""
        self.y += (self.ai_settings.cat_speed_factor * self.ai_settings.fleet_direction)
        self.rect.y = self.y

