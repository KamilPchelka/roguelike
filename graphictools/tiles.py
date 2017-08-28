class Tile:
    def __init__(self, name, character, foreground, background):
        self.name = name
        self.character = character
        self.foreground = foreground
        self.background = background
        self.string = '\x1b[' + foreground + background + character + '\x1b[0m'


class Tiles:
    grass = Tile('grass', '.', '38;2;109;255;188;', '48;2;40;170;50m')
    dirt = Tile('dirt', '.', '38;2;200;200;200;', '48;2;165;75;15m')
    river = Tile('river', '=', '38;2;63;219;255;', '48;2;57;65;202m')
    flower = Tile('flower', '*', '38;2;255;255;0;', '48;2;40;170;50m')
    mountain = Tile('mountain', '^', '38;2;170;103;17;', '48;2;120;57;15m')
    black = Tile('black', ' ', '38;2;0;0;0;', '48;2;0;0;0m')
    stoneWall = Tile('stoneWall', '#', '38;2;137;150;109;', '48;2;64;70;66m')
    stoneFloor = Tile('stoneFloor', '.', '38;2;200;200;200;', '48;2;120;120;120m')
    hudHash = Tile('hudHash', '#', '38;2;255;255;255;', '48;2;0;0;0m')
    hudStar = Tile('hudStar', '*', '38;2;255;255;255;', '48;2;0;0;0m')

    tile_names = [tile for tile in vars().keys() if not tile.startswith('__')]