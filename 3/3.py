def search_for_adjacent_numbers(x,y,grid):
    X = len(grid)
    Y = len(grid[0])
    if (x-1) >= 0:
        if grid[x-1][y-1]  
if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    grid = []
    with open(path,"r") as inp:
        for i in inp.readlines():
            grid.append(i.replace("\n",""))
        res = []
        x,y = 0,0
        while x != len(grid):
            while y != len(grid[x]):
                if grid[x][y] not in '0123456789\n.':
                    search_for_adjacent_numbers(x,y,grid)
            x+=1
