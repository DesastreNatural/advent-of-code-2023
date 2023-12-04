def get_map_of_numbers(m):
    res = []
    #(x,y,run,number)
    x,y,run = None,None,0
    _t = ""
    for i in range(len(m)):
        for j in range(len(m[i])):
            if run == 0:
                if m[i][j].isdigit():
                    x,y = i,j
                    run += 1
                    _t += m[i][j]
            else:
                if m[i][j].isdigit():
                    run += 1
                    _t += m[i][j]
                else:
                    res.append([x,y,run,int(_t)])
                    x,y,run = None,None,0
                    _t = ""
    if run != 0:
        res.append([x,y,run,int(_t)])
    return res

def is_symbol(x):
    return x not in "0123456789.\n"

def generate_valid_checkable_positions(x,y,grid):
    MIN_X,MIN_Y,MAX_X,MAX_Y = 0,0,len(grid),len(grid[0])
    res = []
    for i in (x-1,x,x+1):
        for j in (y-1,y,y+1):
            if i >= MIN_X and i < MAX_X:
                if j >= MIN_Y and j < MAX_Y:
                    if not(i == x and j == y):
                        res.append((i,j))
    return res

def is_adjacent_to_symbol(coordinate,grid):
    [x,y,run,number] = coordinate
    adjacents = []
    for yv in range(y,y+run):
        adjacents = adjacents + generate_valid_checkable_positions(x,yv,grid)
    return any([is_symbol(grid[d[0]][d[1]]) for d in adjacents])

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    with open(path,"r") as inp:
        grid = []
        out = []
        for i in inp.readlines():
            grid.append(i.replace("\n",""))
            out.append(list(i))
        m = get_map_of_numbers(grid)
        res = 0
        data = []
        for i in m:
            if is_adjacent_to_symbol(i,grid):
                [x,y,run,number] = i
                for yv in range(y,y+run):
                    out[x][yv] = "X"
                res+=i[3]
        print("Part 1 solution is:", res)
