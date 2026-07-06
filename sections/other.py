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
    Show([Class("Omen"), RitualStyle()]),
    Show(
        [
            MultiBaseType(
                [
                    "Gnawed",
                    "Preserved Collarbone",
                    "Preserved Jawbone",
                    "Preserved Rib",
                    "Preserved Cranium",
                    "Ancient Collarbone",
                    "Ancient Jawbone",
                    "Ancient Rib",
                    "Altered Collarbone",
                ],
                OPERATOR.CONTAINS,
            ),
            AbyssStyle(),
        ]
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Catalyst",
                    "Breach Ring",
                    "Wombgift",
                ],
                OPERATOR.CONTAINS,
            ),
            BreachStyle(),
        ]
    ),
    Show([BaseType("Liquid", operator=OPERATOR.CONTAINS), DeliriumStyle()]),
    Show(
        [
            MultiBaseType(
                [
                    "Infuser",
                    "Vaal Siphoner",
                    "Vaal Cultivation Orb",
                    "Core Destabiliser",
                    "Architect's Orb",
                    "Orb of Extraction",
                    "Crystallised Corruption",
                ],
                OPERATOR.CONTAINS,
            ),
            VaalStyle(),
        ]
    ),
    # Other
    Show(
        [
            MultiBaseType(["Tablet"], OPERATOR.CONTAINS),
            TierStyle(TIER.EPIC),
        ]
    ),
    Show(
        [
            MultiBaseType(["Djinn Barya", "Inscribed Ultimatum"], OPERATOR.CONTAINS),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show([MultiBaseType(["Splinter"], OPERATOR.CONTAINS), TierStyle(TIER.EPIC)]),
    Show(
        [
            MultiBaseType(
                [
                    "Gold Key",
                    "Silver Key",
                    "Bronze Key",
                ]
            ),
            TierStyle(TIER.COMMON),
        ]
    ),
    Show(
        [
            MultiBaseType(["Reliquary Key"], OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            Class("Augment"),
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
    # Show(
    #     [
    #         MultiBaseType(
    #             [
    #                 "Breach Splinter",
    #                 "An Audience with the King",
    #                 "Head of the King",
    #                 "Breachlord Sac",
    #             ]
    #         ),
    #         TierStyle(TIER.LEGENDARY),
    #     ],
    # ),
    Show(
        [
            Class("Map Fragments"),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            Class("Pinnacle Keys"),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            MultiBaseType(
                [
                    "Essence of Horror",
                ]
            ),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    # Exceptional items
    Show(
        [
            Quality(21),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass(["Gloves", "Boots", "Helmets"]),
            Sockets(2),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    Show(
        [
            MultiClass(["Body Armours"]),
            Sockets(3),
            TierStyle(TIER.LEGENDARY),
        ]
    ),
    # ===========================
    # Runes of Aldur / Expedition
    # ===========================
    Show(
        [
            Class("Stackable Currency"),
            MultiBaseType(
                [
                    "Expedition Logbook",
                    "Verisium",
                    "Alloy",
                    "Flux",
                    "Ore",
                    "Crest",
                    "Saga",
                ],
                OPERATOR.CONTAINS,
            ),
            ExpeditionStyle(),
        ]
    ),
    Show(
        [
            MultiBaseType(["Expedition Logbook", "Shattered Triskelion"]),
            ExpeditionStyle(),
        ]
    ),
]
