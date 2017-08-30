import tiletools
import graphictools


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


def trigger_game():
    interface = graphictools.import_graphic_from_file('graphics/interface.gfx', 80, 23)
    current_map = graphictools.import_graphic_from_file('graphics/map1.gfx', 47, 21)
    hero = tiletools.Hero(100, 10, 10, 'up')
    display = graphictools.add_to_graphic(interface, current_map, 1, 1)

    game_loop(interface, current_map, display, hero)


def game_loop(interface, current_map, display, hero):
    while True:
        display = graphictools.add_to_graphic(interface, current_map, 1, 1)
        display = graphictools.add_single_tile_to_graphic(display, hero, hero.x, hero.y)
        graphictools.print_graphic(display)
    
        key_pressed = getch()

        handle_user_input(display, current_map, key_pressed, hero)

        if hero.y == 1:
            current_map = graphictools.import_graphic_from_file('graphics/map2.gfx', 47, 21)
            hero.y = 21


def handle_user_input(display, current_map, key_pressed, hero):
    """ Make the move if there is no collision. """
    if key_pressed == "w" and display[hero.x][hero.y-1].walkable:
            display[hero.x][hero.y] = current_map[hero.x - 1][hero.y - 1]
            hero.y -= 1
            hero.direction = 'up'
    elif key_pressed == "a" and display[hero.x-1][hero.y].walkable:
            display[hero.x][hero.y] = current_map[hero.x - 1][hero.y - 1]
            hero.x -= 1
            hero.direction = 'left'

    elif key_pressed == "s" and display[hero.x][hero.y+1].walkable:
            display[hero.x][hero.y] = current_map[hero.x - 1][hero.y - 1]
            hero.y += 1
            hero.direction = 'down'

    elif key_pressed == "d" and display[hero.x+1][hero.y].walkable:
            display[hero.x][hero.y] = current_map[hero.x - 1][hero.y - 1]
            hero.x += 1
            hero.direction = 'right'

    elif key_pressed == "q":
        exit()


def trigger_menu():
    option = 1
    lines_list = []
    with open('graphics/menu.txt', 'r') as f:
        lines_list = f.readlines()
    while True:
        for line in list(lines_list):
            if line.__contains__('%'):
                index = line.index('%')
                if(int(line[index+1]) == option):
                    line = line.replace('%' + str(option), " [6;30;42m")
                else:
                    line = line.replace('%' + line[index+1], ' ')
            print(line, end='')
        input = getch()
        output = handle_main_menu_user_input(input, option)
        if output in [1,2,3,4,5]:
            option = output


def handle_main_menu_user_input(input, option):
    if (input == "A"):
        if (option == 1):
            return 5
        else:
            option -= 1
            return option
    elif (input == "B"):
        if (option == 5):
            return 1
        else:
            option += 1
            return  option
    elif (input == "q"):
        exit()
    elif (input == "C" and option in [1, 5]):
        selected_item_handler(option)
    return None


def selected_item_handler(option):
    """
    Function triggers stage which depends on option variable.
    :param option: 
    :return: None
    """
    if (option == 1):
        trigger_game()
    if (option == 5):
        exit()
        

if __name__ == '__main__':
        trigger_menu()

