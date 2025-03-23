from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, SPLINTER

rules = [
    Show([MultiBaseType(list(SPLINTER)), TierStyle(TIER.COMMON)]),
]
