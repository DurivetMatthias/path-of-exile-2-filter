from app.conditions import (
    MultiClass,
    Class,
    BaseEvasion,
    BaseArmour,
    BaseEnergyShield,
    BaseType,
    MultiBaseType,
)
from app.actions import TierStyle
from app.blocks import Hide, Show
from app.categories import GEAR, WEAPON, TIER, OPERATOR, RING

dex_config = {
    GEAR.BODY_ARMOUR: 400,
    GEAR.HELMET: 200,
    GEAR.BOOTS: 160,
    GEAR.GLOVES: 100,
}

dex_gear_rules = [
    Show(
        [
            Class(key),
            BaseArmour(0, operator=OPERATOR.EQUAL),
            BaseEnergyShield(0, operator=OPERATOR.EQUAL),
            BaseEvasion(value, operator=OPERATOR.GTE),
            TierStyle(TIER.LEGENDARY),
        ]
    )
    for key, value in dex_config.items()
]

staff_rules = [
    Show(
        [
            BaseType("Gelid Staff"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Class(WEAPON.STAFF),
            TierStyle(TIER.COMMON),
        ]
    ),
]

ring_rules = [
    Show(
        [
            MultiBaseType(
                [
                    RING.AMETHYST,
                    RING.GOLD,
                    RING.PRISMATIC,
                    RING.RUBY,
                    RING.SAPPHIRE,
                    RING.SAPPHIRE,
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
]

belt_rules = [
    Show(
        [
            Class(GEAR.BELT),
            TierStyle(TIER.COMMON),
        ]
    ),
]

amulet_rules = [
    Show(
        [
            Class(GEAR.AMULET),
            TierStyle(TIER.COMMON),
        ]
    ),
]

hide_the_rest = [
    Hide(
        [
            MultiClass(list(GEAR)),
        ]
    ),
    Hide(
        [
            MultiClass(list(WEAPON)),
        ]
    ),
    Hide(
        [
            MultiClass(
                [
                    "Shields",
                    "Foci",
                    "Quivers",
                ]
            ),
        ]
    ),
]

rules = [
    *dex_gear_rules,
    *staff_rules,
    *ring_rules,
    *belt_rules,
    *amulet_rules,
    *hide_the_rest,
]
