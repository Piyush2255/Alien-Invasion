import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import Game_Stats
from button import Button
from scoreboard import Scoreboard

def run_game():

	pygame.init()
	game_settings=Settings()
	screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship=Ship(screen,game_settings)

	bullets=Group()

	aliens=Group()
	gf.create_fleet(aliens,screen,game_settings,ship)

	stats=Game_Stats(game_settings)

	play_button=Button(screen,"PLAY")
	sb=Scoreboard(game_settings,screen,stats)

	while True:

		gf.check_events(ship,bullets,screen,game_settings,stats,play_button,aliens,sb)
		if stats.game_active:
			ship.update()
			bullets.update()
			gf.update_bullets(bullets,aliens,screen,game_settings,ship,stats,sb)
			gf.update_alien(aliens,ship,bullets,game_settings,stats,screen,sb)
			gf.check_fleet_edges(game_settings,aliens)
			
		gf.update_screen(game_settings,ship,screen,bullets,aliens,stats,play_button,sb)

print("Loading....")
run_game()