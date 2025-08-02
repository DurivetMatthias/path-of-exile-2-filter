from app.conditions import MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, BOW, QUIVER

rules = [
    # Show([MultiBaseType(list(BOW)), TierStyle(TIER.EPIC)]),
    # Show([MultiBaseType(list(QUIVER)), TierStyle(TIER.EPIC)]),
    Show(
        [
            MultiBaseType(list(BOW)[-7:]),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    QUIVER.PRIMED,
                    QUIVER.VISCERAL,
                    QUIVER.VOLANT,
                    QUIVER.TWO_POINT,
                    QUIVER.FIRE,
                    QUIVER.BROAD,
                ]
            ),
            TierStyle(TIER.EPIC),
        ]
    ),
]
