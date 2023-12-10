def get_missing_elem(line):
    return add_one_elem_to_sequence(
        generate_difference_lines_from(
            line)
        )[0][-1]

def add_one_elem_to_sequence(difflines):
    difflines[-1].append(0)
    for i in range(len(difflines)-1,0,-1):
        difflines[i-1].append((difflines[i][-1] + difflines[i-1][-1]))
    return difflines

def get_missing_elem_but_backwards(line):
    return add_one_elem_to_sequence_but_backwards(
        generate_difference_lines_from(
            line)
        )[0][0]

def add_one_elem_to_sequence_but_backwards(difflines):
    difflines[-1] = [0] + difflines[-1]
    for i in range(len(difflines)-1,0,-1):
        difflines[i-1] = [((difflines[i-1][0] - difflines[i][0]))] + difflines[i-1]
    return difflines

def generate_difference_lines_from(line):
    res = [line]
    while not(all([i == 0 for i in res[-1]])):
        res.append([res[-1][i] - res[-1][i-1] for i in range(1,len(res[-1]))])
    return res

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    with open(path,"r") as inp:
        lines = [[int(j) for j in i.replace("\n","").split(" ")] for i in inp.readlines()]
        print("Part 1 solution is:", sum([get_missing_elem(i) for i in lines]))
        print("Part 2 solution is:", sum([get_missing_elem_but_backwards(i) for i in lines]))