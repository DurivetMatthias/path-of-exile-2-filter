from app.actions import TierStyle
from app.conditions import Rarity, BaseType
from app.blocks import Show
from app.categories import RARITY, TIER

bases = [
    "Scale Mail",  # Doryani's Prototype
    "Gold Ring",  # Ventor's Gamble
    # "Sapphire Ring",  # Polcirkeln
    # "Long Quarterstaff",  # Pillar of the Caged God
    # "Crude Bow",  # Widowhail
    # "Quilted Vest",  # Foxshade
    "Smuggler Coat",  # Queen of the Forest
    # "Silk Robe",  # Cloak of Flame
    # "Brimmed Helm",  # Greymake
    # "Gold Circlet",  # Atziri's Disdain
    # "Rampart Tower Shield",  # Lycosidae
    # "Braced Sabatons",  # Darkray Vectors
    # "Jewelled Gloves",  # Kitoko's Current
    "Dousing Charm",  # Beira's Anguish
    "Silver Charm",  # The Fall of the Axe
    "Antidote Charm",  # "Arakaali's Gift
    "Golden Charm",  # Rite of Passage
    "Double Belt",  # Bijouborne
    "Execratus Hammer",  # Nebuloch
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
