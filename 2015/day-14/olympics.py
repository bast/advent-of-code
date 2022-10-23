import sys
from collections import defaultdict

sys.path.append("../..")

from read import read_regex_and_parse


def distance_traveled(speed, flight_duration, rest_duration):
    distance = 0
    current_flight_duration = 0
    current_rest_duration = 0
    while True:
        if current_flight_duration < flight_duration:
            current_flight_duration += 1
            distance += speed
        else:
            current_rest_duration += 1
            if current_rest_duration == rest_duration:
                current_flight_duration = 0
                current_rest_duration = 0
        yield distance


def leading_reindeer(distances):
    distance_to_names = defaultdict(list)
    for name, distance in distances.items():
        distance_to_names[distance].append(name)
    top_distance = sorted(distance_to_names.keys())[-1]
    return distance_to_names[top_distance]


iterators = {}
for name, speed, flight_duration, rest_duration in read_regex_and_parse(
    "input.txt",
    r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
    (str, int, int, int),
):
    iterators[name] = distance_traveled(speed, flight_duration, rest_duration)

num_seconds = 2503
distances = {}
points = defaultdict(int)
for _ in range(num_seconds):
    for name in iterators:
        distances[name] = next(iterators[name])
    for name in leading_reindeer(distances):
        points[name] += 1

print("distances:")
for name, distance in distances.items():
    print(f"- {name}: {distance}")

print("\npoints:")
for name, score in points.items():
    print(f"- {name}: {score}")
