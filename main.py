from app import filter
from sections import currency, flask, gear, unique, socketable, vendor, waystones, quest

rules = [
    *currency.rules,
    *flask.rules,
    *gear.rules,
    *unique.rules,
    *socketable.rules,
    *vendor.rules,
    *waystones.rules,
    *quest.rules,
]

filter.generate(rules=rules, filter_name="main")
