from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

GLASSBLOWER = [
    GEAR.CHARM,
    FLASK.LIFE,
    FLASK.MANA,
]

rules = [
    Show(
        [
            AreaLevel(30),
            Rarity(RARITY.RARE),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            Quality(),
            MultiClass(GLASSBLOWER),
            TierStyle(TIER.COMMON),
        ]
    ),
]
