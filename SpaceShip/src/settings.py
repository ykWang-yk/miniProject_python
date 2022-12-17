class Settings:
    """管理所有类属性"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.ship_limit = 3
        #子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        #外星人设置
        self.fleet_drop_speed = 10

        #加快游戏节奏
        self.speedup_scale = 1.1
        #提高分数
        self.score_scale = 1.5

        self.initialize_dynamic_setting()
        #积分
        self.alien_points = 50

    def initialize_dynamic_setting(self):
        #初始化变化的配置
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        # direction为1代表向右 -1代表向左
        self.fleet_direction = 1

    def increase_speed(self):
        #提高速度
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

        print(self.alien_points)

