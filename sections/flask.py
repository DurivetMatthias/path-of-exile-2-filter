from app.conditions import AreaLevel, MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, LIFE_FLASK, MANA_FLASK, AREA_LEVEL, OPERATOR

rules = [
    Show(
        [
            MultiBaseType(list(LIFE_FLASK)),
            AreaLevel(AREA_LEVEL.YELLOW_MAPS, OPERATOR.LT),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiBaseType(list(MANA_FLASK)),
            AreaLevel(AREA_LEVEL.YELLOW_MAPS, OPERATOR.LT),
            TierStyle(TIER.COMMON),
        ]
    ),
]
