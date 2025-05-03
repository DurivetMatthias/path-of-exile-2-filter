from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, RELIC

rules = [
    Show([MultiBaseType(list(RELIC)), TierStyle(TIER.LEGENDARY)]),
]
