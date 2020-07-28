import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

	def __init__(self,screen,game_settings):

		super().__init__()
		self.screen=screen
		self.game_settings=game_settings
		self.image=pygame.image.load('C:\\Users\\HP\\Desktop\\Aliens\\Images\\ufo3.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()

		self.rect.x=self.rect.width
		self.rect.y=self.rect.height

		self.x=float(self.rect.x)

	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self):

		self.x+=(self.game_settings.alien_speed_factor*self.game_settings.fleet_direction)
		self.rect.x=self.x

	def check_edges(self):

		if self.rect.right>=self.screen_rect.right:
			return True

		elif self.rect.left<=0:
			return True