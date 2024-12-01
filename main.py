from app import filter
from sections import currency

rules = [*currency.rules]

filter.generate(rules=rules, filter_name="main")
