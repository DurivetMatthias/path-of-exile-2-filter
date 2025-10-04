from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    # Show magic boots
    Show(
        [
            AreaLevel(11),
            MultiClass([ARMOUR.BOOTS]),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Show caster gear
    Show(
        [
            MultiClass(list(ARMOUR)),
            PureEnergyShield(),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            MultiClass([WEAPON.WAND, OFFHAND.FOCUS]),
            TierStyle(TIER.RARE),
        ]
    ),
    # Exceptional
    Show(
        [
            MultiClass([WEAPON.WAND, OFFHAND.FOCUS]),
            Quality(21),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass([ARMOUR.BODY]),
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
    Hide([MultiClass(["Charms"])]),
]
