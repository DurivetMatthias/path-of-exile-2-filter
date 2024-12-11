from app.actions import TierStyle
from app.conditions import AreaLevel, MultiClass, MultiBaseType
from app.blocks import Hide, Show
from app.categories import OPERATOR, TIER

rules = [
    Show(
        [
            AreaLevel(65, operator=OPERATOR.LT),
            MultiClass(["Life Flasks", "Mana Flasks"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(65, operator=OPERATOR.LT),
            MultiBaseType(["Ultimate Life Flask", "Ultimate Mana Flask"]),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Hide(
        [
            AreaLevel(65, operator=OPERATOR.GTE),
            MultiClass(["Life Flasks", "Mana Flasks"]),
        ]
    ),
]
