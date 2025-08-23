from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

ARCANIST = [
    WEAPON.WAND,
    WEAPON.STAFF,
    WEAPON.SCEPTRE,
    WEAPON.TRAP,
]
MARTIAL = [
    WEAPON.BOW,
    WEAPON.DAGGER,
    WEAPON.CLAW,
    WEAPON.ONE_HAND_AXE,
    WEAPON.ONE_HAND_MACE,
    WEAPON.ONE_HAND_SWORD,
    WEAPON.TWO_HAND_AXE,
    WEAPON.TWO_HAND_MACE,
    WEAPON.TWO_HAND_SWORD,
    WEAPON.SPEAR,
    WEAPON.CROSSBOW,
    WEAPON.FISHING_ROD,
    WEAPON.FLAIL,
    WEAPON.QUARTERSTAFF,
]
ARMOUR = [
    GEAR.BODY_ARMOUR,
    GEAR.BOOTS,
    GEAR.GLOVES,
    GEAR.HELMET,
    OFFHAND.SHIELD,
    OFFHAND.QUIVER,
    OFFHAND.FOCUS,
]
GLASSBLOWER = [
    GEAR.CHARM,
    FLASK.LIFE,
    FLASK.MANA,
]

rules = [
    Show(
        [
            AreaLevel(10),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(30),
            Rarity(RARITY.RARE),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(10),
            Sockets("S", operator=OPERATOR.EXACT),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(10),
            Sockets("SS", operator=OPERATOR.EXACT),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(30),
            Quality(),
            MultiClass(MARTIAL),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Show(
    #     [
    #         AreaLevel(30),
    #         Quality(),
    #         MultiClass(ARCANIST),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    # Show(
    #     [
    #         AreaLevel(30),
    #         Quality(),
    #         MultiClass(ARMOUR),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    Show(
        [
            Quality(),
            MultiClass(GLASSBLOWER),
            TierStyle(TIER.COMMON),
        ]
    ),
]
