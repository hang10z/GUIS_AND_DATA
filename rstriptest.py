def read_depots(file):
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip('\n'))
        return depots


options = read_depots('depots.txt')
print(str(options)[1:-1])
