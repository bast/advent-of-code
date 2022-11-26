import sys

sys.path.append("../..")

from crt import chinese_remainder


def compute_residues(moduli, positions):
    return [(n - 1 - p - i) % n for i, (n, p) in enumerate(zip(moduli, positions))]


moduli = [5, 13, 17, 3, 19, 7]
positions = [2, 7, 10, 2, 9, 0]

print("part 1:", chinese_remainder(moduli, compute_residues(moduli, positions)))

moduli.append(11)
positions.append(0)

print("part 2:", chinese_remainder(moduli, compute_residues(moduli, positions)))
