from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, SPEAR, WAND

rules = [
    # Show([MultiBaseType([SPEAR.SEAGLASS]), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType([WAND.ATTUNED, WAND.SIPHONING]), TierStyle(TIER.LEGENDARY)]),
]
