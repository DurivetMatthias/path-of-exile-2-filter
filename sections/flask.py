from app.actions import TierStyle
from app.conditions import MultiClass, MultiBaseType
from app.blocks import Hide, Show
from app.categories import OPERATOR, TIER, FLASK

rules = [
    # Show(
    #     [
    #         MultiClass(["Life Flasks", "Mana Flasks"]),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    # Show(
    #     [
    #         MultiBaseType(["Ultimate Life Flask", "Ultimate Mana Flask"]),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    Hide(
        [
            MultiBaseType([FLASK.LIFE, FLASK.MANA], operator=OPERATOR.EQUAL),
        ]
    ),
]
