from app.conditions import BaseType, Rarity
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, RARITY, OPERATOR, RING, BELT

rules = [
    # Goldrim
    Show(
        [
            BaseType("Felt Cap"),
            Rarity(RARITY.NORMAL, operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Ventor's Gamble
    Show(
        [
            BaseType(RING.GOLD),
            Rarity(RARITY.NORMAL, operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Widowhail
    Show(
        [
            BaseType("Crude Bow"),
            Rarity(RARITY.NORMAL, operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Polcirkeln
    Show(
        [
            BaseType(RING.SAPPHIRE),
            Rarity(RARITY.NORMAL, operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Headhunter
    Show(
        [
            BaseType(BELT.HEAVY),
            Rarity(RARITY.NORMAL, operator=OPERATOR.EQUAL),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
]
