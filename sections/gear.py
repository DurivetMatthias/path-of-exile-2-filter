from app.conditions import AreaLevel, MultiClass
from app.blocks import Hide
from app.categories import GEAR, WEAPON

rules = [
    Hide(
        [
            AreaLevel(65),
            MultiClass(list(GEAR)),
        ]
    ),
    Hide(
        [
            AreaLevel(65),
            MultiClass(list(WEAPON)),
        ]
    ),
]
