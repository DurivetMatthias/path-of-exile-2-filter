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
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.BARYA),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(59),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.BARYA),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(63),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.BARYA),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(75),
            Strictness(STRICTNESS.UBER),
        ]
    ),
    # Trial of Corruption
    Show(
        [
            BaseType(TRIAL.ULTIMATUM),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(59),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.ULTIMATUM),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(63),
            Strictness(STRICTNESS.REGULAR),
        ]
    ),
    Show(
        [
            BaseType(TRIAL.ULTIMATUM),
            TierStyle(TIER.LEGENDARY),
            ItemLevel(75),
            Strictness(STRICTNESS.UBER),
        ]
    ),
]
