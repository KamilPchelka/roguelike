class Tile:
    def __init__(self, name, character, foreground, background, is_obstacle):
        self.name = name
        self.character = character
        self.foreground = foreground
        self.background = background
        self.is_obstacle = is_obstacle
        self.string = '\x1b[' + foreground + background + character + '\x1b[0m'


class Tiles:
    grass = Tile('grass', '.', '38;2;109;255;188;', '48;2;40;170;50m', False)
    dirt = Tile('dirt', '.', '38;2;200;200;200;', '48;2;165;75;15m', True)
    river = Tile('river', '=', '38;2;63;219;255;', '48;2;57;65;202m', True)
    flower = Tile('flower', '*', '38;2;255;255;0;', '48;2;40;170;50m', False)
    mountain = Tile('mountain', '^', '38;2;170;103;17;', '48;2;120;57;15m', True)
    black = Tile('black', ' ', '38;2;0;0;0;', '48;2;0;0;0m', True)
    stoneWall = Tile('stoneWall', '#', '38;2;137;150;109;', '48;2;64;70;66m', True)
    stoneFloor = Tile('stoneFloor', '.', '38;2;200;200;200;', '48;2;120;120;120m', False)
    hudHash = Tile('hudHash', '#', '38;2;255;255;255;', '48;2;0;0;0m', True)
    hudStar = Tile('hudStar', '*', '38;2;255;255;255;', '48;2;0;0;0m', True)

    tile_names = [tile for tile in vars().keys() if not tile.startswith('__')]