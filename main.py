from app import filter
from sections import (
    currency,
    flask,
    unique,
    socketable,
    vendor,
    waystones,
    quest,
    breach,
    essence,
    tiered,
    gem,
    chance,
    expedition,
    jewel,
    delirium,
)
from sections.gear import invoker, leveling

base_rules = [
    *currency.rules,
    *flask.rules,
    *unique.rules,
    *socketable.rules,
    *vendor.rules,
    *waystones.rules,
    *quest.rules,
    *breach.rules,
    *essence.rules,
    *tiered.rules,
    *gem.rules,
    *chance.rules,
    *expedition.rules,
    *jewel.rules,
    *delirium.rules,
]

filter.generate(
    rules=[
        *invoker.rules,
        *base_rules,
    ],
    filter_name="invoker",
)
filter.generate(
    rules=[
        *leveling.rules,
        *base_rules,
    ],
    filter_name="leveling",
)
