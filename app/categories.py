"""A collection of all the categorical values used throughout the code"""

from enum import StrEnum, IntEnum


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
    FOCUS = "FOCI"


class FISHING_ROD(StrEnum):
    # https://poe2db.tw/us/Fishing_Rods#FishingRodsItem
    ROD = "Fishing Rod"


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


class SPEAR:
    # https://poe2db.tw/us/Spears#SpearsItem
    HARDWOOD = "Hardwood Spear"
    IRONHEAD = "Ironhead Spear"
    HUNTING = "Hunting Spear"
    WINGED = "Winged Spear"
    # TODO: Add more spear types


class BOW(StrEnum):
    # https://poe2db.tw/us/Bows#BowsItem
    CRUDE = "Crude Bow"
    SHORT = "Shortbow"
    WARDEN = "Warden Bow"
    RECURVE = "Recurve Bow"
    COMPOSITE = "Composite Bow"
    DUALSTRING = "Dualstring Bow"
    CULTIST = "Cultist Bow"
    ZEALOT = "Zealot Bow"
    ARTILLERY = "Artillery Bow"
    TRIBAL = "Tribal Bow"
    GREAT = "Greatbow"
    DOUBLE_LIMB = "Double Limb Bow"
    HEAVY = "Heavy Bow"


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
    CHARM = "Charms"


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
    GOLDEN = "Golden Charm"


class FLASK(StrEnum):
    LIFE = "Life Flasks"
    MANA = "Mana Flasks"


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
    # https://poe2db.tw/us/Mana_Flasks#ManaFlasksItem
    LESSER = "Lesser Mana Flask"
    MEDIUM = "Medium Mana Flask"
    GREATER = "Greater Mana Flask"
    GRAND = "Grand Mana Flask"
    GIANT = "Giant Mana Flask"
    COLOSSAL = "Colossal Mana Flask"
    GARGANTUAN = "Gargantuan Mana Flask"
    TRANSCENDENT = "Transcendent Mana Flask"
    ULTIMATE = "Ultimate Mana Flask"


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
    RUBY = "Ruby"
    EMERALD = "Emerald"
    SAPPHIRE = "Sapphire"
    DIAMOND = "Diamond"
    TIME_LOST_RUBY = "Time-Lost Ruby"
    TIME_LOST_EMERALD = "Time-Lost Emerald"
    TIME_LOST_SAPPHIRE = "Time-Lost Sapphire"
    TIME_LOST_DIAMOND = "Time-Lost Diamond"


class GEM(StrEnum):
    SKILL = "Uncut Skill Gem"
    SUPPORT = "Uncut Support Gem"
    SPIRIT = "Uncut Spirit Gem"


class RUNE(StrEnum):
    IRON = "Iron Rune"
    DESERT = "Desert Rune"
    GLACIAL = "Glacial Rune"
    STORM = "Storm Rune"
    BODY = "Body Rune"
    MIND = "Mind Rune"
    VISION = "Vision Rune"
    REBIRTH = "Rebirth Rune"
    INSPIRATION = "Inspiration Rune"
    STONE = "Stone Rune"


class SOUL_CORE(StrEnum):
    TACATI = "Soul Core of Tacati"
    TOPOTANTE = "Soul Core of Topotante"
    OPILOTI = "Soul Core of Opiloti"
    JIQUANI = "Soul Core of Jiquani"
    ZALATL = "Soul Core of Zalatl"
    CITAQUALOTL = "Soul Core of Citaqualotl"
    PUHUARTE = "Soul Core of Puhuarte"
    TZAMOTO = "Soul Core of Tzamoto"
    XOPEC = "Soul Core of Xopec"
    QUIPOLATL = "Soul Core of Quipolatl"
    TICABA = "Soul Core of Ticaba"
    ATMOHUA = "Soul Core of Atmohua"
    CHOLOTL = "Soul Core of Cholotl"
    ZANTIPI = "Soul Core of Zantipi"
    AZCAPA = "Soul Core of Azcapa"


class CURRENCY(StrEnum):
    # https://poe2db.tw/us/Currency#CurrencyItem
    WISDOM = "Scroll of Wisdom"

    TRANSMUTATION = "Orb of Transmutation"
    AUGMENTATION = "Orb of Augmentation"
    ALCHEMY = "Orb of Alchemy"
    REGAL = "Regal Orb"
    CHAOS = "Chaos Orb"
    VAAL = "Vaal Orb"
    EXALTED = "Exalted Orb"
    DIVINE = "Divine Orb"
    ANNULMENT = "Orb of Annulment"
    CHANCE = "Orb of Chance"
    MIRROR = "Mirror of Kalandra"

    ARCANIST = "Arcanist's Etcher"
    ARMOURER = "Armourer's Scrap"
    BLACKSMITH = "Blacksmith's Whetstone"
    ARTIFICER = "Artificer's Orb"
    GEMCUTTER = "Gemcutter's Prism"
    GLASSBLOWER = "Glassblower's Bauble"

    LESSER_JEWELLER = "Lesser Jeweller's Orb"
    GREATER_JEWELLER = "Greater Jeweller's Orb"
    PERFECT_JEWELLER = "Perfect Jeweller's Orb"

    ARTIFICERS_SHARD = "Artificer's Shard"
    TRANSMUTATION_SHARD = "Transmutation Shard"
    REGAL_SHARD = "Regal Shard"
    CHANCE_SHARD = "Chance Shard"


class ARTIFACT(StrEnum):
    EXOTIC_COINAGE = "Exotic Coinage"
    CIRCLE = "Broken Circle Artifact"
    SCYTHE = "Black Scythe Artifact"
    ORDER = "Order Artifact"
    SUN = "Sun Artifact"


class SEKHEMA_KEY(StrEnum):
    BRONZE = "Bronze Key"
    SILVER = "Silver Key"
    GOLD = "Gold Key"


class ESSENCE(StrEnum):
    BODY = "Essence of the Body"
    MIND = "Essence of the Mind"
    ENHANCEMENT = "Essence of Enhancement"
    TORMENT = "Essence of Torment"
    FLAMES = "Essence of Flames"
    ICE = "Essence of Ice"
    ELECTRICITY = "Essence of Electricity"
    RUIN = "Essence of Ruin"
    BATTLE = "Essence of Battle"
    SORCERY = "Essence of Sorcery"
    HASTE = "Essence of Haste"
    INFINITE = "Essence of the Infinite"


class GREATER_ESSENCE(StrEnum):
    BODY = "Greater Essence of the Body"
    MIND = "Greater Essence of the Mind"
    ENHANCEMENT = "Greater Essence of Enhancement"
    TORMENT = "Greater Essence of Torment"
    FLAMES = "Greater Essence of Flames"
    ICE = "Greater Essence of Ice"
    ELECTRICITY = "Greater Essence of Electricity"
    RUIN = "Greater Essence of Ruin"
    BATTLE = "Greater Essence of Battle"
    SORCERY = "Greater Essence of Sorcery"
    HASTE = "Greater Essence of Haste"
    INFINITE = "Greater Essence of the Infinite"


class EMOTION(StrEnum):
    DESPAIR = "Distilled Despair"
    DISGUST = "Distilled Disgust"
    ENVY = "Distilled Envy"
    FEAR = "Distilled Fear"
    GREED = "Distilled Greed"
    GUILT = "Distilled Guilt"
    IRE = "Distilled Ire"
    ISOLATION = "Distilled Isolation"
    PARANOIA = "Distilled Paranoia"
    SUFFERING = "Distilled Suffering"


class CATALYST(StrEnum):
    FLESH = "Flesh Catalyst"
    NEURAL = "Neural Catalyst"
    CARAPACE = "Carapace Catalyst"
    UUL_NETOL = "Uul-Netol's Catalyst"
    XOPH = "Xoph's Catalyst"
    TUL = "Tul's Catalyst"
    ESH = "Esh's Catalyst"
    CHAYULA = "Chayula's Catalyst"
    REAVER = "Reaver Catalyst"
    SIBILANT = "Sibilant Catalyst"
    SKITTERING = "Skittering Catalyst"
    ADAPTIVE = "Adaptive Catalyst"


class OMEN(StrEnum):
    AMELIORATION = "Omen of Amelioration"
    CORRUPTION = "Omen of Corruption"
    DEXTRAL_ALCHEMY = "Omen of Dextral Alchemy"
    DEXTRAL_ANNULMENT = "Omen of Dextral Annulment"
    DEXTRAL_CORONATION = "Omen of Dextral Coronation"
    DEXTRAL_ERASURE = "Omen of Dextral Erasure"
    DEXTRAL_EXALTAION = "Omen of Dextral Exaltation"
    GREATER_ANNULMENT = "Omen of Greater Annulment"
    GREATER_EXALTAION = "Omen of Greater Exaltation"
    REFRESHMENT = "Omen of Refreshment"
    RESURGENCE = "Omen of Resurgence"
    SINISTRAL_ALCHEMY = "Omen of Sinistral Alchemy"
    SINISTRAL_ANNULMENT = "Omen of Sinistral Annulment"
    SINISTRAL_CORONATION = "Omen of Sinistral Coronation"
    SINISTRAL_ERASURE = "Omen of Sinistral Erasure"
    SINISTRAL_EXALTATION = "Omen of Sinistral Exaltation"
    WHITTLING = "Omen of Whittling"


class SPLINTER(StrEnum):
    SIMULACRUM = "Simulacrum Splinter"
    BREACH = "Breach Splinter"


class INVITATION(StrEnum):
    RITUAL = "An Audience with the King"
    EXPEDITION = "Expedition Logbook"
    BREACH = "Breachstone"
    SIMULACRUM = "Simulacrum"

    ANCIENT = "Ancient Crisis Fragment"
    FADED = "Faded Crisis Fragment"
    WEATHERED = "Weathered Crisis Fragment"

    COWARDLY = "Cowardly Fate"
    DEADLY = "Deadly Fate"
    VICTORIOUS = "Victorious Fate"


class TRIAL(StrEnum):
    ULTIMATUM = "Inscribed Ultimatum"
    BARYA = "Djinn Barya"


class AREA_LEVEL(IntEnum):
    # TODO: Find exact area levels
    ACT_1 = 1
    ACT_2 = 16
    ACT_3 = 33
    ACT_4 = 45
    ACT_5 = 51
    ACT_6 = 58
    WHITE_MAPS = 65
    YELLOW_MAPS = 70
    RED_MAPS = 75
    ENDGAME = 79
