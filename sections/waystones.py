# Socketable
from app.conditions import Class
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER

rules = [
    Show(
        [
            Class("Waystones"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Class("Tablet"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
