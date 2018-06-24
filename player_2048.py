from game_2048 import *
import math



directions = ['u', 'd', 'l', 'r']

def play_with_AI(nn):

	game = Game()

	playing = True

	play = 1

	#print '\n\n------------------\n--------------------\n'

	while playing:

		entrance = np.copy(game.board)
		entrance = entrance.reshape(-1)
		#print game.board

		#print 'play ' + str(play)
		play += 1

		for index in range(len(entrance)):
			if entrance[index] != 0:
				entrance[index] = math.log(entrance[index], 2)

		maior = 0
		saida = nn.sactivate(entrance)
		for i in range(len(saida)):
			if saida[i] > saida[maior]:
				maior = i

		movement = directions[maior]

		#print movement

		#print 'O meu movimento foi: ' + movement



		if not game.apply_command(movement):
			#print '++++++++++++++++++\n+++++++++++++++++\n\n\n'
			return float(game.score)

		game.new_round()


def play_with_user():
	while True:

		print '\n --------------------'
		print game.board
		game.user_play()
		print '\n'
		print game.board

		print 'score: ' + str(game.score)
		game.new_round()
