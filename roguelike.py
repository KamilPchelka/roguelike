import os


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


def get_yx(board):
    for row in board:
        try:
            return board.index(row), row.index("@")
        except:
            continue


def main():
    width = 20
    height = 10

    board = create_board(width, height)

    # test movement
    board[4][9] = "@"
    print_board(board)

    while True:
        os.system("clear")
        print_board(board)
        key_pressed = getch()
        if key_pressed == "w":
            y = get_yx(board)[0]
            x = get_yx(board)[1]
            board[y-1][x] = "@"
            board[y][x] = " "
        elif key_pressed == "a":
            y = get_yx(board)[0]
            x = get_yx(board)[1]
            board[y][x-1] = "@"
            board[y][x] = " "
        elif key_pressed == "s":
            y = get_yx(board)[0]
            x = get_yx(board)[1]
            board[y+1][x] = "@"
            board[y][x] = " "
        elif key_pressed == "d":
            y = get_yx(board)[0]
            x = get_yx(board)[1]
            board[y][x+1] = "@"
            board[y][x] = " "
        elif key_pressed == "q":
            break



main()