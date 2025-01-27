from app.conditions import BaseEvasion, BaseEnergyShield, BaseArmour, MultiClass
from app.actions import TierStyle
from app.blocks import Show

from app.categories import TIER, GEAR, OPERATOR

rules = [
    Show(
        [
            MultiClass(
                [
                    GEAR.BODY_ARMOUR,
                    GEAR.HELMET,
                    GEAR.GLOVES,
                    GEAR.BOOTS,
                ]
            ),
            BaseArmour(0, operator=OPERATOR.EQUAL),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiClass(
                [
                    GEAR.RING,
                    GEAR.AMULET,
                    GEAR.BELT,
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
]
