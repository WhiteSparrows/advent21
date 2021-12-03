filename = __file__[0:-7] + "data.txt"

#Main loop
with open(filename, "r") as f:
    data = f.read()
    measurements = data.splitlines()

length = len(measurements[0])
measurements = list(map(int, measurements))
n = len(measurements)
a = ""
for b in length:

print(length)
print(n)