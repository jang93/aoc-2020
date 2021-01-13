

def trees_encountered(right, down):
    count = 0
    with open('input.txt', 'r') as input_file:
        line = input_file.readline()
        for _ in range(down):
            line = input_file.readline()
        position = right
        while line:
            if line[position % (len(line) - 1)] == '#':
                count += 1
            for _ in range(down):
                line = input_file.readline()
            position += right
    return count

def trees_encountered_2():
    return trees_encountered(1,1) * trees_encountered(3,1) * trees_encountered(5,1) * trees_encountered(7,1) * trees_encountered(1,2)






if __name__ == '__main__':
    # print(trees_encountered(3,1))
    print(trees_encountered_2())