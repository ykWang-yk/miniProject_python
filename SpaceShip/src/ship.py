import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载图像并获取外界举行
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #每搜新的飞船放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        #飞船的属性中存储小树枝
        self.x = float(self.rect.x)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #调整飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #更新位置
        self.rect.x = self.x

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)