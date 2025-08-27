from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    # Show all gear since no attribute requirement
    Show(
        [
            AreaLevel(11),
            MultiClass([ARMOUR.BOOTS, ARMOUR.GLOVES, ARMOUR.HELMET, ARMOUR.BODY]),
            TierStyle(TIER.COMMON),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    # Stomping ground
    Show(
        [
            MultiClass([ARMOUR.BOOTS, ARMOUR.GLOVES, ARMOUR.HELMET, ARMOUR.BODY]),
            PureArmour(),
            TierStyle(TIER.EPIC),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            MultiClass([WEAPON.SPEAR]),
            TierStyle(TIER.EPIC),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            MultiClass([OFFHAND.SHIELD]),
            PureArmour(),
            TierStyle(TIER.EPIC),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    # Real build?
    Show(
        [
            MultiClass([WEAPON.BOW, OFFHAND.QUIVER, WEAPON.QUARTERSTAFF]),
            TierStyle(TIER.EPIC),
            FilterLevel(FILTER_LEVEL.MAP_PROGRESSION),
        ]
    ),
    Show(
        [
            MultiClass([ARMOUR.BOOTS, ARMOUR.GLOVES, ARMOUR.HELMET, ARMOUR.BODY]),
            PureEvasion(),
            TierStyle(TIER.EPIC),
            FilterLevel(FILTER_LEVEL.MAP_PROGRESSION),
        ]
    ),
    Show(
        [
            MultiBaseType(["Thawing Charm", "Silver Charm", "Golden Charm"]),
            TierStyle(TIER.EPIC),
            FilterLevel(FILTER_LEVEL.ENDGAME),
        ]
    ),
    # Hide the rest
    Hide([MultiClass(list(ARMOUR))]),
    Hide([MultiClass(list(WEAPON))]),
    Hide([MultiClass(list(OFFHAND))]),
]
