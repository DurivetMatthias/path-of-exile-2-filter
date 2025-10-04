from app import filter
from sections import (
    gem,
    gear,
    jewel,
    flask,
    other,
    unique,
    vendor,
    jewelry,
    special,
    currency,
    waystone,
)

rules = [
    *gem.rules,
    *gear.rules,
    *flask.rules,
    *jewel.rules,
    *other.rules,
    *unique.rules,
    *vendor.rules,
    *jewelry.rules,
    *special.rules,
    *currency.rules,
    *waystone.rules,
]

filter.generate(rules=rules)
