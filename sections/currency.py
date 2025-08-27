from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

config = {
    # Tiered currency
    CURRENCY.TRANSMUTATION: TIER.COMMON,
    CURRENCY.GREATER_TRANSMUTATION: TIER.EPIC,
    CURRENCY.PERFECT_TRANSMUTATION: TIER.LEGENDARY,
    CURRENCY.AUGMENTATION: TIER.COMMON,
    CURRENCY.GREATER_AUGMENTATION: TIER.EPIC,
    CURRENCY.PERFECT_AUGMENTATION: TIER.LEGENDARY,
    CURRENCY.REGAL: TIER.EPIC,
    CURRENCY.GREATER_REGAL: TIER.EPIC,
    CURRENCY.PERFECT_REGAL: TIER.LEGENDARY,
    CURRENCY.CHAOS: TIER.LEGENDARY,
    CURRENCY.GREATER_CHAOS: TIER.EPIC,
    CURRENCY.PERFECT_CHAOS: TIER.LEGENDARY,
    CURRENCY.EXALTED: TIER.LEGENDARY,
    CURRENCY.GREATER_EXALTED: TIER.EPIC,
    CURRENCY.PERFECT_EXALTED: TIER.LEGENDARY,
    # Other
    CURRENCY.VAAL: TIER.EPIC,
    CURRENCY.ALCHEMY: TIER.LEGENDARY,
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
    *currency_rules,
    Show(
        [
            MultiBaseType(list(CURRENCY)),
            TierStyle(TIER.COMMON),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            AreaLevel(20),
            StackSize(1),
            BaseType("Gold"),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            BaseType("Gold"),
            StackSize(100),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            BaseType("Gold"),
            StackSize(300),
            FilterLevel(FILTER_LEVEL.MAP_PROGRESSION),
        ]
    ),
    Show(
        [
            BaseType("Gold"),
            StackSize(500),
            FilterLevel(FILTER_LEVEL.ENDGAME),
        ]
    ),
    Hide([BaseType("Gold")]),
]
