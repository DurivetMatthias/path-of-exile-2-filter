from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            AreaLevel(64),
            MultiClass([FLASK.LIFE, FLASK.MANA]),
            TierStyle(TIER.RARE),
        ]
    ),
    # Show(
    #     [
    #         MultiBaseType(["Ultimate Mana Flask", "Ultimate Life Flask"]),
    #         ItemLevel(81),
    #         TierStyle(TIER.RARE),
    #     ]
    # ),
    # Show(
    #     [
    #         MultiClass([GEAR.CHARM]),
    #         MultiBaseType(["Thawing Charm", "Silver Charm", "Golden Charm"]),
    #         TierStyle(TIER.RARE),
    #     ]
    # ),
    Show(
        [
            MultiClass([GEAR.CHARM]),
            TierStyle(TIER.RARE),
        ]
    ),
    Hide([MultiClass([FLASK.LIFE, FLASK.MANA])]),
]
