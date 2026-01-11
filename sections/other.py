from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *


class AbyssStyle(Condition):
    def __str__(self):
        rgb = RGB.GREEN
        color = COLOR.GREEN
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.RAINDROP),
                PlayAlertSound(BASIC_SOUND.ELECTRICITY, VOLUME.MEDIUM),
            ]
        )


class ExpeditionStyle(Condition):
    def __str__(self):
        rgb = RGB.BLUE
        color = COLOR.BLUE
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.PENTAGON),
                PlayAlertSound(BASIC_SOUND.METRONOME, VOLUME.MEDIUM),
            ]
        )


class RitualStyle(Condition):
    def __str__(self):
        rgb = RGB.RED
        color = COLOR.RED
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.TRIANGLE),
                PlayAlertSound(BASIC_SOUND.ROTATION, VOLUME.MEDIUM),
            ]
        )


class BreachStyle(Condition):
    def __str__(self):
        rgb = RGB.PURPLE
        color = COLOR.PURPLE
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.HEXAGON),
                PlayAlertSound(BASIC_SOUND.NEEDLE, VOLUME.MEDIUM),
            ]
        )


class DeliriumStyle(Condition):
    def __str__(self):
        rgb = RGB.GREY
        color = COLOR.GREY
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.SQUARE),
                PlayAlertSound(BASIC_SOUND.INVERTED_RIPPLE, VOLUME.MEDIUM),
            ]
        )


class VaalStyle(Condition):
    def __str__(self):
        rgb = RGB.RED
        color = COLOR.RED
        return formatting.format_conditions(
            [
                PlayEffect(color),
                SetTextColor(RGB.WHITE),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.TRIANGLE),
                PlayAlertSound(BASIC_SOUND.PUNCH, VOLUME.MEDIUM),
            ]
        )


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
