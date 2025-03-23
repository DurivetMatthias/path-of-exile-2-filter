from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, ESSENCE, GREATER_ESSENCE

rules = [
    Show([MultiBaseType(list(ESSENCE)), TierStyle(TIER.EPIC)]),
    Show([MultiBaseType(list(GREATER_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
]
