import tiletools
import graphictools


def main():
    interface = graphictools.import_graphic_from_file('graphics/interface.gfx', 80, 23)
    map1 = graphictools.import_graphic_from_file('graphics/map1.gfx', 47, 21)
    display = graphictools.add_to_graphic(interface, map1, 1, 1)
    graphictools.print_graphic(display)



if __name__ == '__main__':
        main()