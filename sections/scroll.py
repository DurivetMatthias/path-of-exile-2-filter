from app.conditions import AreaLevel, BaseType
from app.actions import TierStyle
from app.blocks import Show, Hide
from app.categories import TIER, OPERATOR, CURRENCY, AREA_LEVEL


rules = [
    Show(
        [
            AreaLevel(AREA_LEVEL.ACT_2, OPERATOR.LT),
            BaseType(CURRENCY.WISDOM),
            TierStyle(TIER.COMMON),
        ],
    ),
    Hide(
        [
            AreaLevel(AREA_LEVEL.ACT_2, OPERATOR.GTE),
            BaseType(CURRENCY.WISDOM),
            TierStyle(TIER.COMMON),
        ],
    ),
]
