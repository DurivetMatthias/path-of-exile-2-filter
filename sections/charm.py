from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, CHARM

rules = [
    Show([MultiBaseType(list(CHARM)), TierStyle(TIER.RARE)]),
]
