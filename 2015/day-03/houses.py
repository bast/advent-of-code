def visited_positions(directions):
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    for c in directions:
        match c:
            case "^":
                y += 1
            case "v":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
        visited.add((x, y))
    return visited


directions = open("input.txt", "r").read()

positions = visited_positions(directions)
print(f"part 1: {len(positions)}")

positions_santa = visited_positions(directions[::2])
positions_robo = visited_positions(directions[1::2])
positions = positions_santa.union(positions_robo)
print(f"part 2: {len(positions)}")
