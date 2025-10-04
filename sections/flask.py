from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            MultiClass([FLASK.LIFE, FLASK.MANA]),
            TierStyle(TIER.RARE),
        ]
    ),
    # Show(
    #     [
    #         MultiBaseType(["Ultimate Life Flask", "Ultimate Mana Flask"]),
    #         Rarity(RARITY.MAGIC),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    Show(
        [
            MultiClass([GEAR.CHARM]),
            # MultiBaseType(["Thawing Charm", "Silver Charm", "Golden Charm"]),
            TierStyle(TIER.RARE),
        ]
    ),
    Hide([MultiClass([FLASK.LIFE, FLASK.MANA])]),
]
