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
            MultiBaseType(
                [
                    "Vile Robe",
                    "Ancestral Tiara",
                    "Sekhema Sandals",
                    "Sirenscale Gloves",
                ]
            ),
            ItemLevel(79),
            Rarity(RARITY.NORMAL),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiBaseType(["Withered Wand", "Tasalian Focus"]),
            ItemLevel(79),
            # Rarity(RARITY.NORMAL),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Gold Ring",
                    "Pearl Ring",
                    "Prismatic Ring",
                    "Ruby Ring",
                    "Topaz Ring",
                    "Sapphire Ring",
                    "Solar Amulet",
                    "Gold Amulet",
                    "Lunar Amulet",
                ]
            ),
            ItemLevel(79),
            Rarity(RARITY.NORMAL),
            TierStyle(TIER.EPIC),
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
    Hide([MultiClass(list(JEWELRY))]),
    Hide([MultiClass(["Charms"])]),
]
