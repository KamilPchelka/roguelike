import graphictools
class Map():
    def __init__(self, name, graphic_path, hero=None):
        self.name = name
        self.map_graphic = graphictools.import_graphic_from_file(graphic_path, 47, 21)
        self.hero = hero


class Maps():
    items = {'7,1': 'gold,20,0.1',
             '41,2': 'blue potion,4,0.8',
             '15,3' : 'red potion,5,1',
             '3,4': 'gold,50,0.3',
             '18,6': 'gold armor,1,5',
             '33,8': 'gold,89,0.5',
             '41,9': 'red potion,9,1.8',
             '8,10': 'gold shoes,1,3',
             '27,10': 'gold helmet,1,2',
             '1,12': 'blue potion,6,1.2',
             '18,12': 'gold,100,0.5',
             '35,14': 'arrow,23,0.5',
             '21,15': 'gold,55,0.2',
             '12,17': 'blue potion,12,2.4',
             '2,18': 'gold,40,0.2',
             '29,17': 'dragon glass,4,1'}

    def load_map_graphic(path):
        return graphictools.import_graphic_from_file(path, 47, 21)
    