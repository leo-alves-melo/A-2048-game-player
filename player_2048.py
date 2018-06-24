from game_2048 import *
import math

game = Game()

directions = ['u', 'd', 'l', 'r']

def play_with_AI(nn):

	playing = True

	while playing:

		entrance = game.board.reshape(-1)

		for index in range(len(entrance)):
			if entrance[index] != 0:
				entrance[index] = math.log(entrance[index], 2)

		movement = directions[nn.predict(entrance)]

		if not game.apply_command(movement):
			return game.score


def play_with_user():
	while True:

		print '\n --------------------'
		print game.board
		game.user_play()
		print '\n'
		print game.board

		print 'score: ' + str(game.score)
		game.new_round()
