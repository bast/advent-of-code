from copy import deepcopy
from collections import deque


def apply_effects(effects, stats):
    for effect in effects:
        if effects[effect]["duration"] > 0:
            effects[effect]["duration"] -= 1
            for k, v in effects[effect]["modifies"].items():
                stats[k] += v


def effect_is_active(spell, effects) -> bool:
    if spell in effects:
        if effects[spell]["duration"] > 0:
            return True
    return False


def get_available_spells(spells, effects, mana) -> list[str]:
    available_spells = set()
    for spell in spells:
        if spells[spell]["cost"] <= mana and not effect_is_active(spell, effects):
            available_spells.add(spell)
    return list(available_spells)


def next_round(spell_name, stats, effects, difficult):
    if difficult:
        stats["player_hit_points"] -= 1
    if stats["player_hit_points"] < 1:
        return stats, effects

    stats["player_armor"] = 0
    apply_effects(effects, stats)
    if stats["boss_hit_points"] < 1:
        return stats, effects

    spell = spells[spell_name]
    stats["player_mana"] -= spell["cost"]
    stats["mana_spent"] += spell["cost"]
    if spell["duration"] == 0:
        for k, v in spell["modifies"].items():
            stats[k] += v
    else:
        effects[spell_name] = deepcopy(spell)

    stats["player_armor"] = 0
    apply_effects(effects, stats)
    if stats["boss_hit_points"] < 1:
        return stats, effects

    damage = stats["boss_damage"] - stats["player_armor"]
    stats["player_hit_points"] -= max(damage, 1)

    return stats, effects


spells = {
    "Magic Missile": {
        "cost": 53,
        "duration": 0,
        "modifies": {"boss_hit_points": -4},
    },
    "Drain": {
        "cost": 73,
        "duration": 0,
        "modifies": {"boss_hit_points": -2, "player_hit_points": 2},
    },
    "Shield": {
        "cost": 113,
        "duration": 6,
        "modifies": {"player_armor": 7},
    },
    "Poison": {
        "cost": 173,
        "duration": 6,
        "modifies": {"boss_hit_points": -3},
    },
    "Recharge": {
        "cost": 229,
        "duration": 5,
        "modifies": {"player_mana": 101},
    },
}

stats_0 = {
    "player_hit_points": 50,
    "player_mana": 500,
    "mana_spent": 0,
    "player_armor": 0,
    "boss_hit_points": 51,
    "boss_damage": 9,
}


def find_min_mana(difficult: bool) -> int:
    min_mana = 100000000

    queue = deque()
    for spell_name in get_available_spells(spells, {}, stats_0["player_mana"]):
        queue.appendleft(([spell_name], deepcopy(stats_0), {}))

    visited = set()
    while len(queue) > 0:
        spell_sequence, _stats, _effects = queue.pop()
        visited.add(tuple(spell_sequence))
        spell_name = spell_sequence[-1]
        stats, effects = next_round(spell_name, _stats, _effects, difficult)
        if stats["player_hit_points"] > 0:
            if stats["boss_hit_points"] < 1:
                min_mana = min(min_mana, stats["mana_spent"])
        game_over = stats["boss_hit_points"] < 1 or stats["player_hit_points"] < 1
        if not game_over:
            if stats["mana_spent"] <= min_mana:
                for spell_name in get_available_spells(
                    spells, effects, stats["player_mana"]
                ):
                    new_spell_sequence = spell_sequence + [spell_name]
                    if tuple(new_spell_sequence) not in visited:
                        queue.appendleft(
                            (new_spell_sequence, deepcopy(stats), deepcopy(effects))
                        )
    return min_mana


print("part 1:", find_min_mana(False))
print("part 2:", find_min_mana(True))
