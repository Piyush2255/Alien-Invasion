import pygame
from pygame.sprite import Sprite

class Lives(Sprite):

	def __init__(self):

		super().__init__()
		#self.screen=screen
		#self.screen_rect=self.screen.get_rect()
		#self.game_settings=game_settings
		self.image=pygame.image.load('C:\\Users\\HP\\Desktop\\Aliens\\Images\\rocket3.bmp')
		self.rect=self.image.get_rect()