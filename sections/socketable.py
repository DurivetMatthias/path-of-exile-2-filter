from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show, Hide
from app.categories import TIER, RUNE, SOUL_CORE

rules = [
    Show(
        [
            MultiBaseType(list(SOUL_CORE)),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Show(
    #     [
    #         MultiBaseType(
    #             [
    #                 RUNE.IRON,
    #                 RUNE.DESERT,
    #                 RUNE.GLACIAL,
    #                 RUNE.STORM,
    #             ]
    #         ),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    Hide(
        [
            MultiBaseType(list(RUNE)),
        ]
    ),
]
