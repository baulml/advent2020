import re

def prep_file(file):
    with open(file) as f:
        rawdata = []
        s = ''
        for d in f.read().splitlines():
            if d == '':
                rawdata.append(s)
                s = ''
            else:
                s += d + ' '
        rawdata.append(s)
    return [dict([tuple(l.split(':')) for l in d.split()]) for d in rawdata]

def validate(passport):
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(k in passport for k in keys)

def validate_key(key, value):
    if key == 'byr':
        return value.isdigit() and 1920 <= int(value) <= 2002
    if key == 'iyr':
        return value.isdigit() and 2010 <= int(value) <= 2020
    if key == 'eyr':
        return value.isdigit() and 2020 <= int(value) <= 2030
    if key == 'hgt':
        n = value[:-2]
        if not n.isdigit():
            return False
        unit = value[-2:]
        if unit == 'cm':
            return 150 <= int(n) <= 193
        if unit == 'in':
            return 59 <= int(n) <= 76
        return False
    if key == 'hcl':
        return value[0] == '#' and re.fullmatch(r'[a-f\d]{6}', value[1:]) is not None
    if key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if key == 'pid':
        return value.isdigit() and len(value) == 9

def validate_keys(passport):
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for k in keys:
        if k not in passport or not validate_key(k, passport[k]):
            return False
    return True

def part_1(input):
    return sum(map(validate, input))

def part_2(input):
    return sum(map(validate_keys, input))

input = prep_file('input.txt')
print(part_1(input))
print(part_2(input))
