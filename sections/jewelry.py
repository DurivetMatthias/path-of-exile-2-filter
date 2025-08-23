from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    Show(
        [
            MultiClass(list(JEWELRY)),
            TierStyle(TIER.EPIC),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    RING.RUBY,
                    RING.SAPPHIRE,
                    RING.TOPAZ,
                    RING.BREACH,
                    RING.PRISMATIC,
                    RING.AMETHYST,
                    RING.GOLD,
                    AMULET.LAPIS,
                    AMULET.JADE,
                    AMULET.AMBER,
                    AMULET.STELLAR,
                    AMULET.SOLAR,
                    AMULET.BLOODSTONE,
                    AMULET.LUNAR,
                    AMULET.GOLD,
                    *list(BELT),
                ]
            ),
            TierStyle(TIER.EPIC),
            Strictness(STRICTNESS.UBER),
        ]
    ),
]
