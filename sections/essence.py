from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, ESSENCE, GREATER_ESSENCE, CORRUPT_ESSENCE

rules = [
    Show([MultiBaseType(list(ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(GREATER_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(CORRUPT_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
]
