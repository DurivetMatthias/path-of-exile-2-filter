from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            MultiClass(list(JEWELRY)),
            TierStyle(TIER.EPIC),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            MultiClass(["Belts"]),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Ruby Ring",
                    "Sapphire Ring",
                    "Topaz Ring",
                    "Breach Ring",
                    "Prismatic Ring",
                    "Amethyst Ring",
                    "Gold Ring",
                    "Lapis Amulet",
                    "Jade Amulet",
                    "Amber Amulet",
                    "Stellar Amulet",
                    "Solar Amulet",
                    "Bloodstone Amulet",
                    "Lunar Amulet",
                    "Gold Amulet",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
    Hide([MultiClass(list(JEWELRY))]),
]
