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


GLASSBLOWER = [
    GEAR.CHARM,
    FLASK.LIFE,
    FLASK.MANA,
]

# TODO style for vendor items
rules = [
    Show(
        [
            Rarity(RARITY.RARE),
            VendorStyle(),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            Quality(),
            MultiClass(GLASSBLOWER),
            VendorStyle(),
        ]
    ),
]
