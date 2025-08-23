from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show([MultiBaseType(list(SOUL_CORE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(TALISMAN)), TierStyle(TIER.LEGENDARY)]),
    Show(
        [
            MultiBaseType(list(LESSER_RUNE)),
            TierStyle(TIER.COMMON),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            MultiBaseType(list(RUNE)),
            TierStyle(TIER.COMMON),
            Strictness(STRICTNESS.STRICT),
        ]
    ),
    Show(
        [
            MultiBaseType(list(GREATER_RUNE)),
            TierStyle(TIER.LEGENDARY),
            Strictness(STRICTNESS.UBER),
        ]
    ),
    Show(
        [
            BaseType("Rune of", operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
            Strictness(STRICTNESS.UBER),
        ]
    ),
]
