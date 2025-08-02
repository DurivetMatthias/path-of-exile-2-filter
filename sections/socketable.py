from app.conditions import MultiBaseType, BaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, LESSER_RUNE, RUNE, GREATER_RUNE, SOUL_CORE, TALISMAN

rules = [
    Show([MultiBaseType(list(SOUL_CORE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(TALISMAN)), TierStyle(TIER.LEGENDARY)]),
    # Show([MultiBaseType(list(LESSER_RUNE)), TierStyle(TIER.COMMON)]),
    # Show([BaseType(LESSER_RUNE.IRON), TierStyle(TIER.RARE)]),
    # Show([BaseType(LESSER_RUNE.DESERT), TierStyle(TIER.RARE)]),
    # Show([BaseType(LESSER_RUNE.GLACIAL), TierStyle(TIER.RARE)]),
    # Show([BaseType(LESSER_RUNE.STORM), TierStyle(TIER.RARE)]),
    # Show([BaseType(LESSER_RUNE.VISION), TierStyle(TIER.RARE)]),
    # Show([MultiBaseType(list(RUNE)), TierStyle(TIER.RARE)]),
    # Show([BaseType(RUNE.IRON), TierStyle(TIER.EPIC)]),
    # Show([BaseType(RUNE.DESERT), TierStyle(TIER.EPIC)]),
    # Show([BaseType(RUNE.GLACIAL), TierStyle(TIER.EPIC)]),
    # Show([BaseType(RUNE.STORM), TierStyle(TIER.EPIC)]),
    # Show([BaseType(RUNE.VISION), TierStyle(TIER.EPIC)]),
    Show([MultiBaseType(list(GREATER_RUNE)), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(GREATER_RUNE.IRON), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(GREATER_RUNE.DESERT), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(GREATER_RUNE.GLACIAL), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(GREATER_RUNE.STORM), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(GREATER_RUNE.VISION), TierStyle(TIER.LEGENDARY)]),
]
