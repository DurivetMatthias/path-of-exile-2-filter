from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show([MultiBaseType(list(SOUL_CORE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(TALISMAN)), TierStyle(TIER.LEGENDARY)]),
    Show(
        [
            MultiBaseType(list(LESSER_RUNE)),
            TierStyle(TIER.COMMON),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            MultiBaseType(list(RUNE)),
            TierStyle(TIER.COMMON),
            FilterLevel(FILTER_LEVEL.MAP_PROGRESSION),
        ]
    ),
    Show(
        [
            MultiBaseType(list(GREATER_RUNE)),
            TierStyle(TIER.LEGENDARY),
            FilterLevel(FILTER_LEVEL.ENDGAME),
        ]
    ),
    Show(
        [
            BaseType("Rune of", operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
            FilterLevel(FILTER_LEVEL.ENDGAME),
        ]
    ),
]
