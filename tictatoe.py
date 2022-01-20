def main():
    print("This is the Tic Tac Toe game")

    player = next_player("")
    board_funtion = board()
    
    while not (has_winner(board_funtion) or the_draw(board_funtion)):
        display_board(board_funtion)
        decision(player, board_funtion)
        player = next_player(player)
    display_board(board_funtion)



def board():
    numbers = []
    for square in range(9):
        numbers.append(square + 1)
    return numbers


def display_board(board):
        print(f"\n{board[0]}|{board[1]}|{board[2]}")
        print("------")
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print("------")
        print (f"{board[6]}|{board[7]}|{board[8]}")

def the_draw(board):

    for i in range(9):
        if board[i] != "x" and board[i] != "o":
            return False
    return True

def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def decision(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


def next_player(current):
    if current == "" or current =="o":
        return "x"
    elif current == "x":
        return "o"
if __name__ == "__main__":
    main()