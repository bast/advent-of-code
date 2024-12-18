from collections import defaultdict
from dataclasses import dataclass
import sys


@dataclass
class FileSystem:
    file_records: dict
    empty_blocks: defaultdict
    first_empty: dict

    def __init__(self, text, part):
        self.file_records = {}
        self.empty_blocks = defaultdict(set)
        self.first_empty = {}

        position = 0
        index = 0
        content = 0
        for i, length in enumerate(map(int, text)):
            if i % 2 == 0:
                match part:
                    case 1:
                        for j in range(length):
                            self.file_records[index] = (position + j, 1, content)
                            index += 1
                    case 2:
                        self.file_records[index] = (position, length, content)
                        index += 1
                content += 1
            else:
                self.add_empty(position, length)
            position += length

    def add_empty(self, position, length):
        self.empty_blocks[length].add(position)
        self.first_empty[length] = min(self.empty_blocks[length])

    def remove_empty(self, position, length):
        self.empty_blocks[length].remove(position)
        numbers = self.empty_blocks[length]
        if len(numbers) > 0:
            self.first_empty[length] = min(numbers)
        else:
            del self.first_empty[length]

    def find_empty(self, length):
        i = sys.maxsize
        length_found = 0
        for k, v in self.first_empty.items():
            if k >= length:
                if v < i:
                    i = v
                    length_found = k
        if length_found == 0:
            return None, None
        else:
            return i, length_found

    def defragment(self):
        for k in reversed(sorted(self.file_records.keys())):
            position, length, content = self.file_records[k]
            new_position, length_found = self.find_empty(length)
            if new_position is not None:
                if new_position < position:
                    self.file_records[k] = (new_position, length, content)
                    self.remove_empty(new_position, length_found)
                    # in the general case we might need to create an empty
                    # record at the position where the file used to be
                    # pre-move but we are saved here by moving files in
                    # descending order
                    if length_found > length:
                        self.add_empty(new_position + length, length_found - length)

    def checksum(self) -> int:
        s = 0
        for _, (position, length, content) in self.file_records.items():
            for i in range(position, position + length):
                s += i * content
        return s


for text in ["2333133121414131402", open("input.txt").read().strip()]:
    for part in [1, 2]:
        fs = FileSystem(text, part)
        fs.defragment()
        print("part:", part, "checksum:", fs.checksum())
