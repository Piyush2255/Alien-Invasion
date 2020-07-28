import sys
import pygame
from bullets import Bullet
from alien import Alien
from math import *
from time import sleep

def check_keydown_events(event,ship,screen,game_settings,bullets):

	if event.key==pygame.K_RIGHT:
		ship.moving_right=True

	elif event.key==pygame.K_LEFT:
		ship.moving_left=True

	#elif event.key==pygame.K_UP:
	#	ship.moving_up=True

	#elif event.key==pygame.K_DOWN:
	#	ship.moving_down=True

	elif event.key==pygame.K_SPACE:
		fire_bullets(bullets,screen,ship,game_settings)	

def check_keyup_events(event,ship):

	if event.key==pygame.K_RIGHT:
		ship.moving_right=False

	elif event.key==pygame.K_LEFT:
		ship.moving_left=False

	#elif event.key==pygame.K_UP:
	#	ship.moving_up=False

	#elif event.key==pygame.K_DOWN:
	#	ship.moving_down=False

	elif event.key==pygame.K_ESCAPE:
		sys.exit()

def check_events(ship,bullets,screen,game_settings,stats,play_button,aliens,sb):

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()

		elif event.type==pygame.KEYDOWN:
			check_keydown_events(event,ship,screen,game_settings,bullets)	

		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)

		elif event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_button(stats,play_button,mouse_x,mouse_y,aliens,screen,game_settings,ship,bullets,sb)

def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,screen,game_settings,ship,bullets,sb):

	button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		pygame.mouse.set_visible(False)
		stats.game_active=True
		game_settings.initialize_dynamic_settings()
		stats.reset_stats()
		sb.prep_score()
		sb.prep_level()
		sb.prep_lives()

		aliens.empty()
		bullets.empty()

		create_fleet(aliens,screen,game_settings,ship)
		ship.center_ship()

def update_screen(game_settings,ship,screen,bullets,aliens,stats,play_button,sb):

	screen.fill(game_settings.bg_colour)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	aliens.draw(screen)
	sb.show_score()

	if not stats.game_active:
		play_button.draw_button()

	pygame.display.flip()

def update_bullets(bullets,aliens,screen,game_settings,ship,stats,sb):

	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)

	check_bullet_collision(bullets,aliens,screen,game_settings,ship,stats,sb)

def check_bullet_collision(bullets,aliens,screen,game_settings,ship,stats,sb):

	collisons=pygame.sprite.groupcollide(bullets,aliens,True,True)

	if collisons:
		for alien in collisons.values():
			stats.score+=game_settings.alien_points*len(alien)
			sb.prep_score()
		check_high_score(stats,sb)

	if len(aliens)==0:
		bullets.empty()
		create_fleet(aliens,screen,game_settings,ship)
		game_settings.increase_speed()
		stats.level+=1
		sb.prep_level()

def check_high_score(stats,sb):

	if stats.score>stats.high_score:
		stats.high_score=stats.score
		sb.prep_high_score()
		with open("high_score.txt",'w') as high_score_file:
			high_score_file.write(str(stats.high_score))

def fire_bullets(bullets,screen,ship,game_settings):

	if len(bullets)<game_settings.allowed_bullets:
		new_bullet=Bullet(screen,ship,game_settings)
		bullets.add(new_bullet)

def get_total_rows(game_settings,ship_height,alien_height):

	available_space=game_settings.screen_height-ship_height-3*alien_height
	total_rows=int(available_space/(2*alien_height))
	return total_rows

def get_total_aliens(alien_width,game_settings):

	available_space=game_settings.screen_width-2*alien_width
	total_aliens=ceil(available_space/(2*alien_width))
	return total_aliens

def create_new_alien(screen,alien_width,alien_number,aliens,row_number,game_settings):

	alien=Alien(screen,game_settings)
	alien.x+=2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
	aliens.add(alien)

def create_fleet(aliens,screen,game_settings,ship):

	alien=Alien(screen,game_settings)
	alien_width=alien.rect.width
	total_aliens=get_total_aliens(alien_width,game_settings)
	total_rows=get_total_rows(game_settings,ship.rect.height,alien.rect.height)
	
	for row_number in range(total_rows):
		for alien_number in range(total_aliens):

			create_new_alien(screen,alien_width,alien_number,aliens,row_number,game_settings)		

def ship_hit(ship,aliens,bullets,game_settings,stats,screen,sb):

	if stats.ships_left>0:

		stats.ships_left-=1;

		bullets.empty()
		aliens.empty()
		sb.prep_lives()

		create_fleet(aliens,screen,game_settings,ship)
		ship.center_ship()

		sleep(0.5)

	else:
		stats.game_active=False
		pygame.mouse.set_visible(True)

def update_alien(aliens,ship,bullets,game_settings,stats,screen,sb):

	#alien=Alien(screen,game_settings)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ship,aliens,bullets,game_settings,stats,screen,sb)

	check_alien_bottom(screen,ship,aliens,game_settings,bullets,stats,sb)

def change_fleet_direction(aliens,game_settings):

	for alien in aliens.sprites():
		alien.rect.y+=game_settings.drop_speed

	if game_settings.fleet_direction==1:
		game_settings.fleet_direction=-1

	else:
		game_settings.fleet_direction=1

def check_fleet_edges(game_settings,aliens):

	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(aliens,game_settings)
			break

def check_alien_bottom(screen,ship,aliens,game_settings,bullets,stats,sb):

	screen_rect=screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom>=screen_rect.bottom:
			ship_hit(ship,aliens,bullets,game_settings,stats,screen,sb)
			break