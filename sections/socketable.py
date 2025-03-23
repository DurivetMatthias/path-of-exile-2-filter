from app.conditions import MultiBaseType, BaseType, AreaLevel
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, RUNE, SOUL_CORE, AREA_LEVEL, OPERATOR

rules = [
    Show([MultiBaseType(list(SOUL_CORE)), TierStyle(TIER.LEGENDARY)]),
    Show(
        [
            BaseType(RUNE.IRON),
            TierStyle(TIER.LEGENDARY),
            AreaLevel(AREA_LEVEL.ACT_4, OPERATOR.LT),
        ]
    ),
    Show(
        [
            BaseType(RUNE.DESERT),
            TierStyle(TIER.LEGENDARY),
            AreaLevel(AREA_LEVEL.ACT_4, OPERATOR.LT),
        ]
    ),
    Show(
        [
            BaseType(RUNE.GLACIAL),
            TierStyle(TIER.LEGENDARY),
            AreaLevel(AREA_LEVEL.ACT_4, OPERATOR.LT),
        ]
    ),
    Show(
        [
            BaseType(RUNE.STORM),
            TierStyle(TIER.LEGENDARY),
            AreaLevel(AREA_LEVEL.ACT_4, OPERATOR.LT),
        ]
    ),
    # Show([BaseType(RUNE.IRON), TierStyle(TIER.LEGENDARY)]),
    # Show([BaseType(RUNE.DESERT), TierStyle(TIER.LEGENDARY)]),
    # Show([BaseType(RUNE.GLACIAL), TierStyle(TIER.LEGENDARY)]),
    # Show([BaseType(RUNE.STORM), TierStyle(TIER.LEGENDARY)]),
    # Show([BaseType(RUNE.BODY), TierStyle(TIER.LEGENDARY)]),
    # Show([BaseType(RUNE.MIND), TierStyle(TIER.LEGENDARY)]),
    # Show([BaseType(RUNE.VISION), TierStyle(TIER.LEGENDARY)]),
    # Show([BaseType(RUNE.REBIRTH), TierStyle(TIER.LEGENDARY)]),
    # Show([BaseType(RUNE.INSPIRATION), TierStyle(TIER.LEGENDARY)]),
    # Show([BaseType(RUNE.STONE), TierStyle(TIER.LEGENDARY)]),
]
