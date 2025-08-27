from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            MultiClass([FLASK.LIFE, FLASK.MANA]),
            TierStyle(TIER.RARE),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            MultiBaseType(["Ultimate Life Flask", "Ultimate Mana Flask"]),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
            FilterLevel(FILTER_LEVEL.MAP_PROGRESSION),
        ]
    ),
    Hide([MultiClass([FLASK.LIFE, FLASK.MANA])]),
]
