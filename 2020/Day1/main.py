def read_input_data():
    with open('input') as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    return content


def clean_data(data, max_number):
    result_data = []
    keys_buffer = {}
    for d in data:
        if d in keys_buffer:
            if keys_buffer[d] < max_number:
                result_data.append(d)
                keys_buffer[d] += 1
        else:
            keys_buffer[d] = 1
            result_data.append(d)
    return result_data


def part1():
    data = read_input_data()
    data = clean_data(data, 2)

    already_checked = {}

    is_result_founded = False

    for i in range(len(data)):
        if data[i] in already_checked:
            continue
        else:
            already_checked[data[i]] = 1

        for j in range(i + 1, len(data)):
            if (data[i] + data[j]) == 2020:
                is_result_founded = True
                print(data[i] * data[j])
                break
        if is_result_founded:
            break


def part1_recurs():
    data = read_input_data()
    data = clean_data(data, 2)

    print(calculate(data, 0, 0))


def dict_based_solution(data, find, number_of_find):
    if number_of_find == 2:
        inner_memory = {}
        for d in data:
            if find - d in inner_memory:
                inner_memory[find - d].append(d)
            else:
                inner_memory[find - d] = [d]
        for d in data:
            if d in inner_memory:
                value = inner_memory[d]
                if (d != value[0]) or len(value) > 1:
                    return [d, inner_memory[d][0]]
        return None
    memory = {}
    for d in data:
        dc = data.copy()
        dc.remove(d)
        inner_found = dict_based_solution(dc, find - d, number_of_find - 1)
        if inner_found is not None:
            inner_found.append(d)
            memory[find] = inner_found
            break
    if find in memory:
        return memory[find]
    else:
        return None


def calculate(data, first_index, second_index):
    if (data[first_index] + data[second_index]) == 2020:
        return data[first_index] * data[second_index]
    else:
        if second_index < len(data):
            return calculate(data, first_index, second_index + 1)
        else:
            return calculate(data, first_index + 1, 0)


data = read_input_data()
data = clean_data(data, 3)
# part1()
# res = part1_opt(data, 2020)
# print(res[0] * res[1])
res_num = dict_based_solution(data.copy(), 2020, 3)
res = 1
for r in res_num:
    res *= r
print(res)
#
# part2()
# print(part2_opt(data.copy(), 2020))
# res_num = dict_based_solution(data.copy(), 2020, 4)
# res = 1
# for r in res_num:
#     res *= r
#print(res)