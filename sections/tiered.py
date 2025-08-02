from app.conditions import Rarity, UnidentifiedItemTier
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, RARITY

rules = [
    Show(
        [
            Rarity(RARITY.RARE),
            UnidentifiedItemTier(),
            TierStyle(TIER.COMMON),
        ]
    ),
]
