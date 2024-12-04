from app import filter
from sections import currency, flask, gear, unique

rules = [
    *currency.rules,
    *flask.rules,
    *gear.rules,
    *unique.rules,
]

filter.generate(rules=rules, filter_name="main")
