from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, CATALYST

rules = [
    Show([MultiBaseType(list(CATALYST)), TierStyle(TIER.EPIC)]),
]
