"""A collection of all the categorical values used throughout the code"""

from enum import StrEnum


class COLOR(StrEnum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    BROWN = "Brown"
    WHITE = "White"
    YELLOW = "Yellow"
    CYAN = "Cyan"
    GREY = "Grey"
    ORANGE = "Orange"
    PINK = "Pink"
    PURPLE = "Purple"


class SHAPE(StrEnum):
    CIRCLE = "Circle"
    DIAMOND = "Diamond"
    HEXAGON = "Hexagon"
    SQUARE = "Square"
    STAR = "Star"
    TRIANGLE = "Triangle"
    CROSS = "Cross"
    MOON = "Moon"
    RAINDROP = "Raindrop"
    KITE = "Kite"
    PENTAGON = "Pentagon"
    UPSIDE_DOWN_HOUSE = "UpsideDownHouse"


class SIZE(StrEnum):
    LARGE = "0"
    MEDIUM = "1"
    SMALL = "2"


class BASIC_SOUND(StrEnum):
    DISABLED = "None"
    CYMBAL = "1"
    GUN = "2"
    BELL = "3"
    ROTATION = "4"
    ELECTRICITY = "5"
    NEEDLE = "6"
    RIPPLE = "7"
    INVERTED_RIPPLE = "8"
    SLOW_RIPPLE = "9"
    TINK = "10"
    PISTOL = "11"
    METRONOME = "12"
    TAMBOURINE = "13"
    SLOW_TREMBLE = "14"
    TREMBLE = "15"
    PUNCH = "16"


class VOLUME(StrEnum):
    QUIET = "25"
    MEDIUM = "100"
    LOUD = "200"


class RGB(StrEnum):
    BLACK = "0 0 0"
    WHITE = "255 255 255"
    RED = "255 0 0"
    GREEN = "0 255 0"
    BLUE = "0 0 255"
    YELLOW = "255 255 0"
    ORANGE = "255 100 0"
    PINK = "255 0 255"
    PURPLE = "200 0 255"
    CYAN = "0 255 255"
    GREY = "150 150 150"


class FONT_SIZE(StrEnum):
    SMALL = "15"
    MEDIUM = "30"
    LARGE = "45"


class RARITY(StrEnum):
    NORMAL = "normal"
    MAGIC = "magic"
    RARE = "rare"
    UNIQUE = "unique"


class TIER(StrEnum):
    COMMON = "COMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"


class OPERATOR(StrEnum):
    EQUAL = "="
    NOT_EQUAL = "!="
    LTE = "<="
    LT = "<"
    GTE = ">="
    GT = ">"
    EXACT = "=="


class WEAPON(StrEnum):
    BOW = "Bows"
    CLAW = "Claws"
    CROSSBOW = "Crossbows"
    DAGGER = "Daggers"
    FISHING_ROD = "Fishing Rods"
    FLAIL = "Flails"
    ONE_HAND_AXE = "One Hand Axes"
    ONE_HAND_MACE = "One Hand Maces"
    ONE_HAND_SWORD = "One Hand Swords"
    SCEPTRE = "Sceptres"
    SPEAR = "Spears"
    STAFF = "Staves"
    TRAP = "Traps"
    TWO_HAND_AXE = "Two Hand Axes"
    TWO_HAND_MACE = "Two Hand Maces"
    TWO_HAND_SWORD = "Two Hand Swords"
    QUARTERSTAFF = "Quarterstaves"
    WAND = "Wands"


class OFFHAND(StrEnum):
    QUIVER = "Quivers"
    SHIELD = "Shields"


class JEWELRY(StrEnum):
    AMULET = "Amulets"
    BELT = "Belts"
    RING = "Rings"


class GEAR(StrEnum):
    AMULET = "Amulets"
    BELT = "Belts"
    BODY_ARMOUR = "Body Armours"
    BOOTS = "Boots"
    GLOVES = "Gloves"
    HELMET = "Helmets"
    RING = "Rings"


class CHARM(StrEnum):
    ANTIDOTE = "Antidote Charm"
    DOUSING = "Dousing Charm"
    RUBY = "Ruby Charm"
    SAPPHIRE = "Sapphire Charm"
    SILVER = "Silver Charm"
    STAUNCHING = "Staunching Charm"
    STONE = "Stone Charm"
    THAWING = "Thawing Charm"
    TOPAZ = "Topaz Charm"


class FLASK(StrEnum):
    LIFE = "Life Flask"
    MANA = "Mana Flask"


class LIFE_FLASK(StrEnum):
    # https://poe2db.tw/us/Life_Flasks#LifeFlasksItem
    LESSER = "Lesser Life Flask"
    MEDIUM = "Medium Life Flask"
    GREATER = "Greater Life Flask"
    GRAND = "Grand Life Flask"
    GIANT = "Giant Life Flask"
    COLOSSAL = "Colossal Life Flask"
    GARGANTUAN = "Gargantuan Life Flask"
    TRANSCENDENT = "Transcendent Life Flask"
    ULTIMATE = "Ultimate Life Flask"


class MANA_FLASK(StrEnum):
    # TODO
    pass


class AMULET(StrEnum):
    # https://poe2db.tw/us/Amulets#AmuletsItem
    CRIMSON = "Crimson Amulet"
    AZURE = "Azure Amulet"
    AMBER = "Amber Amulet"
    JADE = "Jade Amulet"
    LAPIS = "Lapis Amulet"
    LUNAR = "Lunar Amulet"
    BLOODSTONE = "Bloodstone Amulet"
    STELLAR = "Stellar Amulet"
    SOLAR = "Solar Amulet"
    GOLD = "Gold Amulet"


class BELT(StrEnum):
    # https://poe2db.tw/us/Belts#BeltsItem
    GOLDEN_OBI = "Golden Obi"
    RAWHIDE = "Rawhide Belt"
    LINEN = "Linen Belt"
    WIDE = "Wide Belt"
    LONG = "Long Belt"
    PLATE = "Plate Belt"
    ORNATE = "Ornate Belt"
    MAIL = "Mail Belt"
    DOUBLE = "Double Belt"
    HEAVY = "Heavy Belt"
    UTILITY = "Utility Belt"
    FINE = "Fine Belt"


class RING(StrEnum):
    # https://poe2db.tw/us/Rings#RingsItem
    GOLDEN_HOOP = "Golden Hoop"
    IRON = "Iron Ring"
    LAZULI = "Lazuli Ring"
    RUBY = "Ruby Ring"
    SAPPHIRE = "Sapphire Ring"
    TOPAZ = "Topaz Ring"
    AMETHYST = "Amethyst Ring"
    EMERALD = "Emerald Ring"
    PEARL = "Pearl Ring"
    PRISMATIC = "Prismatic Ring"
    GOLD = "Gold Ring"
    UNSET = "Unset Ring"
    BREACH = "Breach Ring"


class JEWEL(StrEnum):
    # https://poe2db.tw/us/Jewels#JewelsItem
    RUBY = "Ruby Jewel"
    EMERALD = "Emerald Jewel"
    SAPPHERE = "Sapphire Jewel"
    DIAMOND = "Diamond Jewel"
    TIME_LOST_RUBY = "Time-Lost Ruby"
    TIME_LOST_EMERALD = "Time-Lost Emerald"
    TIME_LOST_SAPPHIRE = "Time-Lost Sapphire"
    TIME_LOST_DIAMOND = "Time-Lost Diamond"


class STAFF(StrEnum):
    # https://poe2db.tw/us/Staves#StavesItem
    ASHEN = "Ashen Staff"
    GELID = "Gelid Staff"
    VOLTAIC = "Voltaic Staff"
    SPRIGGAN = "Spriggan Staff"
    PYROPHYTE = "Pyrophyte Staff"
    CHIMING = "Chiming Staff"
    RENDING = "Rending Staff"
    REAPING = "Reaping Staff"
    ICICLE = "Icicle Staff"
    ROARING = "Roaring Staff"
    PARALYSING = "Paralysing Staff"
    CLERIC = "Cleric Staff"
    DARK = "Dark Staff"


class BODY_ARMOUR(StrEnum):
    # https://poe2db.tw/us/Body_Armours#BodyArmoursItem
    class STR(StrEnum):
        RUSTED_CUIRASS = "Rusted Cuirass"
        FUR_PLATE = "Fur Plate"
        IRON_CUIRASS = "Iron Cuirass"
        RAIDER_PLATE = "Raider Plate"
        MARAKETH_CUIRASS = "Maraketh Cuirass"
        STEEL_PLATE = "Steel Plate"
        FULL_PLATE = "Full Plate"
        VAAL_CUIRASS = "Vaal Cuirass"
        JUGGERNAUT_PLATE = "Juggernaut Plate"
        CHIEFTAIN_CUIRASS = "Chieftain Cuirass"
        COLOSSEUM_PLATE = "Colosseum Plate"
        CHAMPION_CUIRASS = "Champion Cuirass"
        GLORIOUS_PLATE = "Glorious Plate"
        CONQUEROR_PLATE = "Conqueror Plate"
        ABYSSAL_CUIRASS = "Abyssal Cuirass"

    class DEX(StrEnum):
        LEATHER_VEST = "Leather Vest"
        QUILTED_VEST = "Quilted Vest"
        PATHFINDER_COAT = "Pathfinder Coat"
        SHROUDED_VEST = "Shrouded Vest"
        RHOAHIDE_VEST = "Rhoahide Vest"
        STUDDED_VEST = "Studded Vest"
        SCOUTS_VEST = "Scout's Vest"
        SERPENTSCALE_VEST = "Serpentscale Vest"
        CORSAIR_VEST = "Corsair Vest"
        SMUGGLER_COAT = "Smuggler Coat"
        STRIDER_VEST = "Strider Vest"
        HARDLEATHER_COAT = "Hardleather Coat"
        EXQUISITE_VEST = "Exquisite Vest"
        MAIL_COAT = "Mail Coat"
        ARMOURED_VEST = "Armoured Vest"

    class INT(StrEnum):
        # TODO
        pass

    class STR_DEX(StrEnum):
        # TODO
        pass

    class STR_INT(StrEnum):
        # TODO
        pass

    class DEX_INT(StrEnum):
        # TODO
        pass


class HELMET(StrEnum):
    class STR(StrEnum):
        # TODO
        pass

    class DEX(StrEnum):
        # TODO
        pass

    class INT(StrEnum):
        # TODO
        pass

    class STR_DEX(StrEnum):
        # TODO
        pass

    class STR_INT(StrEnum):
        # TODO
        pass

    class DEX_INT(StrEnum):
        # TODO
        pass


class BOOTS(StrEnum):
    class STR(StrEnum):
        # TODO
        pass

    class DEX(StrEnum):
        # TODO
        pass

    class INT(StrEnum):
        # TODO
        pass

    class STR_DEX(StrEnum):
        # TODO
        pass

    class STR_INT(StrEnum):
        # TODO
        pass

    class DEX_INT(StrEnum):
        # TODO
        pass


class GLOVES(StrEnum):
    class STR(StrEnum):
        # TODO
        pass

    class DEX(StrEnum):
        # TODO
        pass

    class INT(StrEnum):
        # TODO
        pass

    class STR_DEX(StrEnum):
        # TODO
        pass

    class STR_INT(StrEnum):
        # TODO
        pass

    class DEX_INT(StrEnum):
        # TODO
        pass
