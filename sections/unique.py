from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

bases = [
    # "Gold Ring",  # Ventor's Gamble
    "Heavy Belt",  # Headhunter
]

rules = [
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.EPIC)]),
]
rules.extend(
    Show([Rarity(RARITY.NORMAL), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
rules.extend(
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
