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
                SetTextColor(rgb),
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
                SetTextColor(rgb),
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
                SetTextColor(rgb),
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
                SetTextColor(rgb),
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
                SetTextColor(rgb),
                SetBorderColor(rgb),
                SetBackgroundColor(rgb),
                SetFontSize(FONT_SIZE.LARGE),
                MinimapIcon(SIZE.SMALL, color, SHAPE.SQUARE),
                PlayAlertSound(BASIC_SOUND.INVERTED_RIPPLE, VOLUME.MEDIUM),
            ]
        )


rules = [
    # Quest items
    Show([Class("Quest Items"), TierStyle(TIER.COMMON)]),
    # Custom Styles
    Show([MultiBaseType(list(OMEN)), RitualStyle()]),
    Show([MultiBaseType(list(ABYSS)), AbyssStyle()]),
    Show([MultiBaseType(list(CATALYST)), BreachStyle()]),
    Show([MultiBaseType(list(EMOTION)), DeliriumStyle()]),
    Show([MultiBaseType(list(EXPEDITION)), ExpeditionStyle()]),
    # Essence
    Show([MultiBaseType(list(ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(LESSER_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(GREATER_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(PERFECT_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(CORRUPT_ESSENCE)), TierStyle(TIER.LEGENDARY)]),
    # Other
    Show([MultiBaseType(list(RELIC)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(TABLET)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(SEKHEMA_KEY)), TierStyle(TIER.COMMON)]),
    Show([MultiBaseType(list(INVITATION)), TierStyle(TIER.LEGENDARY)]),
    Show([MultiBaseType(list(RELIQUARY_KEY)), TierStyle(TIER.LEGENDARY)]),
]
