from app.conditions import MultiBaseType, Rarity
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, LIFE_FLASK, MANA_FLASK, RARITY

rules = [
    Show(
        [
            MultiBaseType([LIFE_FLASK.ULTIMATE, MANA_FLASK.ULTIMATE]),
            Rarity(RARITY.MAGIC),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Show(
    #     [
    #         MultiBaseType(list(LIFE_FLASK)),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    # Show(
    #     [
    #         MultiBaseType(list(MANA_FLASK)),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
]
