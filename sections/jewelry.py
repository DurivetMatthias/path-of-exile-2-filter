from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            MultiClass(list(JEWELRY)),
            TierStyle(TIER.RARE),
        ]
    ),
    Show([MultiBaseType(["Breach Ring"]), TierStyle(TIER.EPIC)]),
    Show(
        [
            MultiBaseType(["Gold Ring", "Pearl Ring", "Solar Amulet", "Gold Amulet"]),
            ItemLevel(75),
            Rarity(RARITY.NORMAL),
            TierStyle(TIER.EPIC),
        ]
    ),
    Hide([MultiClass(list(JEWELRY))]),
]
