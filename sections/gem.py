from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    # Skill
    Show(
        [TierStyle(TIER.LEGENDARY), BaseType(GEM.SKILL), Strictness(STRICTNESS.REGULAR)]
    ),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(14), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(15), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(16), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(17), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(18), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(19), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(20), BaseType(GEM.SKILL)]),
    # Support
    Show(
        [
            TierStyle(TIER.LEGENDARY),
            BaseType(GEM.SUPPORT),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            TierStyle(TIER.EPIC),
            ItemLevel(3),
            BaseType(GEM.SUPPORT),
            Strictness(STRICTNESS.STRICT),
        ]
    ),
    # Spirit
    Show(
        [
            TierStyle(TIER.LEGENDARY),
            BaseType(GEM.SPIRIT),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(14), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(15), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(16), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(17), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(18), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(19), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(20), BaseType(GEM.SPIRIT)]),
]
