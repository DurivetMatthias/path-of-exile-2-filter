from app.blocks import Show
from app.actions import TierStyle
from app.conditions import MultiClass, BaseEnergyShield, BaseEvasion
from app.categories import TIER, ARMOUR

rules = [
    # Show(
    #     [
    #         MultiClass(list(ARMOUR)),
    #         BaseEnergyShield(),
    #         BaseEvasion(),
    #         TierStyle(TIER.COMMON),
    #     ]
    # ),
    Show(
        [
            MultiClass([ARMOUR.BOOTS]),
            BaseEnergyShield(35),
            BaseEvasion(),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiClass([ARMOUR.GLOVES]),
            BaseEnergyShield(23),
            BaseEvasion(),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiClass([ARMOUR.HELMET]),
            BaseEnergyShield(46),
            BaseEvasion(),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiClass([ARMOUR.BODY]),
            BaseEnergyShield(101),
            BaseEvasion(),
            TierStyle(TIER.COMMON),
        ]
    ),
]
