game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def printGame():
	print(game[0])
	print(game[1])
	print(game[2])

print("Welcome to Tic Tac Toe. Please press enter to continue.")
input()
x = 0
while(x < 9):
	printGame()
	print("\nPlease enter coordinates in the form x,y : type QUIT to quit.")
	stringIn = input()
	if(stringIn.upper() == "QUIT"):
		break
	row = 0;
	col = 0;
	cont = False;
	try:
		row = int(stringIn[2])
		col = int(stringIn[0])
		cont = True
	except:
		cont = False
	print()
	if(cont and game[row-1][col-1] == ' '):
		if(x % 2 == 0):
			game[row-1][col-1] = 'X'
			x = x + 1
		else:
			game[row-1][col-1] = '0'
			x = x + 1
	else:
		print("Invalid input, please try again.")
printGame()


