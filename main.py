from app import filter
from sections import (
    gem,
    jewel,
    flask,
    other,
    unique,
    currency,
    waystone,
)
from sections.builds import shield_wall

rules = [
    *gem.rules,
    *shield_wall.rules,
    *flask.rules,
    *jewel.rules,
    *other.rules,
    *unique.rules,
    *currency.rules,
    *waystone.rules,
]

filter.generate(rules)
