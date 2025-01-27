from app.conditions import (
    ItemLevel,
    MultiBaseType,
    MultiClass,
)
from app.actions import TierStyle
from app.blocks import Hide, Show

from app.categories import (
    GEAR,
    WEAPON,
    TIER,
    OFFHAND,
    RING,
    AMULET,
)

gear_rules = [
    Show(
        [
            ItemLevel(82),
            MultiBaseType(
                [
                    "Expert Waxed Jacket",
                    "Expert Feathered Tiara",
                    "Expert Feathered Sandals",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]

weapon_rules = [
    Show(
        [
            ItemLevel(82),
            MultiBaseType(
                [
                    "Expert Slicing Quarterstaff",
                    "Expert Long Quarterstaff",
                    "Expert Crescent Quarterstaff",
                    "Expert Gothic Quarterstaff",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]

jewelry_rules = [
    Show(
        [
            ItemLevel(82),  # Resistances
            MultiBaseType(
                [
                    RING.RUBY,
                    RING.TOPAZ,
                    RING.SAPPHIRE,
                    RING.PRISMATIC,
                    RING.GOLD,
                    RING.BREACH,
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            ItemLevel(82),
            MultiBaseType(
                [
                    AMULET.AZURE,
                    AMULET.GOLD,
                    AMULET.STELLAR,
                    AMULET.JADE,
                    AMULET.LAPIS,
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]

hide_the_rest = [
    Hide(
        [
            MultiClass(list(GEAR)),
        ]
    ),
    Hide(
        [
            MultiClass(list(WEAPON)),
        ]
    ),
    Hide(
        [
            MultiClass(list(OFFHAND)),
        ]
    ),
]

rules = [
    *gear_rules,
    *weapon_rules,
    *jewelry_rules,
    *hide_the_rest,
]
