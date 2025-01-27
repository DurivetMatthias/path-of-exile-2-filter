from app.conditions import BaseType, MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, OPERATOR


# Trial of the Sekhema currency
# {"name": "Order Artifact", "tier": TIER.RARE},
# {"name": "Black Scythe Artifact", "tier": TIER.RARE},
# {"name": "Sun Artifact", "tier": TIER.RARE},
# {"name": "Broken Circle Artifact", "tier": TIER.RARE},
# {"name": "Exotic Coinage", "tier": TIER.RARE},

rules = [
    Show(
        [
            BaseType("Expedition Logbook"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            BaseType("Exotic Coinage"),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Order Artifact",
                    "Black Scythe Artifact",
                    "Sun Artifact",
                    "Broken Circle Artifact",
                ]
            ),
            TierStyle(TIER.RARE),
        ]
    ),
]
