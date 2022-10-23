import sys
from itertools import permutations

sys.path.append("../..")

from read import read_regex_and_parse


def total_distance(route, city_distances) -> int:
    return sum(map(lambda section: city_distances[section], zip(route, route[1:])))


cities = set()
city_distances = {}
for city_from, city_to, distance in read_regex_and_parse(
    "input.txt", r"(\w+) to (\w+) = (\d+)", (str, str, int)
):
    cities.add(city_from)
    cities.add(city_to)
    city_distances[(city_from, city_to)] = distance
    city_distances[(city_to, city_from)] = distance

distances = map(
    lambda route: total_distance(route, city_distances), permutations(cities)
)

shortest, *_, longest = sorted(distances)

print("part 1:", shortest)
print("part 2:", longest)
