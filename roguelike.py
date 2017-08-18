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

def launch_main_game():
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
            main_menu_handler()
            break

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

def main_menu_handler():
    lines = open("Screens/main_menu_screen").readlines()
    selected = 1
    while(True):
        os.system('clear')
        draw_main_menu(selected, lines)
        input = getch()
        print(input)
        if(input == "A"):
            if(selected == 1):
                selected = 5
            else:
                selected -= 1
        elif(input == "B"):
            if(selected == 5):
                selected = 1
            else:
                selected += 1
        elif (input == "q"):
            exit()
        elif (input == "C" and selected == 1):
            selected_item_handler(selected)
            break

def draw_main_menu(selected, lines):
    if (selected == 1):
        for index in range(0, 50):
            print(lines[index], end='')
    if (selected == 2):
        for index in range(51, 101):
            print(lines[index], end='')
    if (selected == 3):
        for index in range(102, 152):
            print(lines[index], end='')
    if (selected == 4):
        for index in range(204, 254):
            print(lines[index], end='')
    if (selected == 5):
        for index in range(255, 305):
            print(lines[index], end='')

def selected_item_handler(selected):
    """
    Function triggers stage which depends on selected variable.
    :param selected: 
    :return: None
    """
    if (selected == 1):
        launch_main_game()


def main():
    main_menu_handler()
main()