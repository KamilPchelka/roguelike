import graphictools
class Map():
    def __init__(self, name, map_graphic):
        self.name = name
        self.map_graphic = map_graphic


class Maps():
    def load_map_ghraphic(path):
        return graphictools.import_graphic_from_file(path, 47, 21)

    map1 = Map('map1', load_map_ghraphic('graphics/map1.gfx'))
    map2 = Map('map2', load_map_ghraphic('graphics/map2.gfx'))
