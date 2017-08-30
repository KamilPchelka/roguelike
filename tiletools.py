class Tile:
    def __init__(self, name, character, foreground, background, walkable=True):
        self.name = name
        self.character = character
        self.foreground = foreground
        self.background = background
        self.walkable = walkable
        self.string = '\x1b[' + foreground + background + character + '\x1b[0m'


class Tiles:
    grass = Tile('grass', '.', '38;2;109;255;188;', '48;2;40;170;50m', True)
    dirt = Tile('dirt', '.', '38;2;200;200;200;', '48;2;165;75;15m', True)
    river = Tile('river', '=', '38;2;63;219;255;', '48;2;57;65;202m', False)
    flower = Tile('flower', '*', '38;2;255;255;0;', '48;2;40;170;50m', True)
    mountain = Tile('mountain', '^', '38;2;170;103;17;', '48;2;120;57;15m', False)
    black = Tile('black', ' ', '38;2;0;0;0;', '48;2;0;0;0m', False)
    stoneWall = Tile('stoneWall', '#', '38;2;137;150;109;', '48;2;64;70;66m', False)
    stoneFloor = Tile('stoneFloor', '.', '38;2;200;200;200;', '48;2;120;120;120m', True)
    hudHash = Tile('hudHash', '#', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudStar = Tile('hudStar', '*', '38;2;255;255;255;', '48;2;0;0;0m', False)

    tile_names = [tile for tile in vars().keys() if not tile.startswith('__')]


class Enemy(Tile):
    def __init__(self, hp):
        super().__init__('grass', '?', '38;2;109;255;188;', '48;2;40;170;50m', True)
        self.hp = hp


class Hero(Tile):
    def __init__(self, hp, x, y, direction, gold=0):
        super().__init__('player', '@', '38;2;255;255;255;', '48;2;40;170;50m', True)
        self.hp = hp
        self.x = x
        self.y = y
        self.direction = direction
        self.gold = gold

    def update_string(self):
        self.string = '\x1b[' + self.foreground + self.background + self.character + '\x1b[0m'


class Gold(Tile):
    def __init__(self, x, y, value, hero, exist=True):
        super().__init__('gold', '$', '38;2;0;0;0;', '48;2;255;255;0m', True)
        self.x = x
        self.y = y
        self.value = value
        self.exist = exist
        self.hero = hero

    def collision_check(self):
        if self.x == self.hero.x and self.y == self.hero.y:
            self.hero.gold += self.value
            self.exist = False