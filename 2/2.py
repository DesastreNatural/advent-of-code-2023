def parse_turn(t):
    data = {"red": 0, "green": 0, "blue": 0} # RGB
    for i in t.split(","):
        _i = i.strip().split(" ")
        data[_i[1]] += int(_i[0])
    return data

def parse_line(l):
    _t = l.split(":")
    g = int(_t[0].replace("Game ",""))
    _turns = _t[1].split(";")
    return (g,[parse_turn(t) for t in _turns])

def is_game_compatible_with(game,reference={"red": 12, "green": 13, "blue": 14}):
    (_,states) = game
    for s in states:
        for color in reference.keys():
            if s[color] > reference[color]:
                return False
    return True

def minimum_cubes_for_game(game):
    (_,states) = game
    minimal = {"red": 0, "green": 0, "blue": 0}
    for s in states:
        for color in minimal.keys():
            if s[color] > minimal[color]:
                minimal[color] = s[color]
    return minimal

def power_of_cubes(cubes):
    r = 1
    for i in cubes:
        r *= cubes[i]
    return r

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    with open(path,"r") as inp:
        lines = [line.replace("\n","") for line in inp.readlines()]
        games = [parse_line(l) for l in lines]
        res1 = 0
        for g in games:
            if is_game_compatible_with(g):
                res1 += g[0]
        print(f"Part #1 solution is {res1}")
        res2 = sum([power_of_cubes(c) for c in [minimum_cubes_for_game(g) for g in games]])
        print(f"Part #2 solution is {res2}")

        
