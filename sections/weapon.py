from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, SPEAR

rules = [
    Show([MultiBaseType(list(SPEAR)), TierStyle(TIER.EPIC)]),
]
