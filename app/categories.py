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
    RUNE_DAGGER = "Rune Daggers"
    SCEPTRE = "Sceptres"
    STAFF = "Staves"
    TWO_HAND_AXE = "Two Hand Axes"
    TWO_HAND_MACE = "Two Hand Maces"
    TWO_HAND_SWORD = "Two Hand Swords"
    WAND = "Wands"


class GEAR(StrEnum):
    AMULET = "Amulets"
    BELT = "Belts"
    BODY_ARMOUR = "Body Armours"
    BOOTS = "Boots"
    GLOVES = "Gloves"
    HELMET = "Helmets"
    RING = "Rings"


class CHARM(StrEnum):
    ANTIDOTE_CHARM = "Antidote Charm"
    DOUSING_CHARM = "Dousing Charm"
    RUBY_CHARM = "Ruby Charm"
    SAPPHIRE_CHARM = "Sapphire Charm"
    SILVER_CHARM = "Silver Charm"
    STAUNCHING_CHARM = "Staunching Charm"
    STONE_CHARM = "Stone Charm"
    THAWING_CHARM = "Thawing Charm"
    TOPAZ_CHARM = "Topaz Charm"
