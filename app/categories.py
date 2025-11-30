"""A collection of all the categorical values used throughout the code"""

from enum import StrEnum


class COLOR(StrEnum):
    RED = "Red"
    CYAN = "Cyan"
    GREY = "Grey"
    BLUE = "Blue"
    PINK = "Pink"
    GREEN = "Green"
    BROWN = "Brown"
    WHITE = "White"
    YELLOW = "Yellow"
    ORANGE = "Orange"
    PURPLE = "Purple"


class SHAPE(StrEnum):
    STAR = "Star"
    MOON = "Moon"
    KITE = "Kite"
    CROSS = "Cross"
    CIRCLE = "Circle"
    SQUARE = "Square"
    DIAMOND = "Diamond"
    HEXAGON = "Hexagon"
    TRIANGLE = "Triangle"
    RAINDROP = "Raindrop"
    PENTAGON = "Pentagon"
    UPSIDE_DOWN_HOUSE = "UpsideDownHouse"


class SIZE(StrEnum):
    SMALL = "2"
    MEDIUM = "1"
    LARGE = "0"


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
    RED = "255 0 0"
    BLACK = "0 0 0"
    BLUE = "0 0 255"
    GREEN = "0 255 0"
    PINK = "255 0 255"
    CYAN = "0 255 255"
    YELLOW = "255 255 0"
    ORANGE = "255 100 0"
    GREY = "150 150 150"
    PURPLE = "200 0 255"
    WHITE = "255 255 255"


class FONT_SIZE(StrEnum):
    SMALL = "15"
    MEDIUM = "30"
    LARGE = "45"


class OPERATOR(StrEnum):
    GT = ">"
    LT = "<"
    LTE = "<="
    GTE = ">="
    EQUAL = "="
    EXACT = "=="
    NOT_EQUAL = "!="


class RARITY(StrEnum):
    NORMAL = "normal"
    MAGIC = "magic"
    RARE = "rare"
    UNIQUE = "unique"


# Custom definitions


class TIER(StrEnum):
    COMMON = "COMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"


class ARMOUR(StrEnum):
    BOOTS = "Boots"
    GLOVES = "Gloves"
    HELMET = "Helmets"
    BODY = "Body Armours"


class WEAPON(StrEnum):
    BOW = "Bows"
    CLAW = "Claws"
    TRAP = "Traps"
    WAND = "Wands"
    FLAIL = "Flails"
    STAFF = "Staves"
    SPEAR = "Spears"
    DAGGER = "Daggers"
    SCEPTRE = "Sceptres"
    CROSSBOW = "Crossbows"
    FISHING_ROD = "Fishing Rods"
    ONE_HAND_AXE = "One Hand Axes"
    TWO_HAND_AXE = "Two Hand Axes"
    QUARTERSTAFF = "Quarterstaves"
    ONE_HAND_MACE = "One Hand Maces"
    TWO_HAND_MACE = "Two Hand Maces"
    ONE_HAND_SWORD = "One Hand Swords"
    TWO_HAND_SWORD = "Two Hand Swords"


class OFFHAND(StrEnum):
    FOCUS = "Foci"
    QUIVER = "Quivers"
    SHIELD = "Shields"
    BUCKLER = "Bucklers"


class JEWELRY(StrEnum):
    BELT = "Belts"
    RING = "Rings"
    AMULET = "Amulets"


class GEAR(StrEnum):
    BELT = "Belts"
    RING = "Rings"
    BOOTS = "Boots"
    CHARM = "Charms"
    GLOVES = "Gloves"
    HELMET = "Helmets"
    AMULET = "Amulets"
    BODY_ARMOUR = "Body Armours"


class FLASK(StrEnum):
    LIFE = "Life Flasks"
    MANA = "Mana Flasks"


class JEWEL(StrEnum):
    # https://poe2db.tw/us/Jewels#JewelsItem
    RUBY = "Ruby"
    DIAMOND = "Diamond"
    EMERALD = "Emerald"
    SAPPHIRE = "Sapphire"
    TIME_LOST_RUBY = "Time-Lost Ruby"
    TIME_LOST_DIAMOND = "Time-Lost Diamond"
    TIME_LOST_EMERALD = "Time-Lost Emerald"
    TIME_LOST_SAPPHIRE = "Time-Lost Sapphire"


class GEM(StrEnum):
    SKILL = "Uncut Skill Gems"
    SPIRIT = "Uncut Spirit Gems"
    SUPPORT = "Uncut Support Gems"


class LINEAGE_SUPPORT(StrEnum):
    XOPH_PYRE = "Xoph's Pyre"
    TACATI_IRE = "Tacati's Ire"
    AHN_CITADEL = "Ahn's Citadel"
    ARJUN_MEDAL = "Arjun's Medal"
    PIETY_MERCY = "Piety's Mercy"
    UHTRED_OMEN = "Uhtred's Omen"
    BRUTUS_BRAIN = "Brutus' Brain"
    PAQUATE_PACT = "Paquate's Pact"
    KAOM_MADNESS = "Kaom's Madness"
    SIONE_TEMPER = "Sione's Temper"
    RAKIATA_FLOW = "Rakiata's Flow"
    ESH_RADIANCE = "Esh's Radiance"
    KURGAL_LEASH = "Kurgal's Leash"
    AMANAMU_TITHE = "Amanamu's Tithe"
    ARAKAALI_LUST = "Arakaali's Lust"
    TUL_STILLNESS = "Tul's Stillness"
    UHTRED_EXODUS = "Uhtred's Exodus"
    UHTRED_AUGURY = "Uhtred's Augury"
    ATZIRI_ALLURE = "Atziri's Allure"
    DIALLA_DESIRE = "Dialla's Desire"
    URUK_SMELTING = "Uruk's Smelting"
    AILITH_CHIMES = "Ailith's Chimes"
    RATHA_ASSAULT = "Ratha's Assault"
    TECROD_REVENGE = "Tecrod's Revenge"
    TAWHOA_TENDING = "Tawhoa's Tending"
    DOEDRE_UNDOING = "Doedre's Undoing"
    IXCHEL_TORMENT = "Ixchel's Torment"
    ZAROKH_REFRAIN = "Zarokh's Refrain"
    DARESSO_PASSION = "Daresso's Passion"
    ROMIRA_REQUITAL = "Romira's Requital"
    EINHAR_BEASTRITE = "Einhar's Beastrite"
    RIGWALD_FEROCITY = "Rigwald's Ferocity"
    GARUKHAN_RESOLVE = "Garukhan's Resolve"
    KALISA_CRESCENDO = "Kalisa's Crescendo"
    KULEMAK_DOMINION = "Kulemak's Dominion"
    ARBITER_IGNITION = "Arbiter's Ignition"
    UUL_NETOL_EMBRACE = "Uul-Netol's Embrace"
    VARASHTA_BLESSING = "Varashta's Blessing"
    VILENTA_PROPULSION = "Vilenta's Propulsion"
    ATALUI_BLOODLETTING = "Atalui's Bloodletting"


class LESSER_RUNE(StrEnum):
    IRON = "Lesser Iron Rune"
    BODY = "Lesser Body Rune"
    MIND = "Lesser Mind Rune"
    STONE = "Lesser Stone Rune"
    ADEPT = "Lesser Adept Rune"
    STORM = "Lesser Storm Rune"
    VISION = "Lesser Vision Rune"
    ROBUST = "Lesser Robust Rune"
    DESERT = "Lesser Desert Rune"
    GLACIAL = "Lesser Glacial Rune"
    RESOLVE = "Lesser Resolve Rune"
    REBIRTH = "Lesser Rebirth Rune"
    TEMPERED = "Lesser Tempered Rune"
    INSPIRATION = "Lesser Inspiration Rune"


class RUNE(StrEnum):
    BODY = "Body Rune"
    IRON = "Iron Rune"
    MIND = "Mind Rune"
    STONE = "Stone Rune"
    ADEPT = "Adept Rune"
    STORM = "Storm Rune"
    DESERT = "Desert Rune"
    VISION = "Vision Rune"
    GLACIAL = "Glacial Rune"
    ROBUST = "Robust Rune"
    REBIRTH = "Rebirth Rune"
    RESOLVE = "Resolve Rune"
    TEMPERED = "Tempered Rune"
    INSPIRATION = "Inspiration Rune"


class GREATER_RUNE(StrEnum):
    BODY = "Greater Body Rune"
    IRON = "Greater Iron Rune"
    MIND = "Greater Mind Rune"
    STONE = "Greater Stone Rune"
    ADEPT = "Greater Adept Rune"
    STORM = "Greater Storm Rune"
    DESERT = "Greater Desert Rune"
    GLACIAL = "Greater Glacial Rune"
    VISION = "Greater Vision Rune"
    ROBUST = "Greater Robust Rune"
    REBIRTH = "Greater Rebirth Rune"
    RESOLVE = "Greater Resolve Rune"
    TEMPERED = "Greater Tempered Rune"
    TITHING = "Greater Rune of Tithing"
    ALACRITY = "Greater Rune of Alacrity"
    NOBILITY = "Greater Rune of Nobility"
    INSPIRATION = "Greater Inspiration Rune"
    LEADERSHIP = "Greater Rune of Leadership"


class TALISMAN(StrEnum):
    OX = "Ox Talisman"
    CAT = "Cat Talisman"
    OWL = "Owl Talisman"
    FOX = "Fox Talisman"
    BOAR = "Boar Talisman"
    BEAR = "Bear Talisman"
    WOLF = "Wolf Talisman"
    STAG = "Stag Talisman"
    RABBIT = "Rabbit Talisman"
    SERPENT = "Serpent Talisman"
    PRIMATE = "Primate Talisman"


class SOUL_CORE(StrEnum):
    XOPEC = "Soul Core of Xopec"
    ZALATL = "Soul Core of Zalatl"
    TACATI = "Soul Core of Tacati"
    TICABA = "Soul Core of Ticaba"
    AZCAPA = "Soul Core of Azcapa"
    JIQUANI = "Soul Core of Jiquani"
    OPILOTI = "Soul Core of Opiloti"
    CHOLOTL = "Soul Core of Cholotl"
    TZAMOTO = "Soul Core of Tzamoto"
    ATMOHUA = "Soul Core of Atmohua"
    ZANTIPI = "Soul Core of Zantipi"
    PUHUARTE = "Soul Core of Puhuarte"
    QUIPOLATL = "Soul Core of Quipolatl"
    TOPOTANTE = "Soul Core of Topotante"
    CITAQUALOTL = "Soul Core of Citaqualotl"


class CURRENCY(StrEnum):
    # https://poe2db.tw/us/Stackable_Currency
    WISDOM = "Scroll of Wisdom"

    TRANSMUTATION = "Orb of Transmutation"
    GREATER_TRANSMUTATION = "Greater Orb of Transmutation"
    PERFECT_TRANSMUTATION = "Perfect Orb of Transmutation"

    AUGMENTATION = "Orb of Augmentation"
    GREATER_AUGMENTATION = "Greater Orb of Augmentation"
    PERFECT_AUGMENTATION = "Perfect Orb of Augmentation"

    REGAL = "Regal Orb"
    GREATER_REGAL = "Greater Regal Orb"
    PERFECT_REGAL = "Perfect Regal Orb"

    CHAOS = "Chaos Orb"
    GREATER_CHAOS = "Greater Chaos Orb"
    PERFECT_CHAOS = "Perfect Chaos Orb"

    EXALTED = "Exalted Orb"
    GREATER_EXALTED = "Greater Exalted Orb"
    PERFECT_EXALTED = "Perfect Exalted Orb"

    VAAL = "Vaal Orb"
    ALCHEMY = "Orb of Alchemy"

    DIVINE = "Divine Orb"
    CHANCE = "Orb of Chance"
    FRACTURING = "Fracturing Orb"
    ANNULMENT = "Orb of Annulment"
    MIRROR = "Mirror of Kalandra"
    HINEKORA = "Hinekora's Lock"

    ARCANIST = "Arcanist's Etcher"
    ARMOURER = "Armourer's Scrap"
    ARTIFICER = "Artificer's Orb"
    GEMCUTTER = "Gemcutter's Prism"
    GLASSBLOWER = "Glassblower's Bauble"
    BLACKSMITH = "Blacksmith's Whetstone"

    LESSER_JEWELLER = "Lesser Jeweller's Orb"
    GREATER_JEWELLER = "Greater Jeweller's Orb"
    PERFECT_JEWELLER = "Perfect Jeweller's Orb"

    REGAL_SHARD = "Regal Shard"
    CHANCE_SHARD = "Chance Shard"
    ARTIFICERS_SHARD = "Artificer's Shard"
    TRANSMUTATION_SHARD = "Transmutation Shard"


class TABLET(StrEnum):
    NORMAL = "Precursor Tablet"
    BOSS = "Overseer Precursor Tablet"
    RITUAL = "Ritual Precursor Tablet"
    BREACH = "Breach Precursor Tablet"
    DELIRIUM = "Delirium Precursor Tablet"
    EXPEDITION = "Expedition Precursor Tablet"


class EXPEDITION(StrEnum):
    SUN = "Sun Artifact"
    ORDER = "Order Artifact"
    SCYTHE = "Black Scythe Artifact"
    CIRCLE = "Broken Circle Artifact"
    EXOTIC_COINAGE = "Exotic Coinage"

    LOGBOOK = "Expedition Logbook"


class ABYSS(StrEnum):
    GNAWED_RIB = "Gnawed Rib"
    ANCIENT_RIB = "Ancient Rib"
    PRESERVED_RIB = "Preserved Rib"
    GNAWED_JAWBONE = "Gnawed Jawbone"
    ANCIENT_JAWBONE = "Ancient Jawbone"
    PRESERVED_JAWBONE = "Preserved Jawbone"
    PRESERVED_CRANIUM = "Preserved Cranium"
    GNAWED_COLLARBONE = "Gnawed Collarbone"
    ANCIENT_COLLARBONE = "Ancient Collarbone"
    PRESERVED_VERTEBRAE = "Preserved Vertebrae"
    PRESERVED_COLLARBONE = "Preserved Collarbone"

    TECROD_GAZE = "Tecrod's Gaze"
    KURGAL_GAZE = "Kurgal's Gaze"
    ULAMAN_GAZE = "Ulaman's Gaze"
    AMANAMU_GAZE = "Amanamu's Gaze"
    KULEMAKS_INVITATION = "Kulemak's Invitation"


class RELIC(StrEnum):
    URN = "Urn Relic"
    VASE = "Vase Relic"
    SEAL = "Seal Relic"
    COFFER = "Coffer Relic"
    INCENSE = "Incense Relic"
    AMPHORA = "Amphora Relic"
    TAPESTRY = "Tapestry Relic"


class SEKHEMA_KEY(StrEnum):
    GOLD = "Gold Key"
    BRONZE = "Bronze Key"
    SILVER = "Silver Key"


class LESSER_ESSENCE(StrEnum):
    ICE = "Lesser Essence of Ice"
    RUIN = "Lesser Essence of Ruin"
    HASTE = "Lesser Essence of Haste"
    BODY = "Lesser Essence of the Body"
    MIND = "Lesser Essence of the Mind"
    BATTLE = "Lesser Essence of Battle"
    FLAMES = "Lesser Essence of Flames"
    COMMAND = "Lesser Essence of Command"
    SORCERY = "Lesser Essence of Sorcery"
    SEEKING = "Lesser Essence of Seeking"
    THAWING = "Lesser Essence of Thawing"
    ABRASION = "Lesser Essence of Abrasion"
    ALACRITY = "Lesser Essence of Alacrity"
    OPULENCE = "Lesser Essence of Opulence"
    GROUNDING = "Lesser Essence of Grounding"
    INFINITE = "Lesser Essence of the Infinite"
    INSULATION = "Lesser Essence of Insulation"
    ELECTRICITY = "Lesser Essence of Electricity"
    ENHANCEMENT = "Lesser Essence of Enhancement"


class ESSENCE(StrEnum):
    ICE = "Essence of Ice"
    RUIN = "Essence of Ruin"
    HASTE = "Essence of Haste"
    BODY = "Essence of the Body"
    MIND = "Essence of the Mind"
    FLAMES = "Essence of Flames"
    BATTLE = "Essence of Battle"
    SEEKING = "Essence of Seeking"
    ABYSS = "Essence of the Abyss"
    SORCERY = "Essence of Sorcery"
    COMMAND = "Essence of Command"
    THAWING = "Essence of Thawing"
    OPULENCE = "Essence of Opulence"
    ALACRITY = "Essence of Alacrity"
    ABRASION = "Essence of Abrasion"
    GROUNDING = "Essence of Grounding"
    INFINITE = "Essence of the Infinite"
    INSULATION = "Essence of Insulation"
    ENHANCEMENT = "Essence of Enhancement"
    ELECTRICITY = "Essence of Electricity"


class GREATER_ESSENCE(StrEnum):
    ICE = "Greater Essence of Ice"
    RUIN = "Greater Essence of Ruin"
    HASTE = "Greater Essence of Haste"
    BODY = "Greater Essence of the Body"
    MIND = "Greater Essence of the Mind"
    FLAMES = "Greater Essence of Flames"
    BATTLE = "Greater Essence of Battle"
    SEEKING = "Greater Essence of Seeking"
    SORCERY = "Greater Essence of Sorcery"
    COMMAND = "Greater Essence of Command"
    THAWING = "Greater Essence of Thawing"
    OPULENCE = "Greater Essence of Opulence"
    ALACRITY = "Greater Essence of Alacrity"
    ABRASION = "Greater Essence of Abrasion"
    GROUNDING = "Greater Essence of Grounding"
    INFINITE = "Greater Essence of the Infinite"
    INSULATION = "Greater Essence of Insulation"
    ENHANCEMENT = "Greater Essence of Enhancement"
    ELECTRICITY = "Greater Essence of Electricity"


class PERFECT_ESSENCE(StrEnum):
    ICE = "Perfect Essence of Ice"
    RUIN = "Perfect Essence of Ruin"
    HASTE = "Perfect Essence of Haste"
    MIND = "Perfect Essence of the Mind"
    BODY = "Perfect Essence of the Body"
    FLAMES = "Perfect Essence of Flames"
    BATTLE = "Perfect Essence of Battle"
    SEEKING = "Perfect Essence of Seeking"
    SORCERY = "Perfect Essence of Sorcery"
    COMMAND = "Perfect Essence of Command"
    THAWING = "Perfect Essence of Thawing"
    OPULENCE = "Perfect Essence of Opulence"
    ABRASION = "Perfect Essence of Abrasion"
    ALACRITY = "Perfect Essence of Alacrity"
    GROUNDING = "Perfect Essence of Grounding"
    INFINITE = "Perfect Essence of the Infinite"
    INSULATION = "Perfect Essence of Insulation"
    ELECTRICITY = "Perfect Essence of Electricity"
    ENHANCEMENT = "Perfect Essence of Enhancement"


class CORRUPT_ESSENCE(StrEnum):
    HORROR = "Essence of Horror"
    DELIRIUM = "Essence of Delirium"
    HYSTERIA = "Essence of Hysteria"
    INSANITY = "Essence of Insanity"
    LESSER_THAWING = "Lesser Essence of Thawing"
    LESSER_COMMAND = "Lesser Essence of Command"
    LESSER_OPULENCE = "Lesser Essence of Opulence"
    LESSER_ALACRITY = "Lesser Essence of Alacrity"
    LESSER_GROUNDING = "Lesser Essence of Grounding"
    LESSER_INSULATION = "Lesser Essence of Insulation"


class EMOTION(StrEnum):
    IRE = "Diluted Liquid Ire"
    ENVY = "Liquid Envy"
    FEAR = "Concentrated Liquid Fear"
    GREED = "Diluted Liquid Greed"
    GUILT = "Diluted Liquid Guilt"
    DESPAIR = "Liquid Despair"
    DISGUST = "Liquid Disgust"
    PARANOIA = "Liquid Paranoia"
    ISOLATION = "Concentrated Liquid Isolation"
    SUFFERING = "Concentrated Liquid Suffering"


class CATALYST(StrEnum):
    TUL = "Tul's Catalyst"
    ESH = "Esh's Catalyst"
    XOPH = "Xoph's Catalyst"
    FLESH = "Flesh Catalyst"
    NEURAL = "Neural Catalyst"
    REAVER = "Reaver Catalyst"
    CHAYULA = "Chayula's Catalyst"
    SIBILANT = "Sibilant Catalyst"
    ADAPTIVE = "Adaptive Catalyst"
    CARAPACE = "Carapace Catalyst"
    UUL_NETOL = "Uul-Netol's Catalyst"
    SKITTERING = "Skittering Catalyst"


class OMEN(StrEnum):
    LIGHT = "Omen of Light"
    HUNT = "Omen of the Hunt"
    CHANCE = "Omen of Chance"
    LIEGE = "Omen of the Liege"
    GAMBLING = "Omen of Gambling"
    BLESSED = "Omen of the Blessed"
    BARTERING = "Omen of Bartering"
    WHITTLING = "Omen of Whittling"
    ANCIENTS = "Omen of the Ancients"
    RESURGENCE = "Omen of Resurgence"
    CORRUPTION = "Omen of Corruption"
    REFRESHMENT = "Omen of Refreshment"
    SOVEREIGN = "Omen of the Sovereign"
    PUTREFACTION = "Omen of Putrefaction"
    AMELIORATION = "Omen of Amelioration"
    RECOMBINATION = "Omen of Recombination"
    BLACKBLOODED = "Omen of the Blackblooded"
    ABYSSAL_ECHOES = "Omen of Abyssal Echoes"
    REINFORCEMENTS = "Omen of Reinforcements"
    CHAOTIC_RARITY = "Omen of Chaotic Rarity"
    SANCTIFICATION = "Omen of Sanctification"
    DEXTRAL_ERASURE = "Omen of Dextral Erasure"
    DEXTRAL_ALCHEMY = "Omen of Dextral Alchemy"
    CHAOTIC_MONSTERS = "Omen of Chaotic Monsters"
    CHAOTIC_QUANTITY = "Omen of Chaotic Quantity"
    ANSWERED_PRAYERS = "Omen of Answered Prayers"
    DEXTRAL_ANNULMENT = "Omen of Dextral Annulment"
    GREATER_ANNULMENT = "Omen of Greater Annulment"
    SINISTRAL_ERASURE = "Omen of Sinistral Erasure"
    SINISTRAL_ALCHEMY = "Omen of Sinistral Alchemy"
    DEXTRAL_EXALTAION = "Omen of Dextral Exaltation"
    GREATER_EXALTAION = "Omen of Greater Exaltation"
    DEXTRAL_CORONATION = "Omen of Dextral Coronation"
    DEXTRAL_NECROMANCY = "Omen of Dextral Necromancy"
    SECRET_COMPARTMENTS = "Omen of Secret Compartments"
    SINISTRAL_ANNULMENT = "Omen of Sinistral Annulment"
    SINISTRAL_EXALTATION = "Omen of Sinistral Exaltation"
    SINISTRAL_NECROMANCY = "Omen of Sinistral Necromancy"
    SINISTRAL_CORONATION = "Omen of Sinistral Coronation"
    CATALYSING_EXALTATION = "Omen of Catalysing Exaltation"
    HOMOGENISING_EXALTATION = "Omen of Homogenising Exaltation"
    HOMOGENISING_CORONATION = "Omen of Homogenising Coronation"
    DEXTRAL_CRYSTALLISATION = "Omen of Dextral Crystallisation"
    SINISTRAL_CRYSTALLISATION = "Omen of Sinistral Crystallisation"


class INVITATION(StrEnum):
    RUNIC = "Runic Splinter"
    BREACH = "Breach Splinter"
    PETITION = "Petition Splinter"
    SIMULACRUM = "Simulacrum Splinter"

    FADED = "Faded Crisis Fragment"
    ANCIENT = "Ancient Crisis Fragment"
    WEATHERED = "Weathered Crisis Fragment"

    PRIMARY_CALAMITY = "Primary Calamity Fragment"
    SECONDARY_CALAMITY = "Secondary Calamity Fragment"
    TERTIARY_CALAMITY = "Tertiary Calamity Fragment"

    DEADLY_FATE = "Deadly Fate"
    COWARDLY_FATE = "Cowardly Fate"
    VICTORIOUS_FATE = "Victorious Fate"


class TRIAL(StrEnum):
    BARYA = "Djinn Barya"
    ULTIMATUM = "Inscribed Ultimatum"


class RELIQUARY_KEY(StrEnum):
    XESHT = "Xesht's Reliquary Key"
    ZAROKH = "Zarokh's Reliquary Key"
    OLROTH = "Olroth's Reliquary Key"
    TWILIGHT = "Twilight Reliquary Key"
    TANGMAZU = "Tangmazu's Reliquary Key"
    ARBITER = "The Arbiter's Reliquary Key"
    RITUALISTIC = "Ritualistic Reliquary Key"
    TRIALMASTER = "The Trialmaster's Reliquary Key"


class ARCHETYPE(StrEnum):
    # mono
    STR = "STR"
    DEX = "DEX"
    INT = "INT"
    # multi
    STR_DEX = "STR_DEX"
    STR_INT = "STR_INT"
    DEX_INT = "DEX_INT"
