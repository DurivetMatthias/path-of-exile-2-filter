from app import filter
from sections import (
    armour,
    currency,
    flask,
    gem,
    jewel,
    other,
    socketable,
    tiered,
    trial,
    unique,
    vendor,
    waystone,
    weapon,
    jewelry,
    hide,
)

rules = [
    *armour.rules,
    *currency.rules,
    *flask.rules,
    *gem.rules,
    *hide.rules,
    *jewel.rules,
    *jewelry.rules,
    *other.rules,
    *socketable.rules,
    *tiered.rules,
    *trial.rules,
    *unique.rules,
    *vendor.rules,
    *waystone.rules,
    *weapon.rules,
]

filter.generate(rules=rules)
