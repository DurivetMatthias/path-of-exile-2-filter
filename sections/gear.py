from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

# TODO define presets and breakpoints
# eg. pre-maps, white maps, T15 maps
# Import whatever is needed without rewriting every time

rules = [
    # Gear
    Show(
        [
            ItemLevel(65, OPERATOR.LT),
            MultiClass([WEAPON.BOW, OFFHAND.QUIVER]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            ItemLevel(65, OPERATOR.LT),
            PureArmour(),
            MultiClass([GEAR.BODY_ARMOUR, GEAR.HELMET, GEAR.BOOTS, GEAR.GLOVES]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            ItemLevel(65, OPERATOR.LT),
            MultiClass([JEWELRY.AMULET, JEWELRY.RING, JEWELRY.BELT]),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Hide the rest
    Hide([MultiClass(list(ARMOUR))]),
    Hide([MultiClass(list(WEAPON))]),
    Hide([MultiClass(list(OFFHAND))]),
    Hide([MultiClass(list(JEWELRY))]),
]
