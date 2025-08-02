from app.conditions import MultiBaseType, BaseType, Class
from app.actions import TierStyle
from app.blocks import Show
from app.categories import (
    ARTIFACT,
    CATALYST,
    CHARM,
    EMOTION,
    ESSENCE,
    GREATER_ESSENCE,
    CORRUPT_ESSENCE,
    INVITATION,
    OMEN,
    RELIC,
    RELIQUARY_KEY,
    CURRENCY,
    SPLINTER,
    TABLET,
    TIER,
)

rules = [
    Show([MultiBaseType(list(ARTIFACT)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(CATALYST)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(CHARM)), TierStyle(TIER.RARE)]),
    Show([MultiBaseType(list(EMOTION)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(GREATER_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(CORRUPT_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(INVITATION)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(OMEN)), TierStyle(TIER.LEGENDARY)]),
    Show([Class("Quest Items"), TierStyle(TIER.COMMON)]),
    Show([MultiBaseType(list(RELIC)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(RELIQUARY_KEY)), TierStyle(TIER.LEGENDARY)]),
    Show([BaseType(CURRENCY.WISDOM), TierStyle(TIER.COMMON)]),
    Show([MultiBaseType(list(SPLINTER)), TierStyle(TIER.COMMON)]),
    Show([MultiBaseType(list(TABLET)), TierStyle(TIER.LEGENDARY)]),
]
