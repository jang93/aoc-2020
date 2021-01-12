
def get_2_entries_that_sum_to_2020():
    subtracted_values = {}
    with open('input.txt', 'r') as input_file:
        line = input_file.readline()
        while line:
            number = int(line)
            if number in subtracted_values:
                return number * subtracted_values[number]
            subtracted_values[2020 - number] = number
            line = input_file.readline()


def get_3_entries_that_sum_to_2020():
    subtracted_one = {}
    subtracted_two = {}
    with open('input.txt', 'r') as input_file:
        line = input_file.readline()
        while line:
            number = int(line)
            if number in subtracted_two:
                return number * subtracted_two[number][0] * subtracted_two[number][1]
            for key, value in subtracted_one.items():
                subtracted_two[key - number] = (value, number)
            subtracted_one[2020-number] = number
            line = input_file.readline()

if __name__ == "__main__":
    # print(get_2_entries_that_sum_to_2020())
    print(get_3_entries_that_sum_to_2020())



