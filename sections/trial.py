from app.conditions import BaseType, ItemLevel
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, TRIAL


rules = [
    # Trial of the Sekhema
    Show([BaseType(TRIAL.BARYA), TierStyle(TIER.LEGENDARY), ItemLevel(44)]),
    Show([BaseType(TRIAL.BARYA), TierStyle(TIER.LEGENDARY), ItemLevel(59)]),
    Show([BaseType(TRIAL.BARYA), TierStyle(TIER.LEGENDARY), ItemLevel(63)]),
    Show([BaseType(TRIAL.BARYA), TierStyle(TIER.LEGENDARY), ItemLevel(75)]),
    # Trial of Corruption
    Show([BaseType(TRIAL.ULTIMATUM), TierStyle(TIER.LEGENDARY), ItemLevel(59)]),
    Show([BaseType(TRIAL.ULTIMATUM), TierStyle(TIER.LEGENDARY), ItemLevel(63)]),
    Show([BaseType(TRIAL.ULTIMATUM), TierStyle(TIER.LEGENDARY), ItemLevel(75)]),
]
