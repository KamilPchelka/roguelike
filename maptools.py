import graphictools
import tiletools


class Map():
    def __init__(self, name, graphic_path, hero=None):
        self.name = name
        self.map_graphic = graphictools.import_graphic_from_file(graphic_path, 47, 21)
        self.hero = hero
    

class Maps():
    items = {'0,6': 'money,20 ',
             '1,40': 'blue potion,4',
             '2,14' : 'red potion,5',
             '3,2': 'money,50',
             '5,17': 'golden chestplate,1',
             '7,32': 'money,89',
             '8,41': 'golden bow,1',
             '9,7': 'golden shoes,1',
             '9,26': 'golden helmet,1',
             '11,0': 'golden bracelet,1',
             '11,17': 'golden crossbow,1',
             '13,34': 'golden arrow,23',
             '14,20': 'money,55',
             '16,11': 'blue potion,12',
             '16,28': 'red potion,6',
             '17,1': 'speed potion,9',}

