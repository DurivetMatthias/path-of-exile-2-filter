from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show([Class("Quest Items"), TierStyle(TIER.COMMON)]),
    Show([MultiBaseType(list(SPLINTER)), TierStyle(TIER.COMMON)]),
    Show([MultiBaseType(list(CHARM)), TierStyle(TIER.RARE)]),
    Show([MultiBaseType(list(RELIC)), TierStyle(TIER.RARE)]),
    Show([MultiBaseType(list(ARTIFACT)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(CATALYST)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(EMOTION)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(GREATER_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(CORRUPT_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(INVITATION)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(OMEN)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(RELIQUARY_KEY)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(TABLET)), TierStyle(TIER.LEGENDARY)]),
]
