from app.conditions import Class
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, WEAPON

rules = [
    Show([TierStyle(TIER.EPIC), Class(WEAPON.SPEAR)]),
]
