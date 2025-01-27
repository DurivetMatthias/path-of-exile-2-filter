from app.conditions import BaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, OPERATOR

rules = [
    Show(
        [
            BaseType("Essence", operator=OPERATOR.EQUAL),
            TierStyle(TIER.RARE),
        ]
    ),
]
