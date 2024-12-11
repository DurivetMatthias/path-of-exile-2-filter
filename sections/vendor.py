from app.conditions import Rarity, Sockets
from app.actions import TierStyle
from app.blocks import Show
from app.categories import RARITY, TIER, OPERATOR

rules = [
    Show(
        [
            Rarity(RARITY.RARE),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            Sockets("S", operator=OPERATOR.EXACT),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            Sockets("SS", operator=OPERATOR.EXACT),
            TierStyle(TIER.EPIC),
        ]
    ),
]
