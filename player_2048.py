from game_2048 import *
import math
from neat import config, population, chromosome, genome, visualize
from neat.nn import nn_pure as nn
from checkpoint import Checkpointer

import sys

#print 'pegando'
#pop = Checkpointer.restore_checkpoint(sys.argv[1])

#print 'peguei'

#winner = pop.stats[0][-1]


# Let's check if it's really solved the problem
#print('\nBest network output:')
#brain = nn.create_ffphenotype(winner)



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


def read_board():
	print 'Linha 1'
	a11 = int(raw_input())
	a12 = int(raw_input())
	a13 = int(raw_input())
	a14 = int(raw_input())

	print 'Linha 2'
	a21 = int(raw_input())
	a22 = int(raw_input())
	a23 = int(raw_input())
	a24 = int(raw_input())

	print 'Linha 3'
	a31 = int(raw_input())
	a32 = int(raw_input())
	a33 = int(raw_input())
	a34 = int(raw_input())

	print 'Linha 4'
	a41 = int(raw_input())
	a42 = int(raw_input())
	a43 = int(raw_input())
	a44 = int(raw_input())

	return np.array([[a11, a12, a13, a14],[a21, a22, a23, a24],[a31, a32, a33, a34],[a41, a42, a43, a44]])


def input_board(board, nn):
	entrance = np.copy(board)
	entrance = entrance.reshape(-1)

	for index in range(len(entrance)):
		if entrance[index] != 0:
			entrance[index] = math.log(entrance[index], 2)

	maior = 0
	saida = nn.sactivate(entrance)
	for i in range(len(saida)):
		if saida[i] > saida[maior]:
			maior = i

	print directions[maior]

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
#while True:
#	board = read_board()
#	input_board(board, brain)
	
