from app.conditions import Rarity, ItemLevel
from app.blocks import Show
from app.categories import RARITY

# Showing Tiered items is not supported yet, show them without highlight for now
rules = [
    # Show(
    #     [
    #         Rarity(RARITY.RARE),
    #         ItemLevel(71),  # Resists
    #     ]
    # ),
]
