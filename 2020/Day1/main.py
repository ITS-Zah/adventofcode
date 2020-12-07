
def read_input_data():
    with open('input_test') as f:
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

        for j in range(i+1, len(data)):
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


def part2():
    data = read_input_data()
    data = clean_data(data, 3)

    already_checked = {}

    is_result_founded = False

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if f"{data[i]},{data[j]}" in already_checked:
                continue
            else:
                already_checked[f"{data[i]},{data[j]}"] = 1
                already_checked[f"{data[j]},{data[i]}"] = 1
            for k in range(j + 1, len(data)):
                if (data[i] + data[j] + data[k]) == 2020:
                    is_result_founded = True
                    print(data[i] * data[j] * data[k])
                    break
            if is_result_founded:
                break


def calculate(data, first_index, second_index):
    if (data[first_index] + data[second_index]) == 2020:
        return data[first_index] * data[second_index]
    else:
        if second_index < len(data):
            return calculate(data, first_index, second_index + 1)
        else:
            return calculate(data, first_index + 1, 0)


part1()
part1_recurs()
