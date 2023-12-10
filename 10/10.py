def connectable_points(origin,symbol):
    (Ox,Oy) = origin
    if symbol == '|':
        return [origin,symbol,[(Ox+1,Oy),(Ox-1,Oy)]]
    elif symbol == '-':
        return [origin,symbol,[(Ox,Oy+1),(Ox,Oy-1)]]
    elif symbol == 'L':
        return [origin,symbol,[(Ox+1,Oy),(Ox,Oy+1)]]
    elif symbol == 'J':
        return [origin,symbol,[(Ox+1,Oy),(Ox,Oy-1)]]
    elif symbol == '7':
        return [origin,symbol,[(Ox-1,Oy),(Ox,Oy-1)]]
    elif symbol == 'F':
        return [origin,symbol,[(Ox-1,Oy),(Ox,Oy+1)]]
    elif symbol == '.':
        return [origin,symbol,[]]
    elif symbol == 'S':
        return [origin,'E',[]]

def calculate_adjacent_valid_points_from(origin,max_points):
    (x,y) = origin
    (Mx,My) = max_points
    res = []
    for i in (x-1,x,x+1):
        for j in (y-1,y,y+1):
            if i >= 0 and i < Mx:
                if j >= 0 and j < My:
                    if not(i == x and j == y):
                        res.append((i,j))
    return res

def calculate_adjacent_connectable_points_for(origin,max_points,pmap):
    adjacensies = calculate_adjacent_valid_points_from(origin,max_points)
    connectable_adjacensies = [connectable_points(i,pmap[i[0]][i[1]]) for i in adjacensies if origin in connectable_points(i,pmap[i[0]][i[1]])[2]]
    return connectable_adjacensies

def someone_has_finished(l):
    for i in l:
        if i[1] == 'E':
            return True
    return False

def follow(origin,max_points,pmap):
    path = [origin]
    path_counter = 1
    while path_counter!=50:
        print(path)
        _d = calculate_adjacent_connectable_points_for(path[-1],max_points,pmap)[0]
        print(_d)
        [_d[2].remove(i) for i in path if i in _d[2]]
        print(path[-1])
        print(_d)
        next = _d[2][0]
        path.append(_d[0])
        path_counter += 1
        if next == origin:
            break
    return path

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input1")
    with open(path,"r") as inp:
        (Sx,Sy) = (0,0)
        pipes_map = [i.replace("\n","") for i in inp.readlines()]
        (MAXx,MAXy) = (len(pipes_map),len(pipes_map[0]))
        for i in range(len(pipes_map)):
            for j in range(len(pipes_map[i])):
                if pipes_map[i][j] == 'S':
                    (Sx,Sy) = (i,j)
        print(Sx,Sy)
        print(follow((Sx,Sy),(MAXx,MAXy),pipes_map))