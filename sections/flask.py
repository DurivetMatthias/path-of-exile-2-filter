from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    # Flask
    Show(
        [
            AreaLevel(65, OPERATOR.LTE),
            MultiClass([FLASK.LIFE, FLASK.MANA]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            Rarity(RARITY.NORMAL),
            MultiBaseType(["Ultimate Mana Flask", "Ultimate Life Flask"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Charm
    Show(
        [
            AreaLevel(65, OPERATOR.LTE),
            Class(FLASK.CHARM),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            Rarity(RARITY.NORMAL),
            MultiBaseType(["Thawing Charm", "Silver Charm", "Golden Charm"]),
            TierStyle(TIER.COMMON),
        ]
    ),
    Hide([MultiClass([FLASK.LIFE, FLASK.MANA, FLASK.CHARM])]),
]
