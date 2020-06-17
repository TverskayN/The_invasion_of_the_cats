import pygame


class Spray:

    """Класс реализующий действия пульверизатора (пульвика)."""

    def __init__(self, ai_setting, screen):
        # Инициализирует пульвелизатор и задает его начальное положение.
        self.screen = screen
        self.ai_setting = ai_setting
        # Загрузка изображения пульвика и получение прямоугольника.
        self.image = pygame.image.load('images/spray.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый пульвик появляется у левого края экрана.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        # Сохранение вещественной координаты центра пульвика
        self.center = float(self.rect.centery)
        # Флаг перемещения
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Обновляет позицию пульвика с учетом флагов."""
        # Обновляем атрибут center, не rect.
        if self.moving_down and self.rect.centery < 2 * self.screen_rect.centery:
            self.rect.centery += self.ai_setting.spray_speed_factor
        elif self.moving_up and self.rect.centery > 0:
            self.rect.centery -= self.ai_setting.spray_speed_factor
        # Обновление атрибута rect на основании self.center.

    def blitme(self):
        """Рисует пульвик в текущей позиции."""
        self.screen.blit(self.image, self.rect)
