from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    # Gear
    Show(
        [
            AreaLevel(64),
            PureEnergyShield(),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(64),
            MultiClass([WEAPON.WAND, OFFHAND.FOCUS, WEAPON.SCEPTRE]),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            AreaLevel(64),
            MultiClass([JEWELRY.RING, JEWELRY.AMULET, JEWELRY.BELT]),
            TierStyle(TIER.RARE),
        ]
    ),
    # Exceptional
    Show(
        [
            Quality(21),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Sockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass(
                [
                    ARMOUR.HELMET,
                    ARMOUR.BOOTS,
                    ARMOUR.GLOVES,
                    WEAPON.WAND,
                    OFFHAND.FOCUS,
                    OFFHAND.SHIELD,
                ]
            ),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Hide the rest
    Hide([MultiClass(list(ARMOUR))]),
    Hide([MultiClass(list(WEAPON))]),
    Hide([MultiClass(list(OFFHAND))]),
    Hide([MultiClass(list(JEWELRY))]),
    Hide([MultiClass(["Charms"])]),
]
