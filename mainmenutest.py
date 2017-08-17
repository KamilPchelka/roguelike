import os
def main_menu_handler():
    lines = open("Screens/main_menu_screen").readlines()
    selected = 1
    while(True):
        os.system('clear')
        draw_main_menu(selected, lines)
        input = getch()
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





def getch():
    """Function get the type of character pressed
        @:return: pressed character
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
if __name__ == '__main__':
    main_menu_handler()