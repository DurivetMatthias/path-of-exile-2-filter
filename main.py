from app import filter
from sections import (
    gem,
    gear,
    jewel,
    flask,
    other,
    unique,
    leveling,
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
    *leveling.rules,
    *currency.rules,
    *waystone.rules,
]

filter.generate(rules)
