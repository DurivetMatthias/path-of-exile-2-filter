from app.conditions import Rarity, Sockets, Quality, MultiBaseType
from app.actions import TierStyle
from app.blocks import Show
from app.categories import RARITY, TIER, OPERATOR, WEAPON, GEAR, OFFHAND, FLASK

ARCANIST = [
    WEAPON.WAND,
    WEAPON.STAFF,
    WEAPON.SCEPTRE,
    WEAPON.TRAP,
]
MARTIAL = [
    WEAPON.BOW,
    WEAPON.DAGGER,
    WEAPON.CLAW,
    WEAPON.ONE_HAND_AXE,
    WEAPON.ONE_HAND_MACE,
    WEAPON.ONE_HAND_SWORD,
    WEAPON.TWO_HAND_AXE,
    WEAPON.TWO_HAND_MACE,
    WEAPON.TWO_HAND_SWORD,
    WEAPON.SPEAR,
    WEAPON.CROSSBOW,
    WEAPON.FISHING_ROD,
    WEAPON.FLAIL,
    WEAPON.QUARTERSTAFF,
]
ARMOUR = [
    GEAR.BODY_ARMOUR,
    GEAR.BOOTS,
    GEAR.GLOVES,
    GEAR.HELMET,
    OFFHAND.SHIELD,
    OFFHAND.QUIVER,
    OFFHAND.FOCUS,
]
GLASSBLOWER = [
    GEAR.CHARM,
    FLASK.LIFE,
    FLASK.MANA,
]

rules = [
    Show([Rarity(RARITY.MAGIC), TierStyle(TIER.COMMON)]),
    Show([Rarity(RARITY.RARE), TierStyle(TIER.COMMON)]),
    Show([Rarity(RARITY.UNIQUE), TierStyle(TIER.COMMON)]),
    Show([Sockets("S", operator=OPERATOR.EXACT), TierStyle(TIER.COMMON)]),
    Show([Sockets("SS", operator=OPERATOR.EXACT), TierStyle(TIER.COMMON)]),
    Show([Quality(), MultiBaseType(MARTIAL), TierStyle(TIER.COMMON)]),
    Show([Quality(), MultiBaseType(ARCANIST), TierStyle(TIER.COMMON)]),
    Show([Quality(), MultiBaseType(ARMOUR), TierStyle(TIER.COMMON)]),
    Show([Quality(), MultiBaseType(GLASSBLOWER), TierStyle(TIER.COMMON)]),
]
