import regex as re

with open("input-1.txt", "r") as f:
    data = f.read().splitlines()

# Part 1
s = 0
for line in data:
    # find all individual digits
    digits = re.findall(r"\d", line)
    num = int(digits[0] + digits[-1])
    s += num

print(s)

# Part 2
words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

s = 0
for line in data:
    # use lookahead to find overlapping words
    pattern = r"(?=(\d|" + "|".join(words.keys()) + "))"
    nums = re.findall(pattern, line)
    # convert words to digits
    nums = [words.get(num, num) for num in nums]
    num = int(nums[0] + nums[-1])
    s += num

print(s)
