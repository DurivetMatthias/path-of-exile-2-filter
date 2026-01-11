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
            TierStyle(TIER.COMMON),
        ]
    ),
    # 19+ uncut gems
    Show(
        [
            MultiClass([GEM.SKILL, GEM.SPIRIT]),
            BaseType("Level 19", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass([GEM.SKILL, GEM.SPIRIT]),
            BaseType("Level 20", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Lineage Support
    Show(
        [
            Class("Support Gems"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
