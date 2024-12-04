from app.actions import TierStyle
from app.conditions import AreaLevel, MultiBaseType
from app.blocks import Hide, Show
from app.categories import OPERATOR, TIER

rules = [
    Show(
        [
            AreaLevel(65, operator=OPERATOR.LT),
            MultiBaseType(["Life Flask", "Mana Flask"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiBaseType(["Divine Life Flask", "Divine Mana Flask"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Hide(
        [
            AreaLevel(65, operator=OPERATOR.GTE),
            MultiBaseType(["Life Flask", "Mana Flask"]),
        ]
    ),
]
