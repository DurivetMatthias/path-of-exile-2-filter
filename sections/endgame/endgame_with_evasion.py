from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *


def leveling_with_evasion():
    rules = [
        # Evasion
        Show(
            [
                ItemLevel(65),
                Rarity(RARITY.NORMAL),
                PureEvasion(),
                MultiClass(
                    [
                        GEAR.GLOVES,
                        GEAR.BOOTS,
                    ]
                ),
                TierStyle(TIER.EPIC),
            ]
        ),
        Show(
            [
                ItemLevel(65),
                Rarity(RARITY.MAGIC, OPERATOR.LTE),
                PureEvasion(200),
                MultiClass(
                    [
                        GEAR.HELMET,
                    ]
                ),
                TierStyle(TIER.EPIC),
            ]
        ),
        Show(
            [
                ItemLevel(65),
                Rarity(RARITY.NORMAL),
                PureEvasion(300),
                MultiClass(
                    [
                        GEAR.BODY_ARMOUR,
                    ]
                ),
                TierStyle(TIER.EPIC),
            ]
        ),
        Show(
            [
                ItemLevel(65),
                Rarity(RARITY.NORMAL),
                MultiBaseType(
                    [
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
                    ]
                ),
                TierStyle(TIER.EPIC),
            ]
        ),
        Show(
            [
                ItemLevel(65),
                Rarity(RARITY.NORMAL),
                MultiBaseType(
                    [
                        # Rings
                        "Fine Belt",
                        "Utility Belt",
                        "Plate Belt",
                        "Mail Belt",
                        "Rawhide Belt",
                    ]
                ),
                TierStyle(TIER.COMMON),
            ]
        ),
    ]

    return rules
