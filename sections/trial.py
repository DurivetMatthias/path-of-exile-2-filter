from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *


rules = [
    # Trial of the Sekhema
    Show(
        [
            BaseType(TRIAL.BARYA),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(44),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.BARYA),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(59),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.BARYA),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(63),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.BARYA),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(75),
            FilterLevel(FILTER_LEVEL.ENDGAME),
        ]
    ),
    # Trial of Corruption
    Show(
        [
            BaseType(TRIAL.ULTIMATUM),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(59),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.ULTIMATUM),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(63),
            FilterLevel(FILTER_LEVEL.CAMPAIGN),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.ULTIMATUM),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(75),
            FilterLevel(FILTER_LEVEL.ENDGAME),
        ]
    ),
]
