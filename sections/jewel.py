from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER

rules = [
    Show(
        [
            MultiBaseType(
                [
                    "Ruby",
                    "Emerald",
                    "Sapphire",
                    "Diamond",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Time-Lost Ruby",
                    "Time-Lost Emerald",
                    "Time-Lost Sapphire",
                    "Time-Lost Diamond",
                    "Timeless Jewel",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
