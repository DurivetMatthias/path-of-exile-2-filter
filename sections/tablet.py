from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, TABLET

rules = [
    Show([MultiBaseType(list(TABLET)), TierStyle(TIER.LEGENDARY)]),
]
