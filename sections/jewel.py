from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

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
