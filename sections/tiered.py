from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            Rarity(RARITY.MAGIC),
            UnidentifiedItemTier(),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Rarity(RARITY.RARE),
            UnidentifiedItemTier(),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Rarity(RARITY.RARE),
            BaseType("Exceptional", operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
