from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            MultiClass(list(FLASK)),
            TierStyle(TIER.COMMON),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            MultiBaseType([LIFE_FLASK.ULTIMATE, MANA_FLASK.ULTIMATE]),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
            Strictness(STRICTNESS.STRICT),
        ]
    ),
]
