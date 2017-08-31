from tiletools import Tiles


def print_tiles_chart(list):
    for tile_name in list:
        string = tile_name + ':'
        print(string.ljust(15), end='')
        print(eval('Tiles.' + tile_name + '.string')*3)


def get_graphic_from_txt(file_name, width, height):
    """ Return a 2d list in graphic[x][y] format, converted from file_name. """

    graphic = [[None for i in range(height)] for j in range(width)]

    with open(file_name) as f:
        y = 0
        for line in f:
            x = 0
            for ch in line:
                if ch == '\n':
                    continue
                graphic[x][y] = ch
                x += 1
            y += 1
    return graphic


def print_graphic(graphic):
    width = len(graphic)
    height = len(graphic[0])

    for y in range(height):
        for x in range(width):
            try:
                print(graphic[x][y].string, end='')
                if x == width - 1:  # if it's a last char in line, print newline
                    print()
            except AttributeError:  # if not a Tile, simply print
                print(graphic[x][y], end='')
                if x == width - 1:
                    print()


def get_unique_characters(graphic):
    """ Get a list of unique characters in the graphic. It will be used for coloring the graphic. """
    unique_characters = []

    for line in graphic:
        for ch in line:
            if ch not in unique_characters:
                unique_characters.append(ch)

    return unique_characters


def colorize(graphic):
    """ A tool for user to change text characters to colorized tiles. """

    chars = get_unique_characters(graphic)

    for ch in chars:
        print_graphic(graphic)
        try:
            print('the tile is:' + ch.string)
        except AttributeError:
            print('the character is:' + str(ch))
        print('available tiles:')
        print_tiles_chart(Tiles.tile_names)
        user_input = input('pick a tile to replace it (enter nothing to skip, "q" to quit): ')

        if user_input == 'q':
            exit()
        elif user_input in Tiles.tile_names:
            width = len(graphic)
            height = len(graphic[0])

            for y in range(height):
                for x in range(width):
                    if graphic[x][y] == ch:
                        graphic[x][y] = eval('Tiles.' + user_input)
        else:
            print('step skipped')

    return graphic


def export_graphic_to_file(graphic):
    """ Export graphic to a file. Every tile is saved as 'Tiles.<tilename> to make import easier.
    '&&x&&' and '&&y&&' are separators. """

    print_graphic(graphic)
    file_name = input('Choose a file name for export (or nothing to quit): ')
    if file_name == '':
        exit()

    width = len(graphic)
    height = len(graphic[0])

    with open(file_name, 'w') as f:
        for i in range(height):
            for j in range(width):
                try:
                    f.write('Tiles.' + graphic[j][i].name + '&&x&&')
                except AttributeError:
                    f.write(graphic[j][i] + '&&x&&')
            f.write('&&y&&')


def import_graphic_from_file(file_name, width, height):
    """ Import graphic from the file. If a Tile object is read, it's written into graphic[x][y]
    ready to use as Tile.<tilename>. """

    graphic = [[None for i in range(height)] for j in range(width)]

    with open(file_name) as f:
        buffer = f.read()
        rows = buffer.split('&&y&&')
        del rows[-1]

        y = 0
        for row in rows:
            x = 0
            tiles = row.split('&&x&&')
            del tiles[-1]
            for tile in tiles:
                try:
                    graphic[x][y] = eval(tile)
                except (SyntaxError, NameError):
                    graphic[x][y] = tile
                finally:
                    x += 1
            y += 1
                        
    return graphic


def add_to_graphic(background, newgraphic, x0, y0):
    """ Insert newgraphic into background starting from given x, y, coordinates. """
    newgraphic_width = len(newgraphic)
    newgraphic_height = len(newgraphic[0])
    for y in range(newgraphic_height):
        for x in range(newgraphic_width):
            background[x + x0][y + y0] = newgraphic[x][y]
    return background


def get_dialogue_graphic(text_list=['                             ', '                             ']):
    two_dimension_list = []
    for line in text_list:
        char_list = []
        for char in line:
            char_list.append('\x1b[' + '38;2;255;255;255;'+ '48;2;0;0;0m'+ char + '\x1b[0m')

        two_dimension_list.append(char_list)

    return two_dimension_list


def add_dialogue_to_display(display, dialogues):
    y0 = 13
    for line in dialogues:
        x0 = 50
        for char in line:
            display[x0][y0] = char
            x0 += 1
        y0 += 1


def add_single_tile_to_graphic(background, single_tile, x, y):
    """ Insert newgraphic into background starting from given x, y, coordinates. """
    background[x][y] = single_tile
    return background


def main():
    """ User loads graphic, colorize it with available tiles, and saves it to a file. """
    
    print('choose action:')
    print('t - open pure text graphic')
    print('c - open colored graphic')
    print('anything else - quit')
    choice = input()

    if choice not in ('t', 'c'):
        return

    file_name = input('Enter file name: ')
    width = int(input('Enter graphics width: '))
    height = int(input('Enter graphics height: '))

    if choice == 't':
        graphic = get_graphic_from_txt(file_name, width, height)
    elif choice == 'c':
        graphic = import_graphic_from_file(file_name, width, height)

    graphic = colorize(graphic)
    export_graphic_to_file(graphic)



if __name__ == '__main__':
    main()