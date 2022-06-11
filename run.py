# player name
playerName = input("Your letter is X. What is your first name?:")
print("Welcome to Exes and Ohs, " + playerName)

# print the board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def board():
    print(board[0:3])
    print(board[3:6])
    print(board[6:])

count = 0
go = 0

# play game
moves = int(input("Place X anywhere between 1-9"))

if board[moves-1] == "-":
    board[moves-1] = "x"
    count = count + 1
    go = 1

# player input

# check for a win or a tie

if count == 9:
    print("GAME OVER. No Winner.")
    sys.exit()