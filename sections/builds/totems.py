from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *


rules = [
    # Gear
    # Show(
    #     [
    #         AreaLevel(1, OPERATOR.LTE),
    #         VendorStyle(),
    #     ]
    # ),
    # Show(
    #     [
    #         AreaLevel(10, OPERATOR.LTE),
    #         Rarity(RARITY.RARE),
    #         VendorStyle(),
    #     ]
    # ),
    # Show(
    #     [
    #         ItemLevel(10, OPERATOR.LTE),
    #         EnergyShieldAndHybrid(),
    #         GearClasses(),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    Show(
        [
            ItemLevel(65, OPERATOR.LT),
            PureArmour(),
            GearClasses(),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Show(
    #     [
    #         ItemLevel(10, OPERATOR.LTE),
    #         MultiClass(["Boots", "Gloves"]),
    #         Rarity(RARITY.MAGIC, OPERATOR.GTE),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    # # Weapons
    Show(
        [
            ItemLevel(65, OPERATOR.LT),
            MultiClass(
                [
                    "Wands",
                    "Sceptres",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Jewelry
    Show(
        [
            ItemLevel(65, OPERATOR.LT),
            JewelryClasses(),
            TierStyle(TIER.RARE),
        ]
    ),
    # Endgame
    Show(
        [
            ItemLevel(65),
            BaseType("Stoic Sceptre"),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(65),
            Class("Body Armours"),
            PureEnergyShield(),
            # PureEnergyShield(150),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(65),
            Class("Helmets"),
            PureEnergyShield(),
            # PureEnergyShield(90),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(65),
            Class("Boots"),
            # PureEnergyShield(68),
            PureEnergyShield(),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(65),
            Class("Gloves"),
            PureEnergyShield(),
            # PureEnergyShield(45),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(65),
            MultiBaseType(
                [
                    # Rings
                    "Topaz Ring",
                    "Sapphire Ring",
                    "Ruby Ring",
                    "Amethyst Ring",
                    "Prismatic Ring",
                    "Pearl Ring",
                    "Lazuli Ring",
                    # Amulets
                    "Azure Amulet",
                    "Amber Amulet",
                    "Lapis Amulet",
                    "Stellar Amulet",
                    "Solar Amulet",
                    "Lunar Amulet",
                    "Pearlescent Amulet",
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            ItemLevel(65),
            Class("Belts"),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Hide the rest
    Hide([GearClasses()]),
    Hide([WeaponClasses()]),
    Hide([OffhandClasses()]),
    Hide([JewelryClasses()]),
]
