from app.conditions import MultiBaseType, BaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, LESSER_RUNE, RUNE, GREATER_RUNE, SOUL_CORE

rules = [
    Show([MultiBaseType(list(SOUL_CORE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(LESSER_RUNE)), TierStyle(TIER.COMMON)]),
    Show([MultiBaseType(list(RUNE)), TierStyle(TIER.RARE)]),
    Show([MultiBaseType(list(GREATER_RUNE)), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(LESSER_RUNE.IRON), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(LESSER_RUNE.DESERT), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(LESSER_RUNE.GLACIAL), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(LESSER_RUNE.STORM), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(RUNE.IRON), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(RUNE.DESERT), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(RUNE.GLACIAL), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(RUNE.STORM), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(GREATER_RUNE.IRON), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(GREATER_RUNE.DESERT), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(GREATER_RUNE.GLACIAL), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(GREATER_RUNE.STORM), TierStyle(TIER.LEGENDARY)]),
]
