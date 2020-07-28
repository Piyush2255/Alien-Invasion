class Settings():

	def __init__(self):

		self.screen_width=1500
		self.screen_height=750
		self.bg_colour=(255,255,255)

		self.ship_limit=3

		self.bullet_height=20
		self.bullet_width=5
		self.bullet_colour=(60,60,60)
		self.allowed_bullets=3

		self.drop_speed=10

		self.speedup_scale=1.2
		self.score_scale=1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):

		self.ship_speed_factor=2
		self.bullet_speed_factor=3
		self.alien_speed_factor=1.8
		self.fleet_direction=1
		self.alien_points=50

	def increase_speed(self):

		self.ship_speed_factor*=self.speedup_scale
		self.bullet_speed_factor*=self.speedup_scale
		self.alien_speed_factor*=self.speedup_scale
		self.alien_points=int(self.alien_points*self.score_scale)