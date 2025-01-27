from app.conditions import BaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, OPERATOR

rules = [
    Show(
        [
            BaseType("Simulacrum Splinter", operator=OPERATOR.EQUAL),
            TierStyle(TIER.RARE),
        ]
    ),
    # Show(
    #     [
    #         BaseType("Emotion", operator=OPERATOR.EQUAL),
    #         TierStyle(TIER.RARE),
    #     ]
    # ),
]
