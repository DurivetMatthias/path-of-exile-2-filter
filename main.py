from app import filter
from sections import (
    currency,
    flask,
    gear,
    gem,
    jewel,
    other,
    socketable,
    special,
    tiered,
    trial,
    unique,
    vendor,
    waystone,
    jewelry,
)

rules = [
    *gear.rules,
    *currency.rules,
    *flask.rules,
    *gem.rules,
    *special.rules,
    *jewel.rules,
    *jewelry.rules,
    *other.rules,
    *socketable.rules,
    *tiered.rules,
    *trial.rules,
    *unique.rules,
    *vendor.rules,
    *waystone.rules,
]

filter.generate(rules=rules)
