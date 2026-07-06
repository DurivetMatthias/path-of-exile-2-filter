from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *


rules = [
    # Leveling with shield wall
    Show(
        [
            AreaLevel(65, OPERATOR.LT),
            Class("Shields"),
            PureArmour(),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(65, OPERATOR.LT),
            Class("One Hand Maces"),
            PureArmour(),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(65, OPERATOR.LT),
            GearClasses(),
            PureArmour(),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            AreaLevel(65, OPERATOR.LT),
            JewelryClasses(),
            TierStyle(TIER.EPIC),
        ]
    ),
    # Endgame Gear
    # Show(
    #     [
    #         # BaseType("Massive Mitts"),
    #         Class("Gloves"),
    #         PureArmour(),
    #         Rarity(RARITY.MAGIC, OPERATOR.LTE),
    #         TierStyle(TIER.RARE),
    #     ]
    # ),
    # Show(
    #     [
    #         Class("Boots"),
    #         PureArmour(),
    #         # BaseType("Tasalian Greaves"),
    #         Rarity(RARITY.NORMAL),
    #         TierStyle(TIER.LEGENDARY),
    #     ]
    # ),
    # Show(
    #     [
    #         # BaseType("Imperial Greathelm"),
    #         Class("Helmets"),
    #         PureArmour(),
    #         Rarity(RARITY.MAGIC, OPERATOR.LTE),
    #         TierStyle(TIER.RARE),
    #     ]
    # ),
    # Show(
    #     [
    #         BaseType("Soldier Cuirass"),
    #         Rarity(RARITY.NORMAL),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    # Show(
    #     [
    #         ItemLevel(82),
    #         MultiClass(["Gloves", "Boots", "Helmets"]),
    #         PureArmour(),
    #         # Rarity(RARITY.MAGIC, OPERATOR.LTE),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    # # Weapons
    # Show(
    #     [
    #         ItemLevel(82),
    #         BaseType("Tawhoan Tower Shield"),
    #         # Rarity(RARITY.MAGIC, OPERATOR.LTE),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    # Show(
    #     [
    #         ItemLevel(81, OPERATOR.GTE),
    #         # Rarity(RARITY.MAGIC, OPERATOR.LTE),
    #         Class("One Hand Maces"),
    #         # MultiBaseType(
    #         #     [
    #         #         "Fortified Hammer",
    #         #         "Structured Hammer",
    #         #     ]
    #         # ),
    #         TierStyle(TIER.LEGENDARY),
    #     ]
    # ),
    # Jewelry
    # Show([UnidentifiedItemTier(5), TierStyle(TIER.COMMON)]),
    # Show([BaseType("Vitalic Ring"), TierStyle(TIER.LEGENDARY)]),
    # Show(
    #     [
    #         ItemLevel(65, OPERATOR.GTE),
    #         Rarity(RARITY.NORMAL),
    #         MultiBaseType(
    #             [
    #                 "Ruby Ring",
    #                 "Sapphire Ring",
    #                 "Topaz Ring",
    #                 "Amethyst Ring",
    #                 "Prismatic Ring",
    #                 "Gold Ring",
    #                 "Solar Amulet",
    #                 "Stellar Amulet",
    #                 "Lapis Amulet",
    #                 "Amber Amulet",
    #                 "Jade Amulet",
    #                 "Pearlescent Amulet",
    #             ]
    #         ),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
    # Hide the rest
    Hide([GearClasses()]),
    Hide([WeaponClasses()]),
    Hide([OffhandClasses()]),
    Hide([JewelryClasses()]),
]
