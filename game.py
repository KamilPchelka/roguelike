import tiletools
import graphictools
import maptools
import time
import os

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


def prepare_inventory_list(inventory):
    line_list = []
    item_info_length = 0
    name_max_length = 0
    for item in inventory:
        if (len(item) > name_max_length):
            name_max_length = len(item)
        if (len(str(inventory.__getitem__(item))) > item_info_length):
            item_info_length = len(str(inventory.__getitem__(item)))
    line_list.append("Name         amount weight")
    item_info_length += 2
    name_max_length -= 5
    format1 = str("{:<" + str(item_info_length) + "s}")
    format2 = str("{:<" + str(name_max_length) + "s}")
    for item in inventory:
        format3 = "{}"
        item_info = inventory.__getitem__(item)
        line = str(format1 + format2 + format3).format(item, str(item_info[0]), str(item_info[1]))
        line_list.append(line)
    return line_list


def add_to_inventory(item, amount, weight):
    if tiletools.Hero.inventory.__contains__("item"):
        item_info = tiletools.Hero.inventory[item]
        item_amount = item_info[1] + float(amount)
        item_weight = item_info[2] + float(weight)
        tiletools.Hero.inventory[item] = [item_amount, item_weight]
    else:
        tiletools.Hero.inventory.__setitem__(item, [float(amount), float(weight)])


def map_2_handler():
    interface = graphictools.import_graphic_from_file('graphics/interface.gfx', 80, 23)
    current_map = maptools.Map('map2', 'graphics/map1.gfx')
    hero = tiletools.Hero(100, 10, 10, 'up')
    display = graphictools.add_to_graphic(interface, current_map.map_graphic, 1, 1)
    game_loop_2(interface, current_map, display, hero)


def map_1_handler(player_name):
    interface = graphictools.import_graphic_from_file('graphics/interface.gfx', 80, 23)
    hero = tiletools.Hero(100, 8, 12, 'up')
    hero.player_name = player_name
    print(hero.player_name)
    """  map initialization """
    map1 = maptools.Map('map1', 'graphics/map2.gfx', hero)
    gold1 = tiletools.Gold(4, 4, 10, hero)
    gold2 = tiletools.Gold(3, 11, 10, hero)
    gold3 = tiletools.Gold(15, 13, 10, hero)
    gold4 = tiletools.Gold(42, 19, 10, hero)
    gold5 = tiletools.Gold(42, 7, 10, hero)
    gold6 = tiletools.Gold(35, 15, 20, hero)
    gold7 = tiletools.Gold(22, 5, 10, hero)
    gold8 = tiletools.Gold(7, 19, 20, hero)
    gold_coins = [gold1, gold2, gold3, gold4, gold5, gold6, gold7, gold8]
    rabbit1 = tiletools.Rabbit(5, 5)
    rabbit2 = tiletools.Rabbit(10, 9)
    rabbit3 = tiletools.Rabbit(6, 5)
    rabbit4 = tiletools.Rabbit(7, 5)
    rabbit5 = tiletools.Rabbit(14, 3)
    rabbit6 = tiletools.Rabbit(33, 7)
    rabbit7 = tiletools.Rabbit(37, 15)
    rabbit8 = tiletools.Rabbit(26, 18)
    rabbit9 = tiletools.Rabbit(12, 18)
    rabbit10 = tiletools.Rabbit(44, 12)
    rabbits = [rabbit1, rabbit2, rabbit3, rabbit4, rabbit5, rabbit6, rabbit7, rabbit8, rabbit9, rabbit10]
    current_map = map1
    """ ------------------- """
    display = graphictools.add_to_graphic(interface, current_map.map_graphic, 1, 1)

    game_loop_1(interface, current_map, display, hero, gold_coins, rabbits)


def game_loop_1(interface, current_map, display, hero, gold_coins, rabbits):

    while True:
        display = graphictools.add_to_graphic(interface, current_map.map_graphic, 1, 1)
        display = graphictools.add_single_tile_to_graphic(display, hero, hero.x, hero.y)

        if hero.gold < 100 or hero.rabbits_killed < 10:
            message = ['Collect 100 gold and kill',
                       '10 rabbits as a sacrifice',
                       'to the Gods. They will help',
                       'you get past the gate.',
                       "",
                       'Your gold: ' + str(hero.gold),
                       'Rabbits killed: ' + str(hero.rabbits_killed)]
        else:
            message = ['You feel bad about yourself',
                        'but Gods are pleased. They',
                        'opened the gate for you.']
            for i in range(3):
                display[17 + i][21] = graphictools.Tiles.grass

        graphictools.add_dialogue_to_display(interface, graphictools.get_dialogue_graphic())
        graphictools.add_dialogue_to_display(interface, graphictools.get_dialogue_graphic(message))

        for coin in gold_coins:
            if current_map.name == "map1" and coin.exist:
                display[coin.x][coin.y] = coin
        for rabbit in rabbits:
            if current_map.name == "map1" and rabbit.alive:
                display[rabbit.x][rabbit.y] = rabbit
        
        graphictools.print_graphic(display)

        key_pressed = getch()

        handle_user_input(display, current_map, key_pressed, hero)
        
        for coin in gold_coins:
            coin.collision_check()

        if hero.y == 21:
            map_2_handler()


def game_loop_2(interface, current_map, display, hero):
    info_box_message = ['Prepare yourself for','the final fight.', 'Gather all items marked', 'as "?" on the map.']
    while True:
        hero_string_pos = str(hero.x) + ',' + str(hero.y)
        if (maptools.Maps.items.__contains__(hero_string_pos)):
            item = maptools.Maps.items[hero_string_pos].split(',')
            add_to_inventory(item[0], item[1], item[2])
            graphictools.add_dialogue_to_display(interface, graphictools.get_dialogue_graphic(
                [[tiletools.Tiles.black.string] * 28] * 9))
            info_box_message = ['You gained:', str('name: ' + item[0]), str('amount: ' + item[1])]
            current_map.map_graphic[hero.x - 1][hero.y -1 ] = tiletools.Tiles.grass
            maptools.Maps.items.__delitem__(hero_string_pos)
            if(not maptools.Maps.items):
                graphictools.add_dialogue_to_display(interface, graphictools.get_dialogue_graphic(
                    [[tiletools.Tiles.black.string] * 28] * 9))
                info_box_message = ['You are ready for the battle',
                                    'get to the boss cave',
                                    'using black entrance',
                                    'at the bottom of the map']
            print(tiletools.Hero.inventory)

        display = graphictools.add_to_graphic(interface, current_map.map_graphic, 1, 1)
        graphictools.add_dialogue_to_display(interface, graphictools.get_dialogue_graphic(info_box_message))
        display = graphictools.add_single_tile_to_graphic(display, hero, hero.x, hero.y)
        graphictools.print_graphic(display)

        key_pressed = getch()
        if (key_pressed == 'i' or key_pressed == 'i'):
            info_box_message = prepare_inventory_list(hero.inventory)

        handle_user_input(display, current_map, key_pressed, hero)
        if(not maptools.Maps.items and hero_string_pos in ['13,18', '14,18', '15,18']):
            exit()


def handle_user_input(display, current_map, key_pressed, hero):
    """ Make the move if there is no collision. """
    if key_pressed == "w" and display[hero.x][hero.y - 1].walkable:
            display[hero.x][hero.y] = current_map.map_graphic[hero.x - 1][hero.y - 1]
            hero.background = display[hero.x][hero.y - 1].background
            hero.update_string()
            hero.y -= 1
            hero.direction = 'up'
    elif key_pressed == "a" and display[hero.x - 1][hero.y].walkable:
            display[hero.x][hero.y] = current_map.map_graphic[hero.x - 1][hero.y - 1]
            hero.background = display[hero.x - 1][hero.y].background
            hero.update_string()
            hero.x -= 1
            hero.direction = 'left'

    elif key_pressed == "s" and display[hero.x][hero.y + 1].walkable:
            display[hero.x][hero.y] = current_map.map_graphic[hero.x - 1][hero.y - 1]
            hero.background = display[hero.x][hero.y + 1].background
            hero.update_string()
            hero.y += 1
            hero.direction = 'down'

    elif key_pressed == "d" and display[hero.x + 1][hero.y].walkable:
            display[hero.x][hero.y] = current_map.map_graphic[hero.x - 1][hero.y - 1]
            hero.background = display[hero.x + 1][hero.y].background
            hero.update_string()
            hero.x += 1
            hero.direction = 'right'

    elif key_pressed == 'k':
        animate_attack(display, hero)

    elif key_pressed == "q":
        exit()


def sword_frame(display, hero, x_offset, y_offset, sword_char):
    tile_copy = display[hero.x + x_offset][hero.y + y_offset]
    string = '\x1b[' + '38;2;255;255;255;' + tile_copy.background + sword_char + '\x1b[0m'
    graphictools.add_single_tile_to_graphic(display, string, hero.x+x_offset, hero.y+y_offset)
    graphictools.print_graphic(display)
    graphictools.add_single_tile_to_graphic(display, tile_copy, hero.x+x_offset, hero.y+y_offset)
    time.sleep(0.1)
    if tile_copy.name == 'rabbit':
        graphictools.add_single_tile_to_graphic(display, tiletools.Tiles.blood, hero.x+x_offset, hero.y+y_offset)
        tile_copy.alive = False
        hero.rabbits_killed += 1


def animate_attack(display, hero):
    if hero.direction == 'up':
        sword_frame(display, hero, -1, -1, '\\')
        sword_frame(display, hero, 0, -1, '|')
        sword_frame(display, hero, 1, -1, '/')

    if hero.direction == 'left':
        sword_frame(display, hero, -1, 1, '/')
        sword_frame(display, hero, -1, 0, '-')
        sword_frame(display, hero, -1, -1, '\\')

    if hero.direction == 'down':
        sword_frame(display, hero, 1, 1, '\\')
        sword_frame(display, hero, 0, 1, '|')
        sword_frame(display, hero, -1, 1, '/')

    if hero.direction == 'right':
        sword_frame(display, hero, 1, -1, '/')
        sword_frame(display, hero, 1, 0, '-')
        sword_frame(display, hero, 1, 1, '\\')


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
            return option
    elif (input == "q"):
        exit()
    elif (input == "C" and option in [1, 2, 3, 4, 5]):
        selected_item_handler(option)
    return None


def selected_item_handler(option):
    """
    Function triggers stage which depends on option variable.
    :param option: 
    :return: None
    """
    if (option == 1):
        story_screen_handler()
    if (option == 2):
        howto_screen_handler()
    if (option == 3):
        pass
    if (option == 4):
        about_screen_handler()
    if (option == 5):
        exit()


def story_screen_handler():
    os.system('clear')
    with open('graphics/story.txt', 'r') as f:
        for line in f:
            print(line, end='')
        input = getch()
        character_creation_handler()


def howto_screen_handler():
    os.system('clear')
    with open('graphics/howto.txt', 'r') as f:
        for line in f:
            print(line, end='')
        input = getch()


def about_screen_handler():
    os.system('clear')
    with open('graphics/about.txt', 'r') as f:
        for line in f:
            print(line, end='')
        input = getch()


def character_creation_handler():
    os.system('clear')
    print('\n' * 6)
    print(' ' * 32, 'Enter your name:')
    print(' ' * 36, end='')
    player_name = input()
    map_1_handler(player_name)


if __name__ == '__main__':
        trigger_menu()

