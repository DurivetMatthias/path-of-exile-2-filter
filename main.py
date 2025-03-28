from app import filter
from sections import (
    artifact,
    catalyst,
    chance,
    currency,
    emotion,
    essence,
    flask,
    gem,
    invitation,
    jewel,
    omen,
    quest,
    scroll,
    socketable,
    splinter,
    trial,
    unique,
    vendor,
    waystone,
)

rules = [
    *artifact.rules,
    *catalyst.rules,
    *chance.rules,
    *currency.rules,
    *emotion.rules,
    *essence.rules,
    *flask.rules,
    *gem.rules,
    *invitation.rules,
    *jewel.rules,
    *omen.rules,
    *quest.rules,
    *scroll.rules,
    *socketable.rules,
    *splinter.rules,
    *trial.rules,
    *unique.rules,
    *vendor.rules,
    *waystone.rules,
]

filter.generate(
    rules=rules,
    filter_name="main",
)
