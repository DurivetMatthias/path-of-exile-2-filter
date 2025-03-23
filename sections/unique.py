from app.actions import TierStyle
from app.conditions import Rarity
from app.blocks import Show
from app.categories import RARITY, TIER

rules = [
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.LEGENDARY)]),
]
