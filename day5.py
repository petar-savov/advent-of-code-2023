with open("input-5.txt") as file_handle:
    seeds, *maps = file_handle.read().split("\n", 1)


def lookup(inp: int, map_group: list[list[int]]):
    for dest_start, source_start, length in map_group:
        if inp >= source_start and inp < source_start + length:
            return dest_start + inp - source_start

    return inp


seeds = [int(x) for x in seeds.split(": ")[1].split(" ")]


maps = [
    [[int(k) for k in x.split()] for x in m.split(":")[1].strip().split("\n")]
    for m in maps[0].strip().split("\n\n")
]

for map_group in maps:
    seeds = [lookup(x, map_group) for x in seeds]

print(min(seeds))
