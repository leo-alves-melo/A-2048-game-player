#Leonardo Alves de Melo

import numpy as np
from random import randint

columns = 4
lines = 4
start_value = 2

class Game():
	def __init__(self):
		self.board = np.array([[0]*columns]*lines)
		self.initiate()

	def get_empty_positions(self):
		empty_positions = []

		for line in range(lines):
			for column in range(columns):
				if self.board[line][column] == 0:
					empty_positions.append((line,column))

		return empty_positions

	def create_start_value(self):

		empty_positions = self.get_empty_positions()

		empty_position = empty_positions[randint(0, len(empty_positions) - 1)]

		self.board[empty_position[0]][empty_position[1]] = start_value

	def initiate(self):
		self.create_start_value()
		self.create_start_value()

	def apply_right(self):
		
		for line in range(lines):

			index = columns - 1

			#Desloca para a direita
			for column in range(1, columns):
				have_to_change = False

				if self.board[line][index - column] != 0:
					change_index = index - column
					while self.board[line][change_index + 1] == 0:
						have_to_change = True
						change_index += 1
						if change_index + 1 == columns:
							break

					if have_to_change:

						self.board[line][change_index] = self.board[line][index - column]
						self.board[line][index - column] = 0

			#Aplica a juncao
			for column in range(1, columns):

				if self.board[line][index - column] == self.board[line][index - column + 1] and self.board[line][index - column] != 0:
					
					self.board[line][index - column + 1] *= 2
					for change_index in range(0, index - column):
						self.board[line][index - column - change_index] = self.board[line][index - column - change_index - 1]
					self.board[line][0] = 0

	def apply_left(self):
		for line in range(lines):

			index = columns - 1

			#Desloca para a esquerda
			for column in range(1, columns):
				have_to_change = False

				if self.board[line][column] != 0:
					change_index = column
					while self.board[line][change_index - 1] == 0:
						have_to_change = True
						change_index -= 1
						if change_index == 0:
							break

					if have_to_change:

						#print 'Mudei: ' + str(change_index) + ' - recebeu ' + str(column)

						self.board[line][change_index] = self.board[line][column]
						self.board[line][column] = 0

			#Aplica a juncao
			for column in range(1, columns):

				if self.board[line][column] == self.board[line][column - 1] and self.board[line][column] != 0:
					
					self.board[line][column - 1] *= 2
					for change_index in range(column, columns - 1):
						self.board[line][change_index] = self.board[line][change_index + 1]
					self.board[line][columns-1] = 0

	def apply_up(self):
		for column in range(columns):

			index = lines - 1

			#Desloca para a esquerda
			for line in range(1, lines):
				have_to_change = False

				if self.board[line][column] != 0:
					change_index = line
					while self.board[change_index - 1][column] == 0:
						have_to_change = True
						change_index -= 1
						if change_index == 0:
							break

					if have_to_change:

						#print 'Mudei: ' + str(change_index) + ' - recebeu ' + str(column)

						self.board[change_index][column] = self.board[line][column]
						self.board[line][column] = 0

			#Aplica a juncao
			for line in range(1, lines):

				#print 'testando: ' + str(line) + ' - ' + str(line - 1)

				if self.board[line][column] == self.board[line - 1][column] and self.board[line][column] != 0:
					
					
					self.board[line - 1][column] *= 2
					for change_index in range(line, lines - 1):
						self.board[change_index][column] = self.board[change_index + 1][column]
					self.board[lines - 1][column] = 0

	def apply_down(self):
		for column in range(columns):

			index = lines - 1

			#Desloca para a esquerda
			for line in range(1, lines):
				have_to_change = False

				if self.board[index - line][column] != 0:
					change_index = index - line
					while self.board[change_index + 1][column] == 0:
						have_to_change = True
						change_index += 1
						if change_index == lines - 1:
							break

					if have_to_change:

						#print 'Mudei: ' + str(change_index) + ' - recebeu ' + str(column)

						self.board[change_index][column] = self.board[index - line][column]
						self.board[index - line][column] = 0

			#Aplica a juncao
			for line in range(1, lines):

				#print 'testando: ' + str(line) + ' - ' + str(line - 1)

				if self.board[index - line][column] == self.board[ index - line + 1][column] and self.board[index - line][column] != 0:
					
					
					self.board[index - line + 1][column] *= 2
					for change_index in range(0, index - line):
						self.board[index - line - change_index][column] = self.board[index - line - change_index - 1][column]
					self.board[0][column] = 0

	#Aplica o comando de girar e diz se ele foi um comando valido
	def apply_command(self, command):

		last_board = np.copy(self.board)
		
		if command == 'r':
			self.apply_right()
		if command == 'l':
			self.apply_left()
		if command == 'u':
			self.apply_up()
		if command == 'd':
			self.apply_down()

		if np.array_equal(last_board, self.board):
			return False
		else:
			return True

			
	def user_play(self):
		print 'Write your command'
		command = raw_input()

		while not self.apply_command(command):
			print 'The board could not be able to turn to that direction. Try another one'
			print 'Write your command'
			command = raw_input()


	def new_round(self):
		self.create_start_value()


game = Game()
#game.board = np.array([[2,2,0,0],[2,0,2,0],[2,0,2,0],[2,0,0,2]])
#print game.board
#game.user_play()
#print game.board
#
#exit()

while True:

	print '\n --------------------'
	print game.board
	game.user_play()
	print '\n'
	print game.board
	game.new_round()

