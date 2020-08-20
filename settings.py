
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
        self.spray_limit = 3
        # Параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 6
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Настройки котов
        self.cat_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вниз; а -1 - вверх
        self.fleet_direction = 1
