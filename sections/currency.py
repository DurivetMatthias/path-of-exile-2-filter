from app.conditions import BaseType, Class
from app.actions import TierStyle
from app.blocks import Show
from app.categories import TIER

config = [
    {"name": "Gold", "tier": TIER.COMMON},
    # Basic currency
    {"name": "Orb of Transmutation", "tier": TIER.RARE},
    {"name": "Orb of Augmentation", "tier": TIER.RARE},
    {"name": "Orb of Alchemy", "tier": TIER.RARE},
    {"name": "Orb of Chance", "tier": TIER.RARE},
    {"name": "Regal Orb", "tier": TIER.RARE},
    {"name": "Exalted Orb", "tier": TIER.LEGENDARY},
    {"name": "Orb of Annulment", "tier": TIER.RARE},
    {"name": "Chaos Orb", "tier": TIER.RARE},
    {"name": "Divine Orb", "tier": TIER.RARE},
    {"name": "Vaal Orb", "tier": TIER.RARE},
    {"name": "Lesser Jeweller's Orb", "tier": TIER.LEGENDARY},
    {"name": "Greater Jeweller's Orb", "tier": TIER.LEGENDARY},
    {"name": "Perfect Jeweller's Orb", "tier": TIER.LEGENDARY},
    {"name": "Artificer's Orb", "tier": TIER.RARE},
    # Basic shards
    {"name": "Transmutation Shard", "tier": TIER.RARE},
    {"name": "Regal Shard", "tier": TIER.RARE},
    {"name": "Chance Shard", "tier": TIER.RARE},
    # Uncut gems
    {"name": "Uncut Skill Gem", "tier": TIER.RARE},
    {"name": "Uncut Support Gem", "tier": TIER.RARE},
    {"name": "Uncut Spirit Gem", "tier": TIER.RARE},
    # Quality currency
    {"name": "Arcanist's Etcher", "tier": TIER.RARE},
    {"name": "Armourer's Scrap", "tier": TIER.RARE},
    {"name": "Blacksmith's Whetstone", "tier": TIER.RARE},
    {"name": "Gemcutter's Prism", "tier": TIER.RARE},
    # Runes
    {"name": "Body Rune", "tier": TIER.RARE},
    {"name": "Desert Rune", "tier": TIER.RARE},
    {"name": "Glacial Rune", "tier": TIER.RARE},
    {"name": "Mind Rune", "tier": TIER.RARE},
    # Breach currency
    {"name": "Breach Splinter", "tier": TIER.RARE},
    {"name": "Breachstone", "tier": TIER.RARE},
    {"name": "Flesh Catalyst", "tier": TIER.RARE},
    {"name": "Reaver Catalyst", "tier": TIER.RARE},
    {"name": "Tul's Catalyst", "tier": TIER.RARE},
    {"name": "Xoph's Catalyst", "tier": TIER.RARE},
    # Expedition currency
    {"name": "Broken Circle Artifact", "tier": TIER.RARE},
    # Delirium currency
    {"name": "Simulacrum Splinter", "tier": TIER.RARE},
    {"name": "Simulacrum", "tier": TIER.RARE},
    {"name": "Distilled Despair", "tier": TIER.RARE},
    {"name": "Distilled Disgust", "tier": TIER.RARE},
    {"name": "Distilled Greed", "tier": TIER.RARE},
    {"name": "Distilled Guilt", "tier": TIER.RARE},
    {"name": "Distilled Ire", "tier": TIER.RARE},
    {"name": "Distilled Paranoia", "tier": TIER.RARE},
    {"name": "Distilled Suffering", "tier": TIER.RARE},
    # Essence currency
    {"name": "Essence of Haste", "tier": TIER.RARE},
    {"name": "Essence of Ice", "tier": TIER.RARE},
    {"name": "Essence of the Body", "tier": TIER.RARE},
    {"name": "Greater Essence of Haste", "tier": TIER.RARE},
    {"name": "Greater Essence of Ice", "tier": TIER.RARE},
    {"name": "Greater Essence of the Body", "tier": TIER.RARE},
    # Ritual currency
    {"name": "Omen of Dextral Annulment", "tier": TIER.RARE},
    {"name": "Omen of Greater Exaltation", "tier": TIER.RARE},
    {"name": "Omen of Sinistral Exaltation", "tier": TIER.RARE},
    # Trial of Chaos currency
    {"name": "Inscribed Ultimatum", "tier": TIER.LEGENDARY},
    # Trial of the Sekhema currency
    {"name": "Djinn Barya", "tier": TIER.LEGENDARY},
]


rules = [Show([BaseType(item["name"]), TierStyle(item["tier"])]) for item in config]

rules.append(Show([Class("currency"), TierStyle(TIER.RARE)]))
