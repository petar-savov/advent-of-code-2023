with open("input-5.txt") as file_handle:
    seeds, *maps = file_handle.read().split("\n", 1)


def lookup(inp: int, map_group: list[list[int]]):
    for dest_start, source_start, length in map_group:
        if inp >= source_start and inp < source_start + length:
            return dest_start + inp - source_start

    return inp


seeds = [int(x) for x in seeds.split(": ")[1].split(" ")]

# keep for part 2
seed_ranges = [(x, y) for x, y in zip(seeds[::2], seeds[1::2])]

maps = [
    [[int(k) for k in x.split()] for x in m.split(":")[1].strip().split("\n")] for m in maps[0].strip().split("\n\n")
]

for map_group in maps:
    seeds = [lookup(x, map_group) for x in seeds]

print(min(seeds))


def lookup_range(seed_ranges, maps):
    for start, length in seed_ranges:
        while length > 0:
            for destination, source, distance in maps:
                delta = start - source
                if delta in range(distance):
                    distance = min(distance - delta, length)
                    yield (destination + delta, distance)
                    start += distance
                    length -= distance
                    break
            else:
                yield start, length
                break


for map_group in maps:
    seed_ranges = list(lookup_range(seed_ranges, map_group))

print(min([d for d, l in seed_ranges]))
