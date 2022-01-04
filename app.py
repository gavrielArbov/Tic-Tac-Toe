from random import choice

def display_board(board):
    for row in board:
        print_decoration1()
        print_decoration2()
        print_row(row)
        print_decoration2()
    print_decoration1()    

def print_decoration1():
    print("+", "+", "+", "+", sep="-------")
    
def print_decoration2():
    print("|", "|", "|", "|", sep="       ")
    
def print_row(row):
    for sign in row:
        print("|   "+str(sign), sep="   ", end="   ")
    print("|", end="")   
    print()

def enter_move(board):
    print("Enter your move: ", end="")
    sign = int(input())
    
    while sign not in available_moves:
        print("Invalid input, Try again: ", end="")
        sign = int(input())
        
    row = (sign-1)//len(board)
    col = (sign-1)%len(board)
    
    available_moves.remove(sign)
    board[row][col] = "O"

    
def victory_for(board, sign):
    # cols
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    # rows
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
        
    # x's
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[2][0] == sign and board[2][1] == sign:
        return True
        
    return False

        

def draw_move(board):
    if len(available_moves) == 9:
        board[1][1] = "X"
        available_moves.remove(5)
    else:
        sign = choice(available_moves)
        row = (sign-1)//len(board)
        col = (sign-1)%len(board)
    
        available_moves.remove(sign)
        board[row][col] = "X"
        
    

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while available_moves:
    draw_move(board)
    display_board(board)
    if victory_for(board, "X"):
        print("The Computer Won!")
        break
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        print("You Won!")
        break
    