from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *


def get_weapon_rules(archetype: ARCHETYPE):
    if archetype == ARCHETYPE.INT:
        return [
            Show(
                [
                    MultiClass(
                        [WEAPON.WAND, WEAPON.STAFF, OFFHAND.FOCUS, WEAPON.SCEPTRE]
                    ),
                    TierStyle(TIER.COMMON),
                ]
            )
        ]


def get_armour_rules(archetype: ARCHETYPE):
    if archetype == ARCHETYPE.INT:
        return [
            Show(
                [
                    PureEnergyShield(),
                    TierStyle(TIER.COMMON),
                ]
            )
        ]
