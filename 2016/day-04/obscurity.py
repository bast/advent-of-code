import re
from collections import Counter, defaultdict


def parse_line(line):
    match = re.match(r"([a-z-]+)-(\d+)\[([a-z]+)\]", line)
    return match.group(1), int(match.group(2)), match.group(3)


def test_parse_line():
    assert parse_line("aaaaa-bbb-z-y-x-123[abxyz]") == ("aaaaa-bbb-z-y-x", 123, "abxyz")
    assert parse_line("a-b-c-d-e-f-g-h-987[abcde]") == ("a-b-c-d-e-f-g-h", 987, "abcde")
    assert parse_line("not-a-real-room-404[oarel]") == ("not-a-real-room", 404, "oarel")
    assert parse_line("totally-real-room-200[decoy]") == (
        "totally-real-room",
        200,
        "decoy",
    )


def is_real_room(name, checksum) -> bool:
    name = name.replace("-", "")
    groups = defaultdict(list)
    for k, v in Counter(name).most_common():
        groups[v].append(k)
    s = ""
    for _, v in groups.items():
        s += "".join(sorted(v))
    s = s[:5]
    return s == checksum


def test_is_real_room():
    assert is_real_room("aaaaa-bbb-z-y-x", "abxyz")
    assert is_real_room("a-b-c-d-e-f-g-h", "abcde")
    assert is_real_room("not-a-real-room", "oarel")
    assert not is_real_room("totally-real-room", "decoy")


def shift_text(s, n):
    s_new = ""
    for c in s:
        if c == "-":
            s_new += " "
        else:
            s_new += chr((ord(c) - ord("a") + n) % 26 + ord("a"))
    return s_new


def test_shift_text():
    assert shift_text("qzmt-zixmtkozy-ivhz", 343) == "very encrypted name"


n = 0
for line in open("input.txt", "r").read().splitlines():
    name, sector, checksum = parse_line(line)
    shifted_name = shift_text(name, sector)
    if "north" in shifted_name:
        print("part 2:", shifted_name, sector)
    if is_real_room(name, checksum):
        n += sector

print("part 1:", n)
