class Record:
    def __init__(self, min, max, pattern, password):
        self.par1: int = min
        self.par2: int = max
        self.pattern: str = pattern
        self.password: str = password


def read_input_data():
    records = []
    with open('input') as f:
        content = f.readlines()

    for line in content:
        line.strip()
        words = line.split(" ")
        min_max = words[0].split("-")
        records.append(Record(int(min_max[0]), int(min_max[1]), words[1][:-1], words[2]))
    return records


def part1():
    data = read_input_data()
    result = 0
    for d in data:
        if d.par1 <= d.password.count(d.pattern) <= d.par2:
            result += 1
    print(result)


def part2():
    data = read_input_data()
    result = 0
    for d in data:
        if (d.password[d.par1-1] == d.pattern) != (d.password[d.par2 - 1] == d.pattern):
            result += 1
    print(result)


part2()
