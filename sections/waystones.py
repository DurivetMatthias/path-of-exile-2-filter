from app.conditions import Class, MapTier
from app.actions import TierStyle
from app.blocks import Show, Hide
from app.categories import TIER, OPERATOR

rules = [
    Show(
        [
            Class("Waystones"),
            MapTier(15),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Class("Waystones"),
            MapTier(1, operator=OPERATOR.EQUAL),
            TierStyle(TIER.RARE),
        ]
    ),
    Show(
        [
            Class("Tablet"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Hide(
        [
            Class("Waystones"),
        ]
    ),
]

# Item Class: Waystones
# Rarity: Normal
# Waystone (Tier 3)
# --------
# Waystone Tier: 3
# --------
# Item Level: 80
# --------
# Can be used in a Map Device, allowing you to enter a Map. Waystones can only be used once.
