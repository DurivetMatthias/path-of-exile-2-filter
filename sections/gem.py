from app.actions import TierStyle
from app.conditions import BaseType, ItemLevel
from app.blocks import Show
from app.categories import TIER, GEM

rules = [
    # Skill
    # Show([TierStyle(TIER.RARE), BaseType(GEM.SKILL)]),
    # Show([TierStyle(TIER.LEGENDARY), ItemLevel(14), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(15), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(16), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(17), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(18), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(19), BaseType(GEM.SKILL)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(20), BaseType(GEM.SKILL)]),
    # Support
    # Show([TierStyle(TIER.LEGENDARY), BaseType(GEM.SUPPORT)]),
    # Show([TierStyle(TIER.LEGENDARY), ItemLevel(1), BaseType(GEM.SUPPORT)]),
    # Show([TierStyle(TIER.LEGENDARY), ItemLevel(2), BaseType(GEM.SUPPORT)]),
    Show([TierStyle(TIER.EPIC), ItemLevel(3), BaseType(GEM.SUPPORT)]),
    # Spirit
    # Show([TierStyle(TIER.LEGENDARY), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(14), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(15), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(16), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(17), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(18), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(19), BaseType(GEM.SPIRIT)]),
    Show([TierStyle(TIER.LEGENDARY), ItemLevel(20), BaseType(GEM.SPIRIT)]),
]
