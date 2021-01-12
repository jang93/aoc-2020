import re

def get_valid_passwords():
    count = 0
    with open('.\day-2\input.txt', 'r') as input_file:
        line = input_file.readline()
        while line:
            matches = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
            min_num, max_num, letter, password = matches.groups()
            num_of_occurrences = password.count(letter)
            if int(min_num) <= num_of_occurrences <= int(max_num):
                count += 1
            line = input_file.readline()
    return count

def get_valid_passwords_2():
    count = 0
    with open('.\day-2\input.txt', 'r') as input_file:
        line = input_file.readline()
        while line:
            matches = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
            first_ind, sec_ind, letter, password = matches.groups()
            if (password[int(first_ind)-1] == letter) ^ (password[int(sec_ind)-1] == letter):
                count += 1
            line = input_file.readline()
    return count


if __name__ == '__main__':
    # print(get_valid_passwords())
    print(get_valid_passwords_2())