from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, RING, AMULET, BELT

rules = [
    Show(
        [
            MultiBaseType(
                [
                    RING.PRISMATIC,
                    RING.SAPPHIRE,
                    RING.RUBY,
                    RING.TOPAZ,
                    RING.AMETHYST,
                    RING.GOLD,
                    RING.BREACH,
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # Show(
    #     [
    #         MultiBaseType(
    #             [
    #                 AMULET.SOLAR,
    #                 AMULET.LUNAR,
    #                 AMULET.GOLD,
    #             ]
    #         ),
    #         TierStyle(TIER.LEGENDARY),
    #     ]
    # ),
    # Just everything for recombination
    # Show([MultiBaseType(list(AMULET)), TierStyle(TIER.EPIC)]),
    # Show([MultiBaseType(list(RING)), TierStyle(TIER.EPIC)]),
    # Show([MultiBaseType(list(BELT)), TierStyle(TIER.EPIC)]),
]
