from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    # Stomping ground
    Show(
        [
            MultiClass([WEAPON.SPEAR]),
            TierStyle(TIER.EPIC),
            AreaLevel(40),
        ]
    ),
    Show(
        [
            MultiClass([OFFHAND.SHIELD]),
            PureArmour(),
            TierStyle(TIER.EPIC),
            AreaLevel(40),
        ]
    ),
    # Real build?
    Show(
        [
            MultiClass([WEAPON.BOW, OFFHAND.QUIVER, WEAPON.QUARTERSTAFF]),
            TierStyle(TIER.EPIC),
            AreaLevel(40, operator=OPERATOR.GT),
        ]
    ),
]
