game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def printGame():
	print(game[0])
	print(game[1])
	print(game[2])

print("Welcome to Tic Tac Toe. Please press enter to continue.")
input()
printGame()
x = 0
while(x < 9):
	print("Please enter coordinates in the form x,y")
	stringIn = input()
	x = int(stringIn[0])
	y = int(stringIn[2])
	game[x-1][y-1] = 'X'
	printGame()

