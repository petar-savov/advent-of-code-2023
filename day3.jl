file = open("input-3.txt")
lines = readlines(file)
close(file)

# padding with "."
lines = ["." * line * "." for line in lines]
pushfirst!(lines, "."^length(lines[1]))
push!(lines, "."^length(lines[1]))


function is_part(lines, row, segment)
    start, stop = segment[1], segment[end]

    surrounding = [
        lines[row-1][start-1:stop+1],
        lines[row+1][start-1:stop+1],
        [lines[row][start-1]],
        [lines[row][stop+1]]
    ]

    for side in surrounding
        if any(c -> c != '.', side)
            return true
        end
    end

    return false
end

nums = [findall(r"\d+", line) for line in lines]

# Part 1
s = 0
for (i, line) in enumerate(lines)
    for segment in nums[i]
        if is_part(lines, i, segment)
            s += parse(Int, lines[i][segment])
        end
    end
end

println(s)

# Part 2
function gear_ratio(lines, nums, row, col)
    if lines[row][col] != '*'
        return 0
    end
    seen = Dict()
    for r in [row - 1, row, row + 1]
        for c in [col - 1, col, col + 1]
            for segment in nums[r]
                if c in segment
                    if is_part(lines, r, segment)
                        key = (r, segment)
                        seen[key] = parse(Int, lines[r][segment])
                    end
                end
            end
        end
    end

    return length(seen) == 2 ? prod(values(seen)) : 0
end

s = 0
for (i, line) in enumerate(lines)
    for (j, char) in enumerate(line)
        s += gear_ratio(lines, nums, i, j)
    end
end

println(s)
