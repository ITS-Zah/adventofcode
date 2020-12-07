def read_input_data():
    with open('input') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


global memory


def move(data, start_x, start_y, right, down):
    global memory
    if start_y >= len(data):
        return 0
    if start_x >= len(data[0]):
        start_x -= len(data[0])
    add_to_result = 1 if data[start_y][start_x] == '#' else 0
    return add_to_result + move(data, start_x + right, start_y + down, right, down)


def part1():
    global memory
    memory = {}
    data = read_input_data()
    count1 = move(data, 0, 0, 1, 1)
    memory = {}
    count2 = move(data, 0, 0, 3, 1)
    memory = {}
    count3 = move(data, 0, 0, 5, 1)
    memory = {}
    count4 = move(data, 0, 0, 7, 1)
    memory = {}
    count5 = move(data, 0, 0, 1, 2)
    print(count1 * count2 * count3 * count4 * count5)


part1()
