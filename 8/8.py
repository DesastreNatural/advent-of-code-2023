import math

def find_how_many_steps(steps,nodes,START,END):
    res = 0
    s = 0
    actual_node = START
    while actual_node != END:
        if s >= len(steps):
            s = 0
        actual_node = nodes[actual_node][steps[s]]
        res += 1
        s += 1
    return res

def single_converge_steps_amount_for(steps,nodes,actual_node):
    res = 0
    s = 0
    while not(actual_node.endswith("Z")):
        if s >= len(steps):
            s = 0
        actual_node = nodes[actual_node][steps[s]]
        res += 1
        s += 1
    return res

def find_how_many_steps_new_method(steps,nodes):
    actual_nodes = [i for i in nodes.keys() if i.endswith('A')]
    converge_points = [single_converge_steps_amount_for(steps,nodes,i) for i in actual_nodes]
    return math.lcm(*converge_points)

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    with open(path,"r") as inp:
        lines = [i.replace("\n","") for i in inp.readlines()]
        steps = lines[0]
        nodes_lines = [i for i in lines[1:] if i != ""]
        nodes = {}
        _t = [i.replace(" ","").split("=") for i in nodes_lines]
        for i in _t:
            LR = i[1].replace("(","").replace(")","").split(",")
            nodes[i[0]] = {"L": LR[0],"R": LR[1]}
        START = "AAA"
        END = "ZZZ"
        print("Part 1 solution is:", find_how_many_steps(steps,nodes,START,END))
        print("Part 2 solution is:", find_how_many_steps_new_method(steps,nodes))
        
