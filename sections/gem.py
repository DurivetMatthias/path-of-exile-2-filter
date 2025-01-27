from app.actions import TierStyle
from app.conditions import MultiBaseType, BaseType, ItemLevel
from app.blocks import Hide, Show
from app.categories import TIER, GEM, OPERATOR

rules = [
    Show(
        [
            ItemLevel(19),
            MultiBaseType(list(GEM)),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            ItemLevel(13, operator=OPERATOR.LTE),
            MultiBaseType(list(GEM)),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    GEM.SPIRIT,
                    GEM.SUPPORT,
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
    Hide(
        [
            MultiBaseType(list(GEM)),
        ]
    ),
]
