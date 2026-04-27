from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *


rules = [
    # Gear
    Show(
        [
            AreaLevel(1),
            VendorStyle(),
        ]
    ),
    Show(
        [
            AreaLevel(10, OPERATOR.LT),
            BaseType("Gold"),
            StackSize(10),
            VendorStyle(),
        ]
    ),
    Show(
        [
            AreaLevel(30),
            Rarity(RARITY.RARE),
            VendorStyle(),
        ]
    ),
    Show(
        [
            # ItemLevel(20, OPERATOR.LT),
            ArmourAndHybrid(),
            MultiClass(list(GEAR)),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            # ItemLevel(20, OPERATOR.LT),
            PureArmour(),
            MultiClass(list(GEAR)),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            # ItemLevel(20, OPERATOR.LT),
            MultiClass([GEAR.BOOTS, GEAR.GLOVES]),
            Rarity(RARITY.MAGIC, OPERATOR.GTE),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Weapons
    Show(
        [
            ItemLevel(20, OPERATOR.LT),
            MultiClass([WEAPON.TALISMAN]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            # ItemLevel(20, OPERATOR.LT),
            MultiClass([WEAPON.ONE_HAND_MACE]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            ItemLevel(16, OPERATOR.GTE),
            PureArmour(),
            MultiClass([OFFHAND.SHIELD]),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Jewelry
    Show(
        [
            # ItemLevel(20, OPERATOR.LT),
            MultiClass(
                [
                    JEWELRY.BELT,
                    JEWELRY.RING,
                    JEWELRY.AMULET,
                ]
            ),
            TierStyle(TIER.RARE),
        ]
    ),
    # Hide the rest
    Hide([MultiClass(list(ARMOUR))]),
    Hide([MultiClass(list(WEAPON))]),
    Hide([MultiClass(list(OFFHAND))]),
    Hide([MultiClass(list(JEWELRY))]),
]
