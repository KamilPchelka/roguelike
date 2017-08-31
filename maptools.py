import graphictools
import tiletools


class Map():
    def __init__(self, name, graphic_path, hero):
        self.name = name
        self.map_graphic = graphictools.import_graphic_from_file(graphic_path, 47, 21)
        self.hero = hero
    

class Maps():
    map1 = Map('map1', load_map_graphic('graphics/map1.gfx'))
    map2 = Map('map2', load_map_graphic('graphics/map2.gfx'))
