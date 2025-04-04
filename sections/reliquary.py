from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, RELIQUARY_KEY

rules = [
    Show([MultiBaseType(list(RELIQUARY_KEY)), TierStyle(TIER.LEGENDARY)]),
]
