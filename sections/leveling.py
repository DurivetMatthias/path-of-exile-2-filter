from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *


class VendorStyle(Condition):
    def __str__(self):
        return formatting.format_conditions(
            [
                PlayEffect(COLOR.YELLOW),
                MinimapIcon(SIZE.SMALL, COLOR.YELLOW, SHAPE.DIAMOND),
                SetFontSize(FONT_SIZE.LARGE),
            ]
        )


BEACH = 1
BEFORE_TIER_3_GEM = 5
BEFORE_ACT_2 = 30
rules = [
    Show(
        [
            AreaLevel(BEACH),
            VendorStyle(),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_TIER_3_GEM),
            StackSize(10),
            BaseType("Gold"),
            VendorStyle(),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_TIER_3_GEM),
            Rarity(RARITY.MAGIC),
            Class(GEAR.BOOTS),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            AreaLevel(BEFORE_ACT_2),
            Rarity(RARITY.RARE),
            VendorStyle(),
        ]
    ),
]
