class Game_Stats():

	def __init__(self,game_settings):

		self.game_settings=game_settings
		self.game_active=False
		with open("high_score.txt") as high_score_file:
			high_score=high_score_file.read()
			high_score1=high_score.strip()
			self.high_score=int(high_score1)
		self.reset_stats()

	def reset_stats(self):

		self.ships_left=self.game_settings.ship_limit
		self.score=0
		self.level=1