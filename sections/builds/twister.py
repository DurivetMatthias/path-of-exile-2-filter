from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *


rules = [
    # Gear
    Show(
        [
            AreaLevel(3, OPERATOR.LTE),
            VendorStyle(),
        ]
    ),
    Show(
        [
            AreaLevel(14, OPERATOR.LT),
            MultiClass([OFFHAND.QUIVER]),
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
            AreaLevel(30, OPERATOR.LT),
            Rarity(RARITY.RARE),
            VendorStyle(),
        ]
    ),
    Show(
        [
            ItemLevel(10, OPERATOR.LT),
            EvasionAndHybrid(),
            MultiClass(list(GEAR)),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            # ItemLevel(20, OPERATOR.LT),
            PureEvasion(),
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
            # ItemLevel(20, OPERATOR.LT),
            MultiClass([WEAPON.SPEAR]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            ItemLevel(20, OPERATOR.LT),
            MultiClass([OFFHAND.BUCKLER]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            # ItemLevel(20, OPERATOR.LT),
            MultiClass([WEAPON.SCEPTRE]),
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
