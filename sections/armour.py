from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            AreaLevel(5),
            MultiClass(list(ARMOUR)),
            TierStyle(TIER.COMMON),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    # Stomping ground
    Show(
        [
            AreaLevel(40),
            MultiClass([ARMOUR.BOOTS, ARMOUR.GLOVES, ARMOUR.HELMET, ARMOUR.BODY]),
            PureArmour(),
            TierStyle(TIER.EPIC),
            Strictness(STRICTNESS.STRICT),
        ]
    ),
    # Dex build?
    Show(
        [
            AreaLevel(40, operator=OPERATOR.GTE),
            MultiClass([ARMOUR.BOOTS, ARMOUR.GLOVES, ARMOUR.HELMET, ARMOUR.BODY]),
            PureEvasion(),
            TierStyle(TIER.COMMON),
        ]
    ),
]
