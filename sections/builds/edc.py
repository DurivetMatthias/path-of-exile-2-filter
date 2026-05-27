from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *


rules = [
    # Gear
    Show(
        [
            AreaLevel(1, OPERATOR.LTE),
            VendorStyle(),
        ]
    ),
    Show(
        [
            AreaLevel(10, OPERATOR.LTE),
            MultiClass([OFFHAND.QUIVER]),
            VendorStyle(),
        ]
    ),
    Show(
        [
            AreaLevel(10, OPERATOR.LTE),
            BaseType("Gold"),
            VendorStyle(),
        ]
    ),
    Show(
        [
            AreaLevel(10, OPERATOR.LTE),
            Rarity(RARITY.RARE),
            VendorStyle(),
        ]
    ),
    Show(
        [
            ItemLevel(10, OPERATOR.LTE),
            EnergyShieldAndHybrid(),
            MultiClass(list(GEAR)),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            PureEnergyShield(),
            MultiClass(list(GEAR)),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            ItemLevel(10, OPERATOR.LTE),
            MultiClass([GEAR.BOOTS, GEAR.GLOVES]),
            Rarity(RARITY.MAGIC, OPERATOR.GTE),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Weapons
    Show(
        [
            MultiClass(
                [
                    WEAPON.WAND,
                    WEAPON.WAND,
                    OFFHAND.FOCUS,
                    WEAPON.SCEPTRE,
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Jewelry
    Show(
        [
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
