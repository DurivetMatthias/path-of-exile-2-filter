from app.conditions import MultiClass
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, JEWELRY

rules = [
    Show([MultiClass(list(JEWELRY)), TierStyle(TIER.EPIC)]),
]
