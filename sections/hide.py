from app.conditions import MultiClass, MultiBaseType
from app.blocks import Hide
from app.categories import GEAR, OFFHAND, WEAPON, FLASK, CURRENCY, TRIAL

rules = [
    Hide([MultiClass(list(GEAR))]),
    Hide([MultiClass(list(OFFHAND))]),
    Hide([MultiClass(list(WEAPON))]),
    Hide([MultiClass(list(FLASK))]),
    Hide([MultiBaseType(list(CURRENCY))]),
    Hide([MultiBaseType(list(TRIAL))]),
]
