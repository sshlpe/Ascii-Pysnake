
def check_point(score):
	if score > max_score():
		with open('files/score.txt', 'w') as file:
			file.write(f'{score}')

def max_score():
	with open('files/score.txt', 'r') as file:
		return int(file.readlines()[0])

if __name__ == '__main__':
	check_point(1)
	print(max_score())