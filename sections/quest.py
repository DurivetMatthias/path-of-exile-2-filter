from app.conditions import Class
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER

rules = [
    Show(
        [
            Class("Quest Items"),
            TierStyle(TIER.COMMON),
        ]
    ),
]
