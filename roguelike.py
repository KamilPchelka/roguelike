import os


def create_board(width, height):
    board = []

    for i in range(width):
        board.append([])

        for j in range(height):
            # if it's a border:
            if (j == 0 or j == height-1) or (i == 0 or i == width-1):
                board[i].append("#")
            else:
                board[i].append(" ")
            
    return board


def print_board(board):
    col = len(board)
    row = len(board[0])
    
    for i in range(row):
        for j in range(col):
            print(board[j][i], end="")
        print()


def getch():
    """Function get the type of character pressed
        @:return: None
    """
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def get_xy(board):
    for column in board:
        try:
            return board.index(column), column.index("@")
        except:
            continue


def main():
    width = 20
    height = 10
    board = create_board(width, height)
    board[9][4] = "@"

    while True:
        os.system("clear")
        print_board(board)

        key_pressed = getch()

        # hero coordinates
        x = get_xy(board)[0]
        y = get_xy(board)[1]

        # make the move if there is no collision
        if key_pressed == "w" and (board[x][y - 1] != "#"):
                board[x][y - 1] = "@"
                board[x][y] = " "

        elif key_pressed == "a" and (board[x - 1][y] != "#"):
                board[x - 1][y] = "@"
                board[x][y] = " "

        elif key_pressed == "s" and (board[x][y + 1] != "#"):
                board[x][y + 1] = "@"
                board[x][y] = " "

        elif key_pressed == "d" and (board[x + 1][y] != "#"):
                board[x + 1][y] = "@"
                board[x][y] = " "

        elif key_pressed == "q":
            break


main()