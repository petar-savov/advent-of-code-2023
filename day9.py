with open("input-9.txt") as f:
    data = [[int(x) for x in line.split()] for line in f.read().splitlines()]


def diff(row):
    return [row[i + 1] - row[i] for i in range(len(row) - 1)]


def expand(row):
    rows = [row]
    while True:
        row = diff(row)
        if all([x == 0 for x in row]):
            row.append(0)
            rows.append(row)
            break
        rows.append(row)

    return rows


def find_last(row):
    rows = expand(row)
    for i in range(len(rows) - 2, 0, -1):
        rows[i - 1].append(rows[i][-1] + rows[i - 1][-1])

    return rows[0][-1]


def find_first(row):
    rows = expand(row)
    for i in range(len(rows) - 2, 0, -1):
        rows[i - 1].insert(0, rows[i - 1][0] - rows[i][0])

    return rows[0][0]


print(sum([find_last(row) for row in data]))
print(sum([find_first(row) for row in data]))
