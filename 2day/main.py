filename = __file__[0:-7] + "data.txt"

#Main loop
with open(filename, "r") as f:
    data = f.read()
    measurements = data.splitlines()

def part1(measurements):
    forward = list(map(int, [el[-1] for el in measurements if "forward" in el]))
    down = list(map(int, [el[-1] for el in measurements if "down" in el]))
    up = list(map(int, [el[-1] for el in measurements if "up" in el]))

    hori = sum(forward)
    depth = sum(down) - sum(up)
    return hori * depth

print("First question is : ", part1(measurements))

def part2(measurements):
    hori = 0
    aim = 0
    depth = 0
    for el in measurements:
        x = int(el[-1])
        if "forward" in el:
            hori += x
            depth += aim * x
        if "up" in el:
            aim -= x
        if "down" in el:
            aim += x
    return hori * depth

print("Second question is : ", part2(measurements))