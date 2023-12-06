def toy_final_distance_from_holding_time(hold_t,time):
    if hold_t >= time or hold_t == 0:
        return 0
    else:
        return ((time - hold_t) * hold_t)

def get_every_possible_distance(time):
    return [toy_final_distance_from_holding_time(hold_t,time) for hold_t in range(time+1)]

def get_number_of_possibilities_of_record_breaking(time,record_distance):
    return len([i for i in get_every_possible_distance(time) if i > record_distance])

def toy_function_limits(time,record_distance):
    l1 = 0
    while toy_final_distance_from_holding_time(l1,time) < record_distance:
        l1 += 1
    l2 = time 
    while toy_final_distance_from_holding_time(l2,time) < record_distance:
        l2 -= 1
    return (l1,l2)

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    with open(path,"r") as inp:
        lines = [i.replace("\n","").replace("\t","") for i in inp.readlines()]
        time = [int(i) for i in lines[0].replace("Time:","").split(" ")  if i != ""]
        distance = [int(i) for i in lines[1].replace("Distance:","").split(" ")  if i != ""]
        res = 1 
        for i in [get_number_of_possibilities_of_record_breaking(t,d) for (t,d) in zip(time,distance)]:
            res *= i
        print("Part 1 solution is:", res)
        ntime = int("".join([str(i) for i in time]))
        ndistance = int("".join([str(i) for i in distance]))
        ls = toy_function_limits(ntime,ndistance)
        print("Part 2 solution is:", (max(ls)-min(ls))+1)