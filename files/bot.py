import math
import random as r


def botAI(board, snake, velx, vely):
	moves = get_moves(velx, vely)
	apple = board.apple_pos
	head = snake.pos[-1]

	values = list(map( lambda x: f_value(board, [head[0] + x[0], head[1] + x[1]], snake), moves))
	min_ = min(values)
	#print(moves)
	#print(values)
	return moves[values.index(min_)]

def f_value(board, pos, snake):
	apple = board.apple_pos
	if not board.check_colition(pos, snake):
		return math.inf

	if not enclose_check(board, pos, snake):
		return math.inf

	return ((apple[0] - pos[0]) ** 2 + (apple[1] - pos[1]) ** 2) ** 1 / 2

def get_moves(velx, vely):
	actions = [[1, 0], [-1, 0], [0,-1], [0,1]]
	if vely == 1:
		not_possible = [-vely, velx]
	else:
		not_possible = [vely, -velx]
	moves = [i for i in actions if i != not_possible]
	r.shuffle(moves)
	return moves

def enclose_check(board, pos, snake):
	check = [pos]
	neighbours = []

	while len(check) != 0:
		new = check.pop(0)
		neighbours.append(new)
		new_neighbours = get_neighbours(board, new, snake)
		for elm in new_neighbours:
			if elm not in check + neighbours:
				check.append(elm)
				if len(neighbours) > snake.score():
					return True

	total = 0
	for line in board.board:
		for col in line:
			if col not in 's':
				total += 1

	return len(neighbours)/total >= 0.8

def get_neighbours(board, pos, snake):
	moves = get_moves(0,0)
	neighbours = []
	for move in moves:
		new = [pos[0] + move[0], pos[1] + move[1]]
		if board.check_colition(new, snake):
			neighbours.append(new)
	return neighbours

if __name__ == '__main__':
	from classes import Board, Snake

	board = Board(5,5)
	snake = Snake()
	board.set_snake(snake)
	[print(i) for i in board.board]

	vy, vx = botAI(board, snake, 0,0)
	for i in range(20):
		print(vx, vy)
		print(enclose_check(board, snake.pos[-1], snake))
		snake.move(vx, vy)
		if not board.set_snake(snake):
			print('dead')
		[print(i) for i in board.board]
		vy, vx = botAI(board, snake, vx, vy)








