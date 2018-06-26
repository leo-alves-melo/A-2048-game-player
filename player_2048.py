from game_2048 import *
import math



directions = ['u', 'd', 'l', 'r']

def play_with_AI(nn):

	average = 0.0

	for times in range(5):

		game = Game()

		playing = True

		while playing:

			entrance = np.copy(game.board)
			entrance = entrance.reshape(-1)

			for index in range(len(entrance)):
				if entrance[index] != 0:
					entrance[index] = math.log(entrance[index], 2)

			maior = 0
			saida = nn.sactivate(entrance)
			for i in range(len(saida)):
				if saida[i] > saida[maior]:
					maior = i

			movement = directions[maior]

			if not game.apply_command(movement):
				average += float(game.score)
				playing = False
			else:
				game.new_round()

	return average/5.0


def play_with_user():

	game = Game()

	while True:

		print '\n --------------------'
		print game.board
		game.user_play()
		print '\n'
		print game.board

		print 'score: ' + str(game.score)
		game.new_round()

#play_with_user()
