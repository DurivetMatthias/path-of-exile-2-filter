from app.blocks import *
from app.styles import *
from app.actions import *
from app.conditions import *
from app.categories import *


rules = [
    # Quest items
    Show([Class("Quest Items"), TierStyle(TIER.COMMON)]),
    Show([Class("Instance Local Items"), TierStyle(TIER.COMMON)]),
    # Custom Styles
    Show([MultiBaseType(list(OMEN)), RitualStyle()]),
    Show([MultiBaseType(list(ABYSS)), AbyssStyle()]),
    Show([MultiBaseType([*list(CATALYST), "Breach Ring"]), BreachStyle()]),
    Show([BaseType("Liquid", operator=OPERATOR.CONTAINS), DeliriumStyle()]),
    Show([MultiBaseType(list(EXPEDITION)), ExpeditionStyle()]),
    Show([MultiBaseType([EXPEDITION.LOGBOOK]), TierStyle(TIER.LEGENDARY)]),
    # Rise of the Vaal
    Show(
        [
            MultiBaseType(
                [
                    "Core Destabiliser",
                    "Vaal Infuser",
                    "Architect's Orb",
                    "Ancient Infuser",
                    "Orb of Extraction",
                    "Crystallised Corruption",
                    "Vaal Cultivation Orb",
                    "Vaal Siphoner",
                ]
            ),
            VaalStyle(),
        ]
    ),
    # Other
    Show([MultiBaseType(list(TABLET)), TierStyle(TIER.EPIC)]),
    Show([MultiBaseType(list(TRIAL)), TierStyle(TIER.COMMON)]),
    Show([MultiBaseType(list(INVITATION)), TierStyle(TIER.EPIC)]),
    Show([MultiBaseType(list(SEKHEMA_KEY)), TierStyle(TIER.COMMON)]),
    Show([MultiBaseType(list(RELIQUARY_KEY)), TierStyle(TIER.LEGENDARY)]),
    Show(
        [
            Class("Augment"),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            BaseType("Rune of", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            BaseType("Thesis", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            BaseType("Idol", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Soul Core", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Relic", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.COMMON),
        ]
    ),
    # Essence
    Show(
        [
            BaseType("Lesser Essence", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            BaseType("Essence", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            BaseType("Greater Essence", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            BaseType("Perfect Essence", operator=OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiBaseType(list(CORRUPT_ESSENCE)),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
]
