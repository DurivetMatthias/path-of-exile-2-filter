from app.conditions import BaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER

config = [
    # Basic currency
    {"name": "Orb of Transmutation", "tier": TIER.COMMON},
    {"name": "Orb of Augmentation", "tier": TIER.COMMON},
    {"name": "Orb of Alchemy", "tier": TIER.RARE},
    {"name": "Orb of Chance", "tier": TIER.RARE},
    {"name": "Regal Orb", "tier": TIER.COMMON},
    {"name": "Exalted Orb", "tier": TIER.COMMON},
    {"name": "Orb of Annulment", "tier": TIER.COMMON},
    {"name": "Chaos Orb", "tier": TIER.COMMON},
    {"name": "Divine Orb", "tier": TIER.COMMON},
    {"name": "Vaal Orb", "tier": TIER.COMMON},
    {"name": "Lesser Jeweller's Orb", "tier": TIER.COMMON},
    {"name": "Greater Jeweller's Orb", "tier": TIER.COMMON},
    {"name": "Perfect Jeweller's Orb", "tier": TIER.COMMON},
    {"name": "Artificer's Orb", "tier": TIER.COMMON},
    # Basic shards
    {"name": "Transmutation Shard", "tier": TIER.COMMON},
    {"name": "Regal Shard", "tier": TIER.COMMON},
    {"name": "Chance Shard", "tier": TIER.COMMON},
    # Uncut gems
    {"name": "Uncut Skill Gem", "tier": TIER.COMMON},
    {"name": "Uncut Support Gem", "tier": TIER.COMMON},
    {"name": "Uncut Spirit Gem", "tier": TIER.COMMON},
    # Quality currency
    {"name": "Arcanist's Etcher", "tier": TIER.COMMON},
    {"name": "Armourer's Scrap", "tier": TIER.COMMON},
    {"name": "Blacksmith's Whetstone", "tier": TIER.COMMON},
    {"name": "Gemcutter's Prism", "tier": TIER.COMMON},
    # Runes
    {"name": "Body Rune", "tier": TIER.COMMON},
    {"name": "Desert Rune", "tier": TIER.COMMON},
    {"name": "Glacial Rune", "tier": TIER.COMMON},
    {"name": "Mind Rune", "tier": TIER.COMMON},
    # Breach currency
    {"name": "Breach Splinter", "tier": TIER.COMMON},
    {"name": "Breachstone", "tier": TIER.COMMON},
    {"name": "Flesh Catalyst", "tier": TIER.COMMON},
    {"name": "Reaver Catalyst", "tier": TIER.COMMON},
    {"name": "Tul's Catalyst", "tier": TIER.COMMON},
    {"name": "Xoph's Catalyst", "tier": TIER.COMMON},
    # Expedition currency
    {"name": "Broken Circle Artifact", "tier": TIER.COMMON},
    # Delirium currency
    {"name": "Simulacrum Splinter", "tier": TIER.COMMON},
    {"name": "Simulacrum", "tier": TIER.COMMON},
    {"name": "Distilled Despair", "tier": TIER.COMMON},
    {"name": "Distilled Disgust", "tier": TIER.COMMON},
    {"name": "Distilled Greed", "tier": TIER.COMMON},
    {"name": "Distilled Guiltœ", "tier": TIER.COMMON},
    {"name": "Distilled Ire", "tier": TIER.COMMON},
    {"name": "Distilled Paranoia", "tier": TIER.COMMON},
    {"name": "Distilled Suffering", "tier": TIER.COMMON},
    # Essence currency
    {"name": "Essence of Haste", "tier": TIER.COMMON},
    {"name": "Essence of Ice", "tier": TIER.COMMON},
    {"name": "Essence of the Body", "tier": TIER.COMMON},
    {"name": "Greater Essence of Haste", "tier": TIER.COMMON},
    {"name": "Greater Essence of Ice", "tier": TIER.COMMON},
    {"name": "Greater Essence of the Body", "tier": TIER.COMMON},
    # Ritual currency
    {"name": "Omen of Dextral Annulment", "tier": TIER.COMMON},
    {"name": "Omen of Greater Exaltation", "tier": TIER.COMMON},
    {"name": "Omen of Sinistral Exaltation", "tier": TIER.COMMON},
    # Trial of Chaos currency
    {"name": "Soul Core of Azcapa", "tier": TIER.COMMON},
    {"name": "Soul Core of Quipolatl", "tier": TIER.COMMON},
    {"name": "Soul Core of Thunder", "tier": TIER.COMMON},
    {"name": "Soul Core of Ticaba", "tier": TIER.COMMON},
    {"name": "Soul Core of Topotante", "tier": TIER.COMMON},
]

rules = [Show([BaseType(item["name"]), TierStyle(item["tier"])]) for item in config]
