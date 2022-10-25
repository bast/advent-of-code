from dataclasses import dataclass


@dataclass
class Player:
    hit_points: int
    damage: int
    armor: int


def combat(players: list[Player]) -> int:
    attacker, defender = 0, 1
    while True:
        damage = players[attacker].damage - players[defender].armor
        players[defender].hit_points -= max(damage, 1)
        if players[defender].hit_points < 1:
            return attacker
        attacker, defender = defender, attacker


winning_costs = []
losing_costs = []

for (weapon_cost, weapon_damage) in [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]:
    for (armor_cost, armor_armor) in [
        (0, 0),
        (13, 1),
        (31, 2),
        (53, 3),
        (75, 4),
        (102, 5),
    ]:
        for (ring_cost, ring_damage, ring_armor) in [
            (0, 0, 0),
            (25, 1, 0),
            (50, 2, 0),
            (100, 3, 0),
            (20, 0, 1),
            (40, 0, 2),
            (80, 0, 3),
            (75, 3, 0),  # 12
            (125, 4, 0),  # 13
            (45, 1, 1),  # 14
            (65, 1, 2),  # 15
            (105, 1, 3),  # 16
            (150, 5, 0),  # 23
            (70, 2, 1),  # 24
            (90, 2, 2),  # 25
            (130, 2, 3),  # 26
            (120, 3, 1),  # 34
            (140, 3, 2),  # 35
            (180, 3, 3),  # 36
            (60, 0, 3),  # 45
            (100, 0, 4),  # 46
            (120, 0, 5),  # 56
        ]:

            damage = weapon_damage + ring_damage
            armor = armor_armor + ring_armor
            cost = weapon_cost + armor_cost + ring_cost
            players = [
                Player(hit_points=100, damage=damage, armor=armor),
                Player(hit_points=109, damage=8, armor=2),
            ]
            winning_player = combat(players)
            if winning_player == 0:
                winning_costs.append(cost)
            else:
                losing_costs.append(cost)


print("part 1:", min(winning_costs))
print("part 2:", max(losing_costs))
