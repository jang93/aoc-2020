

def get_highest_seat_id():
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    highest = 0
    smallest = 1000
    for line in lines:
        number = convert_seat_to_seat_id(line.strip())
        if number > highest:
            highest = number
        if number < smallest:
            smallest = number
    return highest, smallest


def get_missing_seat(highest, smallest):
    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()
    seats = [i for i in range(smallest, highest+1)]
    for line in lines:
        number = convert_seat_to_seat_id(line.strip())
        seats.remove(number)
    return seats[0]


def convert_seat_to_seat_id(letters):
    result = 0
    for ind, letter in enumerate(letters[::-1]):
        if letter in ['B', 'R']:
            result += 2**ind
    return result

if __name__ == '__main__':
    print(get_highest_seat_id())
    highest, smallest = get_highest_seat_id()
    print(get_missing_seat(highest, smallest))