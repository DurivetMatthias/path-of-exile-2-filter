from app.blocks import *
from app.actions import *
from app.conditions import *
from app.categories import *
from sections.endgame.waystone_tiers import *

boots = [
    {"min_ilvl": 65, "name": "Cinched Boots"},
    {"min_ilvl": 70, "name": "Cavalry Boots"},
    {"min_ilvl": 75, "name": "Dragonscale Boots"},
    {"min_ilvl": 80, "name": "Drakeskin Boots"},
]

gloves = [
    {"min_ilvl": 65, "name": "Stalking Bracers"},
    {"min_ilvl": 70, "name": "Grand Bracers"},
    {"min_ilvl": 75, "name": "Barbed Bracers"},
    {"min_ilvl": 80, "name": "Polished Bracers"},
]

helmets = [
    {"min_ilvl": 65, "name": "Woven Cap"},
    {"min_ilvl": 70, "name": "Desert Cap"},
    {"min_ilvl": 75, "name": "Trapper Hood"},
    {"min_ilvl": 80, "name": "Freebooter Cap"},
]

body_armours = [
    {"min_ilvl": 65, "name": "Swiftstalker Coat"},
    {"min_ilvl": 70, "name": "Slipstrike Vest"},
]


def endgame_evasion_rules():
    rules = []

    for bases in [boots, gloves, body_armours, helmets]:
        for index, base in enumerate(bases):
            base_name = base["name"]
            min_ilvl = base["min_ilvl"]

            if index == 0:
                rarity_rule = Rarity(RARITY.MAGIC, OPERATOR.LTE)
            else:
                rarity_rule = Rarity(RARITY.NORMAL)
            if index < len(bases) - 1:
                max_ilvl = bases[index + 1]["min_ilvl"]
                max_ilvl_rule = ItemLevel(max_ilvl, OPERATOR.LT)
            else:
                max_ilvl_rule = NullCondition()

            rules.append(
                Show(
                    [
                        ItemLevel(min_ilvl, OPERATOR.GTE),
                        max_ilvl_rule,
                        rarity_rule,
                        BaseType(base_name),
                        TierStyle(TIER.EPIC),
                    ]
                ),
            )

    return rules
