import re


def read_input_data():
    with open('input') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def get_passports_data(content):
    passports = [{}]
    passport_counter = 0
    for line in content:
        if line == '':
            passports.append({})
            passport_counter += 1
            continue
        fields = line.split(' ')
        for field in fields:
            x, y = field.split(':')
            passports[passport_counter][x] = y
    return passports


def get_number_of_valid_passports(passports, required_fields, optional_fields, additional_params=[]):
    invalid_passports = 0
    checked_fields = set(required_fields) - set(optional_fields)
    for passport in passports:
        for checked_field in checked_fields:
            if checked_field in passport:
                if checked_field in additional_params:
                    search_res = re.search(additional_params[checked_field], passport[checked_field])
                    if search_res is None:
                        invalid_passports += 1
                        break
                continue
            else:
                invalid_passports += 1
                break
    return len(passports) - invalid_passports


additional_params_to_check = {
    'byr': '(^19[2-9][0-9]$)|(^200[0-2]$)',
    'iyr': '(^201[0-9]$)|(^2020$)',
    'eyr': '(^202[0-9]$)|(^2030$)',
    'hgt': '(^1(([5-8][0-9])|(9[0-3]))cm$)|(^((59)|(6[0-9])|7[0-6])in$)',
    'hcl': '^#(\d|[a-f]){6}$',
    'ecl': '(^amb$)|(^blu$)|(^brn$)|(^gry$)|(^grn$)|(^hzl$)|(^oth$)',
    'pid': '^\d{9}$'
}

content = read_input_data()
passports = get_passports_data(content)
print(get_number_of_valid_passports(passports, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'], ['cid'], additional_params_to_check))

