
class Settings:
    """Класс для хранения всех настроек игры."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 768
        self.bg_color = (200, 230, 230)
        # Настройки пульвика
        self.spray_speed_factor = 1.5
        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 6
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
