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

def search_for_gear_symbol(g):
    res = []
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == '*':
                res.append([i,j])
    return res

def rebuild_from_coordinate(x,y,grid):
    #(x,y,run,number)
    nx,ny=x,y
    while grid[nx][ny].isdigit():
        ny-=1
    ny+=1
    run=0
    _t=""
    while ny+run < len(grid[0]):
        if (grid[nx][ny+run].isdigit()):
            _t += grid[nx][ny+run]
            run+=1
        else:
            break
    return (nx,ny,run,_t)

def get_symbol_adjacencies(x,y,grid):
    valid_positions = generate_valid_checkable_positions(x,y,grid)
    with_digits = [i for i in valid_positions if grid[i[0]][i[1]].isdigit()]
    every_adjacent_number_with_possible_duplicates = [rebuild_from_coordinate(i[0],i[1],grid) for i in with_digits]
    return [t for t in (set(tuple(i) for i in every_adjacent_number_with_possible_duplicates))]

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    with open(path,"r") as inp:
        grid = []
        for i in inp.readlines():
            grid.append(i.replace("\n",""))
        m = get_map_of_numbers(grid)
        res = 0
        data = []
        for i in m:
            if is_adjacent_to_symbol(i,grid):
                res+=i[3]
        print("Part 1 solution is:", res)
        gmap = search_for_gear_symbol(grid)
        adjacensies = [get_symbol_adjacencies(gear_symbol[0],gear_symbol[1],grid) for gear_symbol in gmap]
        only_coupled = [d for d in adjacensies if len(d) == 2]
        gear_ratios = [int(d[0][3]) * int(d[1][3]) for d in only_coupled]
        print("Part 2 solution is:", sum(gear_ratios))
