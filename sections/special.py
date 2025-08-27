from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    # Show all in starting area
    Show([AreaLevel(1), TierStyle(TIER.COMMON)]),
]
