import math


def botAI(board, snake, velx, vely):
	actions = [[1, 0], [-1, 0], [0,-1], [0,1]]
	if vely == 1:
		not_possible = [-vely, velx]
	else:
		not_possible = [vely, -velx]
	moves = [i for i in actions if i != not_possible]
	apple = board.apple_pos
	head = snake.pos[-1]

	values = list(map( lambda x: f_value(board, [head[0] + x[0], head[1] + x[1]]), moves))
	min_ = min(values)
	return moves[values.index(min_)]

def f_value(board, pos):
	apple = board.apple_pos
	if not board.check_colition(pos):
		return math.inf

	return ((apple[0] - pos[0]) ** 2 + (apple[1] - pos[1]) ** 2) ** 1 / 2


if __name__ == '__main__':
	board = Board(70,24)
	snake = Snake()
	board.set_snake(snake)
	[print(i) for i in board.board]

	print(botAI(board, snake))
