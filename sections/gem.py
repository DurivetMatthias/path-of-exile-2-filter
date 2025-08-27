from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            MultiBaseType([GEM.SKILL, GEM.SUPPORT, GEM.SPIRIT]),
            TierStyle(TIER.LEGENDARY),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            MultiBaseType([GEM.SKILL, GEM.SUPPORT, GEM.SPIRIT]),
            TierStyle(TIER.COMMON),
            FilterLevel(FILTER_LEVEL.MAP_PROGRESSION),
        ]
    ),
]
