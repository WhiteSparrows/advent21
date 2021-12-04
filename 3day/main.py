from pprint import pprint
from copy import deepcopy


filename = __file__[0:-7] + "data.txt"

with open(filename, "r") as f:
    data = f.read()
    measurements = data.splitlines()

def find_most_common(measurements, index):
    n = len(measurements)
    count = sum([int(row[index]) for row in measurements])
    return int((count >= n/2))


def find_least_common(measurements, index):
    n = len(measurements)
    count = sum([int(row[index]) for row in measurements])
    return int((count < n/2))

def part1(measurements):
    length = len(measurements[0])
    n = len(measurements)
    gamma = ""
    eps = ""
    for i in range(length):
        x = find_most_common(measurements, i)     
        gamma += str(x) 
        eps += str(1 - x)
    return int(eps,2) * int(gamma, 2)

print(f"solution for part a is {part1(measurements)}")

def filter(matrix, filter_function=find_most_common):
    pos = 0
    while(len(matrix) > 1):
        nb_lines = len(matrix)
        target = filter_function(matrix, pos)
        matrix = [row for row in matrix if row[pos] == str(target)]
        pos += 1
    return matrix[0] 


def part2(measurements):
    matrix = deepcopy(measurements)
    oxy = filter(matrix, find_most_common)
    co2 = filter(matrix, find_least_common)
    return int(oxy, 2) * int(co2, 2)


print(f"result for part b is {part2(measurements)}")    