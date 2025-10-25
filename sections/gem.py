from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            MultiClass(
                [
                    GEM.SKILL,
                    GEM.SUPPORT,
                    GEM.SPIRIT,
                ]
            ),
            TierStyle(TIER.RARE),
        ]
    ),
    # 18+ uncut gems
    Show(
        [
            MultiClass([GEM.SKILL, GEM.SPIRIT]),
            BaseType("Level 18", operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass([GEM.SKILL, GEM.SPIRIT]),
            BaseType("Level 19", operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass([GEM.SKILL, GEM.SPIRIT]),
            BaseType("Level 20", operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Lineage Support
    Show(
        [
            MultiClass(["Support Gems"]),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
