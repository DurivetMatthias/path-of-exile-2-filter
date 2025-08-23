from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

config = {
    CURRENCY.TRANSMUTATION: TIER.COMMON,
    CURRENCY.AUGMENTATION: TIER.COMMON,
    CURRENCY.REGAL: TIER.EPIC,
    CURRENCY.VAAL: TIER.EPIC,
    CURRENCY.ALCHEMY: TIER.LEGENDARY,
    CURRENCY.CHAOS: TIER.LEGENDARY,
    CURRENCY.EXALTED: TIER.LEGENDARY,
    CURRENCY.ANNULMENT: TIER.LEGENDARY,
    CURRENCY.CHANCE: TIER.LEGENDARY,
    CURRENCY.DIVINE: TIER.LEGENDARY,
    CURRENCY.FRACTURING: TIER.LEGENDARY,
    CURRENCY.MIRROR: TIER.LEGENDARY,
    CURRENCY.ARCANIST: TIER.COMMON,
    CURRENCY.ARMOURER: TIER.COMMON,
    CURRENCY.BLACKSMITH: TIER.COMMON,
    CURRENCY.ARTIFICER: TIER.COMMON,
    CURRENCY.GEMCUTTER: TIER.EPIC,
    CURRENCY.GLASSBLOWER: TIER.EPIC,
    CURRENCY.LESSER_JEWELLER: TIER.EPIC,
    CURRENCY.GREATER_JEWELLER: TIER.LEGENDARY,
    CURRENCY.PERFECT_JEWELLER: TIER.LEGENDARY,
    CURRENCY.ARTIFICERS_SHARD: TIER.COMMON,
    CURRENCY.TRANSMUTATION_SHARD: TIER.COMMON,
    CURRENCY.REGAL_SHARD: TIER.COMMON,
    CURRENCY.CHANCE_SHARD: TIER.LEGENDARY,
}

currency_rules = [
    Show([BaseType(name), TierStyle(tier)]) for name, tier in config.items()
]

rules = [
    Show(
        [
            MultiBaseType(list(CURRENCY)),
            TierStyle(TIER.COMMON),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    *currency_rules,
    Show(
        [
            BaseType("Gold"),
            StackSize(100),
            TierStyle(TIER.COMMON),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            BaseType("Gold"),
            StackSize(300),
            TierStyle(TIER.COMMON),
            Strictness(STRICTNESS.STRICT),
        ]
    ),
    Show(
        [
            BaseType("Gold"),
            StackSize(500),
            TierStyle(TIER.COMMON),
            Strictness(STRICTNESS.UBER),
        ]
    ),
    Show(
        [
            BaseType("Gold"),
            AreaLevel(20),
            TierStyle(TIER.COMMON),
        ]
    ),
    Hide([BaseType("Gold")]),
]
