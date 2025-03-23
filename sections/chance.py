from app.conditions import BaseType, Rarity
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, RARITY, RING, BELT, BOW

rules = [
    # Goldrim
    Show([BaseType("Felt Cap"), Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY)]),
    # Ventor's Gamble
    Show([BaseType(RING.GOLD), Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY)]),
    # Widowhail
    Show([BaseType(BOW.CRUDE), Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY)]),
    # Polcirkeln
    Show([BaseType(RING.SAPPHIRE), Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY)]),
    # Headhunter
    Show([BaseType(BELT.HEAVY), Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY)]),
]
