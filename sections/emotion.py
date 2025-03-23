from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, EMOTION

rules = [
    Show([MultiBaseType(list(EMOTION)), TierStyle(TIER.EPIC)]),
]
