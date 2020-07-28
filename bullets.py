import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self,screen,ship,game_settings):

		super().__init__()
		self.screen=screen

		self.rect=pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)

		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top

		self.y=float(ship.rect.y)

		self.colour=game_settings.bullet_colour
		self.speed_factor=game_settings.bullet_speed_factor

	def update(self):

		self.y-=self.speed_factor
		self.rect.y=self.y

	def draw_bullet(self):

		pygame.draw.rect(self.screen,self.colour,self.rect)