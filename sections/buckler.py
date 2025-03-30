from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, BUCKLER

rules = [
    Show([MultiBaseType(list(BUCKLER)), TierStyle(TIER.EPIC)]),
]
