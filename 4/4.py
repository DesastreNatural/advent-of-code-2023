def calculate_points_for(c):
    res = 0
    for i in c[1][0]:
        if i in c[1][1]:
            if res == 0:
                res = 1
            else:
                res *= 2
    return res

def recalculate_points_for(c):
    res = 0
    for i in c[1][0]:
        if i in c[1][1]:
            res += 1
    return res


if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    with open(path,"r") as inp:
        _s = [line.split(":") for line in [i.replace("\n","") for i in inp.readlines()]]
        _t = [[int(line[0].replace("Card ","")),[[int(elem) for elem in f.split(" ") if elem != ''] for f in line[1].split("|")]] for line in _s]
        print("Part 1 solution is:", sum([calculate_points_for(i) for i in _t]))
        cards_points = {i[0] : recalculate_points_for(i) for i in _t}
        cards_data = {i[0] : 1 for i in _t}
        for card_n in cards_points:
            for w in range(card_n+1,card_n + cards_points[card_n] + 1):
                if w not in cards_data:
                    cards_data[w] = 1
                else:
                    cards_data[w] += cards_data[card_n]
        print("Part 1 solution is:", sum(cards_data.values()))