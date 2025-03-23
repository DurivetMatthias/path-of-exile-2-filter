from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, OMEN

rules = [
    Show([MultiBaseType(list(OMEN)), TierStyle(TIER.LEGENDARY)]),
]
