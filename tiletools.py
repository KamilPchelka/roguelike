class Tile:
    def __init__(self, name, character, foreground, background, walkable=True):
        self.name = name
        self.character = character
        self.foreground = foreground
        self.background = background
        self.walkable = walkable
        self.string = '\x1b[' + foreground + background + character + '\x1b[0m'

    def update_string(self):
        self.string = '\x1b[' + self.foreground + self.background + self.character + '\x1b[0m'


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
    rabbit = Tile('rabbit', 'a', '38;2;255;255;255;', '48;2;40;170;50m', False)
    blood = Tile('blood', ' ', '38;2;255;0;0;', '48;2;255;0;0m', True)
    item = Tile('item', '?', '38;2;255;0;127;', '48;2;40;170;50m', True)
    gate = Tile('gate', '=', '38;2;200;200;200;', '48;2;120;120;120m', False)

    hudT = Tile('hudT', 'T', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudh = Tile('hudh', 'h', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudi = Tile('hudi', 'i', '38;2;255;255;255;', '48;2;0;0;0m', False)
    huds = Tile('huds', 's', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudy = Tile('hudy', 'y', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudo = Tile('hudo', 'o', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudu = Tile('hudu', 'u', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudn = Tile('hudn', 'n', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudm = Tile('hudm', 'm', '38;2;255;255;255;', '48;2;0;0;0m', False)
    huddot = Tile('huddot', '.', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudUnderscore = Tile('hudUnderscore', '_', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudBackslash = Tile('hudBackslash', '\\', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudSlash = Tile('hudSlash', '/', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudEquals = Tile('hudEquals', '=', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudMinus = Tile('hudMinus', '-', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudBrack1 = Tile('hudBrack1', '[', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudBrack2 = Tile('hudBrack2', ']', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudLine = Tile('hudLine', '|', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudBrack3 = Tile('hudBrack3', '(', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudBrack4 = Tile('hudBrack4', ')', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudApo = Tile('hudApo', '\'', '38;2;255;255;255;', '48;2;0;0;0m', False)
    hudGravis = Tile('hudGravis', '`', '38;2;255;255;255;', '48;2;0;0;0m', False)
    
    tile_names = [tile for tile in vars().keys() if not tile.startswith('__')]


class Enemy(Tile):
    def __init__(self, hp):
        super().__init__('grass', '?', '38;2;109;255;188;', '48;2;40;170;50m', True)
        self.hp = hp


class Hero(Tile):
    inventory = {}
    player_name = ''
    def __init__(self, hp, x, y, direction, gold=0, rabbits_killed=0):
        super().__init__('player', '@', '38;2;255;255;255;', '48;2;40;170;50m', True)
        self.hp = hp
        self.x = x
        self.y = y
        self.direction = direction
        self.gold = gold
        self.rabbits_killed = rabbits_killed


class Gold(Tile):
    def __init__(self, x, y, value, hero, exist=True):
        super().__init__('gold', '$', '38;2;0;0;0;', '48;2;255;255;0m', True)
        self.x = x
        self.y = y
        self.value = value
        self.exist = exist
        self.hero = hero

    def collision_check(self):
        if self.x == self.hero.x and self.y == self.hero.y and self.exist:
            self.hero.gold += self.value
            self.exist = False


class Rabbit(Tile):
    def __init__(self, x, y, alive=True):
        super().__init__('rabbit', 'a', '38;2;255;255;255;', '48;2;40;170;50m', False)
        self.x = x
        self.y = y
        self.alive = alive

    def collision_check(self, sword_x, sword_y):
        if self.x == self.sword_x and self.y == self.sword_y:
            self.alive = False