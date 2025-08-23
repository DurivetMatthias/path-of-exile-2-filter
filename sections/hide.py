from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

rules = [
    # Show all in starting area
    Show([AreaLevel(1), TierStyle(TIER.COMMON)]),
    # MultiClass
    Hide([MultiClass(list(GEAR))]),
    Hide([MultiClass(list(FLASK))]),
    Hide([MultiClass(list(WEAPON))]),
    Hide([MultiClass(list(OFFHAND))]),
    # MultiBaseType
    Hide([MultiBaseType(list(GEM))]),
    Hide([MultiBaseType(list(TRIAL))]),
    Hide([MultiBaseType(list(CURRENCY))]),
]
