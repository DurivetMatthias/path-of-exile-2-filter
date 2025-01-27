from app.conditions import BaseType, StackSize
from app.actions import TierStyle
from app.blocks import Show, Hide
from app.categories import TIER

config = [
    # TODO: separate scroll logic
    # {"name": "Scroll of Wisdom", "tier": TIER.COMMON},
    # Basic currency
    {"name": "Orb of Augmentation", "tier": TIER.COMMON},
    {"name": "Orb of Transmutation", "tier": TIER.RARE},
    {"name": "Regal Orb", "tier": TIER.EPIC},
    {"name": "Orb of Alchemy", "tier": TIER.EPIC},
    {"name": "Orb of Chance", "tier": TIER.LEGENDARY},
    {"name": "Exalted Orb", "tier": TIER.LEGENDARY},
    {"name": "Orb of Annulment", "tier": TIER.LEGENDARY},
    {"name": "Chaos Orb", "tier": TIER.LEGENDARY},
    {"name": "Divine Orb", "tier": TIER.LEGENDARY},
    {"name": "Vaal Orb", "tier": TIER.LEGENDARY},
    {"name": "Lesser Jeweller's Orb", "tier": TIER.EPIC},
    {"name": "Greater Jeweller's Orb", "tier": TIER.LEGENDARY},
    {"name": "Perfect Jeweller's Orb", "tier": TIER.LEGENDARY},
    {"name": "Artificer's Orb", "tier": TIER.EPIC},
    # Basic shards
    {"name": "Transmutation Shard", "tier": TIER.RARE},
    {"name": "Regal Shard", "tier": TIER.RARE},
    {"name": "Chance Shard", "tier": TIER.EPIC},
    # Quality currency
    {"name": "Arcanist's Etcher", "tier": TIER.RARE},
    {"name": "Armourer's Scrap", "tier": TIER.RARE},
    {"name": "Blacksmith's Whetstone", "tier": TIER.RARE},
    {"name": "Gemcutter's Prism", "tier": TIER.LEGENDARY},
    {"name": "Glassblower's Bauble", "tier": TIER.LEGENDARY},
    # Trial of Chaos currency
    {"name": "Inscribed Ultimatum", "tier": TIER.LEGENDARY},
    # Trial of the Sekhema currency
    {"name": "Djinn Barya", "tier": TIER.LEGENDARY},
]

currency_rules = [
    Show([BaseType(item["name"]), TierStyle(item["tier"])]) for item in config
]

rules = [
    *currency_rules,
    Show([BaseType("Gold"), StackSize(1000)]),
    Hide([BaseType("Gold")]),
]
