import pygame

class Ship():

	def __init__(self,screen,game_settings):

		self.screen=screen
		self.image=pygame.image.load('C:\\Users\\HP\\Desktop\\Aliens\\Images\\rocket2.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()
		self.moving_right=False
		self.moving_left=False
		#self.moving_up=False
		#self.moving_down=False
		self.game_settings=game_settings
		self.speed_factor=self.game_settings.ship_speed_factor
		
		self.rect.bottom=self.screen_rect.bottom
		self.rect.centerx=self.screen_rect.centerx

		self.center=float(self.rect.centerx)
		#self.bottom=float(self.rect.bottom)

	def blitme(self):

		self.screen.blit(self.image,self.rect)

	def update(self):

		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.speed_factor

		elif self.moving_left and self.rect.left>0:
			self.center-=self.speed_factor

		#elif self.moving_up and self.rect.top>self.screen_rect.top:
		#	self.bottom-=self.speed_factor

		#elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
		#	self.bottom+=self.speed_factor

		self.rect.centerx=self.center
		#self.rect.bottom=self.bottom
		self.speed_factor=self.game_settings.ship_speed_factor

	def center_ship(self):

		self.rect.centerx=self.screen_rect.centerx
		self.center=float(self.rect.centerx)