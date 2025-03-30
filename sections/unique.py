from app.actions import TierStyle
from app.conditions import Rarity, BaseType
from app.blocks import Show
from app.categories import RARITY, TIER

bases = [
    "Scale Mail"  # Doryani's Prototype
    "Gold Ring"  # Ventor's Gamble
    "Sapphire Ring"  # Polcirkeln
    "Long Quarterstaff"  # Pillar of the Caged God
    "Crude Bow"  # Widowhail
    "Quilted Vest"  # Foxshade
    "Smuggler Coat"  # Queen of the Forest
    "Silk Robe"  # Cloak of Flame
    "Brimmed Helm"  # Greymake
    "Gold Circlet"  # Atziri's Disdain
    "Ring"  # Kalandra's Touch
]

rules = [
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.EPIC)]),
]
rules.extend(
    Show([Rarity(RARITY.NORMAL), TierStyle(TIER.EPIC), BaseType(name)])
    for name in bases
)
rules.extend(
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.LEGENDARY), BaseType(name)])
    for name in bases
)
