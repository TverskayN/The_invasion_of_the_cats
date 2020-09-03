
class Settings:
    """Класс для хранения всех настроек игры."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (200, 230, 230)
        # Настройки пульвика
        self.spray_limit = 3
        # Параметры пули
        self.bullet_width = 6
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Настройки котов
        self.fleet_drop_speed = 10
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости котов
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.spray_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.cat_speed_factor = 1
        # fleet_direction = 1 обозначает движение вниз; а -1 - вверх
        self.fleet_direction = 1
        # Подсчет очков
        self.cat_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость котов."""
        self.spray_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.cat_speed_factor *= self.speedup_scale
        self.cat_points = int(self.cat_points * self.score_scale)
        print(self.cat_points)
