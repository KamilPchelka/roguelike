def create_board(width, height):
    board = []
    for i in range(height):
        board.append([])
        for j in range(width):
            # if it's a border:
            if (i == 0 or i == height-1) or (j == 0 or j == width-1):
                board[i].append("#")
            # if it's NOT a border:
            else:
                board[i].append(" ")
            
    return board


def print_board(board):
    for row in board:
        for elem in row:
            print(elem, end="")
        print()


def main():
    width = 20
    height = 10

    board = create_board(width, height)
    print_board(board)


main()