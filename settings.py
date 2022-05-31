class Settings:
    """A Class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (0,0,0) #RGB

        #Ship
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet
        self.bullet_speed = 1.5
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (148, 0, 52) #RGB warna fuchsia jelly
        self.bullets_allowed = 2

        #Alien
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # 1 kanan, -1 kiri
        self.fleet_direction = 1

        #game speeds
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 10
        self.bullet_speed = 5
        self.alien_speed = 5
        self.fleet_direction = -1
        #Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and aliens point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)