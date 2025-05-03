from app.conditions import MultiBaseType, MultiClass, BaseEvasion, BaseArmour
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER, BUCKLER

rules = [
    # Show([MultiBaseType(list(BUCKLER)), TierStyle(TIER.EPIC)]),
    # Show([MultiClass(["Sceptres"]), TierStyle(TIER.EPIC)]),
    # Show(
    #     [
    #         MultiClass(["Shields"]),
    #         BaseArmour(),
    #         BaseEvasion(),
    #         TierStyle(TIER.EPIC),
    #     ]
    # ),
]
