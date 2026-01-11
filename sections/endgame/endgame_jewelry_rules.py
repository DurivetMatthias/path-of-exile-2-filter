from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *
from sections.endgame.waystone_tiers import *


def endgame_jewelry_rules():
    bases = [
        # Rings
        "Ruby Ring",
        "Sapphire Ring",
        "Topaz Ring",
        "Prismatic Ring",
        "Amethyst Ring",
        # Amulets
        "Amber Amulet",
        "Jade Amulet",
        "Lapis Amulet",
        "Stellar Amulet",
        "Bloodstone Amulet",
        "Solar Amulet",
        # Belts
        "Fine Belt",
        "Utility Belt",
        "Plate Belt",
        "Mail Belt",
        "Rawhide Belt",
    ]
    rules = [
        # 1-5 normal and magic
        Show(
            [
                AreaLevel(TIER_1, OPERATOR.GTE),
                AreaLevel(TIER_5, OPERATOR.LTE),
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                MultiBaseType(bases),
                TierStyle(TIER.EPIC),
            ]
        ),
        # 6-10 only normal
        Show(
            [
                AreaLevel(TIER_6, OPERATOR.GTE),
                AreaLevel(TIER_10, OPERATOR.LTE),
                Rarity(RARITY.NORMAL),
                MultiBaseType(bases),
                TierStyle(TIER.EPIC),
            ]
        ),
        # 11+ only normal
        Show(
            [
                AreaLevel(TIER_11, OPERATOR.GTE),
                Rarity(RARITY.NORMAL),
                MultiBaseType(bases),
                TierStyle(TIER.EPIC),
            ]
        ),
    ]

    return rules
