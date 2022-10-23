
import random as rd

class Board:

	def __init__(self, sizeX, sizeY):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.board = [[' ' for i in range(self.sizeX)] for i in range(self.sizeY)]
		self.apple = False
		self.apple_pos = []

		self.reload()

	def set_board(self):
		self.board = [[' ' for i in range(self.sizeX)] for i in range(self.sizeY)]
		self.set_borders()
		self.board[self.apple_pos[0]][self.apple_pos[1]] = 'm'

	def set_borders(self):
		for i in range(self.sizeY):
			self.board[i][0] = '|'
			self.board[i][-1] = '|'
		self.board[-1] = ['_' for i in range(self.sizeX)]

	def reload(self):
		self.spawn_apple()
		self.set_board()


	def set_snake(self, snake):
		self.set_board()

		for i in range(len(snake.pos)-1):
			elm = snake.pos[i]
			self.board[elm[0]][elm[1]] = 's'

		elm = snake.pos[-1]
		collision = self.check_colition(elm, snake)
		if not collision:
			return False
		if self.board[elm[0]][elm[1]] in 'm':
			snake.grow()
			self.reload()
			return self.set_snake(snake)
		self.board[elm[0]][elm[1]] = 'S'
		return True

	def check_colition(self, pos, snake):
		if (0 > pos[1] or 0 > pos[0]) or (self.sizeX <= pos[1] or self.sizeY <= pos[0]):
			return False

		if self.board[pos[0]][pos[1]] in 'sS' and snake.score() > 1:
			return False

		return True

	def spawn_apple(self):
		possible = []
		for line in range(self.sizeY):
			for col in range(self.sizeX):
				if self.board[line][col] not in 'sS':
					possible.append([line, col])
		self.apple_pos = rd.choice(possible)


class Snake:

	def __init__(self):
		self.pos = [[2,1]]

	def move(self, vx, vy):

	    for i in range(len(self.pos)-1):
	        self.pos[i] = self.pos[i+1].copy()
	    self.pos[-1][0] += vy
	    self.pos[-1][1] += vx

	def grow(self):
		self.pos = [self.pos[0]] + self.pos

	def score(self):
		return len(self.pos) -1


if __name__ == '__main__':
	print('hola gloria')


	

