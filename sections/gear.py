from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *

from sections.endgame.endgame_evasion_rules import *
from sections.endgame.endgame_jewelry_rules import *

# TODO define presets and breakpoints
# eg. pre-maps, white maps, T15 maps
# Import whatever is needed without rewriting every time

rules = [
    # Gear
    *endgame_evasion_rules(),
    *endgame_jewelry_rules(),
    # Hide the rest
    Hide([MultiClass(list(ARMOUR))]),
    Hide([MultiClass(list(WEAPON))]),
    Hide([MultiClass(list(OFFHAND))]),
    Hide([MultiClass(list(JEWELRY))]),
]
