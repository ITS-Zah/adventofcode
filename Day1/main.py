
def read_input_data():
    with open('./input') as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content]
    return content


def clean_data(data):
    result_data = []
    keys_buffer = {}
    for d in data:
        if d in keys_buffer:
            if keys_buffer[d] < 2:
                result_data.append(d)
                keys_buffer[d] += 1
        else:
            keys_buffer[d] = 1
            result_data.append(d)
    return result_data


data = read_input_data()
data = clean_data(data)

already_checked = {}

is_result_founded = False
innerStart = 0

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
