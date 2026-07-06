from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            AreaLevel(65, OPERATOR.LT),
            MultiClass(["Life Flasks", "Mana Flasks", "Charms"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            Rarity(RARITY.NORMAL),
            ItemLevel(81),
            MultiBaseType(
                [
                    "Ultimate Mana Flask",
                    "Ultimate Life Flask",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Thawing Charm",
                    "Silver Charm",
                    "Golden Charm",
                    "Staunching Charm",
                    "Dousing Charm",
                    "Antidote Charm",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    Hide([MultiClass(["Life Flasks", "Mana Flasks", "Charms"])]),
]
