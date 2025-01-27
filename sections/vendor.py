from app.conditions import Rarity, Sockets, AreaLevel
from app.actions import TierStyle
from app.blocks import Show
from app.categories import RARITY, TIER, OPERATOR

rules = [
    # Show(
    #     [
    #         AreaLevel(65, operator=OPERATOR.LT),
    #         Rarity(RARITY.RARE),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    # Show(
    #     [
    #         AreaLevel(65, operator=OPERATOR.LT),
    #         Sockets("S", operator=OPERATOR.EXACT),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    # Show(
    #     [
    #         AreaLevel(65, operator=OPERATOR.LT),
    #         Sockets("SS", operator=OPERATOR.EXACT),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
]
