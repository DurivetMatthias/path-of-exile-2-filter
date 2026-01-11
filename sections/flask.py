from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            # ItemLevel(65),
            # Rarity(RARITY.NORMAL),
            MultiClass([FLASK.LIFE, FLASK.MANA]),
            # MultiBaseType(["Ultimate Mana Flask", "Ultimate Life Flask"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            # ItemLevel(65),
            # Rarity(RARITY.NORMAL),
            Class(FLASK.CHARM),
            # MultiBaseType(["Thawing Charm", "Silver Charm", "Golden Charm"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Hide([MultiClass([FLASK.LIFE, FLASK.MANA, FLASK.CHARM])]),
]
