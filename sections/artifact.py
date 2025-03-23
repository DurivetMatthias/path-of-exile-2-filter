from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, ARTIFACT

rules = [
    Show([MultiBaseType(list(ARTIFACT)), TierStyle(TIER.RARE)]),
]
