import pygame.font
from pygame.sprite import Group
from lives import Lives

class Scoreboard():

	def __init__(self,game_settings,screen,stats):

		self.screen=screen
		self.screen_rect=self.screen.get_rect()
		self.game_settings=game_settings
		self.stats=stats

		self.text_colour=(10,10,10)
		self.font=pygame.font.SysFont(None,48)

		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_lives()

	def prep_score(self):

		rounded_score=round(self.stats.score,-1)
		score_str="{:,}".format(rounded_score)
		self.score_image=self.font.render(score_str,True,self.text_colour,self.game_settings.bg_colour)

		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=10

	def show_score(self):

		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.lives.draw(self.screen)

	def prep_high_score(self):

		high_score=round(self.stats.high_score,-1)
		high_score_str="{:,}".format(high_score)
		self.high_score_image=self.font.render(high_score_str,True,self.text_colour,self.game_settings.bg_colour)

		self.high_score_rect=self.high_score_image.get_rect()
		self.high_score_rect.centerx=self.screen_rect.centerx
		self.high_score_rect.top=10

	def prep_level(self):

		self.level_image=self.font.render(str(self.stats.level),True,self.text_colour,self.game_settings.bg_colour)

		self.level_rect=self.level_image.get_rect()
		self.level_rect.right=self.score_rect.right
		self.level_rect.top=self.score_rect.bottom

	def prep_lives(self):

		self.lives=Group()
		for life_number in range(self.stats.ships_left):
			life=Lives()
			life.rect.x=10+life_number*life.rect.width+life_number*10
			life.rect.y=10
			self.lives.add(life)