from app.conditions import MultiBaseType, Class
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, JEWEL

rules = [
    Show(
        [
            MultiBaseType(
                [
                    JEWEL.RUBY,
                    JEWEL.EMERALD,
                    JEWEL.SAPPHIRE,
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    JEWEL.TIME_LOST_RUBY,
                    JEWEL.TIME_LOST_EMERALD,
                    JEWEL.TIME_LOST_SAPPHIRE,
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show([Class("Jewels"), TierStyle(TIER.LEGENDARY)]),
]
