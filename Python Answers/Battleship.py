#Battleships


def make_board():
    matrix = []
    for i in range(0,5):
        matrix.append(["O"] * 5)
        
    return matrix



def print_board(board):
    for row in board:
        print (" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

print (ship_row)
print (ship_col)

if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")

else:
    print ("You missed my battleship!")
    if guess_row != ship_row or guess_col != ship_col:
    	print ("You not even near the ocean!")
    board[int(guess_row)][int(guess_col)] = "X"

    print_board(board)
