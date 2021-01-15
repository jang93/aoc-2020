import re


def valid_passports():
    count = 0
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    valid_fields = 0

    for line in lines:
        if line == '\n':
            if valid_fields == 7:
                count += 1
            valid_fields = 0
        else:
            fields = line.split(' ')
            for field in fields:
                key, _ = field.split(':')
                if key != 'cid':
                    valid_fields += 1

    return count

def valid_passports_2():
    count = 0
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    valid_fields = 0

    for line in lines:
        if line == '\n':
            if valid_fields == 7:
                count += 1
            valid_fields = 0
        else:
            fields = line.split(' ')
            for field in fields:
                key, val = field.strip().split(':')
                if key == 'byr':
                    if len(val) == 4 and 1920 <= int(val) <= 2002:
                        valid_fields += 1
                elif key == 'iyr':
                    if len(val) == 4 and 2010 <= int(val) <= 2020:
                        valid_fields += 1
                elif key == 'eyr':
                    if len(val) == 4 and 2020 <= int(val) <= 2030:
                        valid_fields += 1
                elif key == 'hgt':
                    match = re.match(r'\d+cm|\d+in', val)
                    if match:
                        if match.group()[-2:] == 'cm':
                            number = match.group()[:-2]
                            if 150 <= int(number) <= 193:
                                valid_fields += 1
                        else:
                            number = match.group()[:-2]
                            if 59 <= int(number) <= 76:
                                valid_fields += 1
                elif key == 'hcl':
                    if re.match(r'#[0-9a-f]{6}$', val):
                        valid_fields += 1
                elif key == 'ecl':
                    if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        valid_fields += 1
                elif key == 'pid':
                    if re.match(r'\d{9}$', val):
                        valid_fields += 1

    return count

if __name__ == '__main__':
    # print(valid_passports())
    print(valid_passports_2())