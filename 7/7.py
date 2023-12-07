from functools import cmp_to_key

def hand_points_for(hand):
    h_set = list(set(hand))
    h_occ = [hand.count(i) for i in h_set]

    if h_occ == [5]:
        return 7
    elif 4 in h_occ:
        return 6
    elif (3 in h_occ) and (2 in h_occ):
        return 5
    elif (3 in h_occ) and (1 in h_occ):
        return 4
    elif h_occ.count(2) == 2:
        return 3
    elif h_occ.count(2) == 1:
        return 2
    else:
        return 1

def get_hand_values(hand):
    return ['23456789TJQKA'.index(i)+1 for i in hand]

def n_hand_points_for(hand):
    jo = hand.count('J')
    hand = hand.replace('J','')
    h_points = hand_points_for(hand)
    if len(hand) == 5:
        return h_points
    elif len(hand) == 0:
        return 7
    else:
        h_set = list(set(hand))
        h_occ = [hand.count(i) for i in h_set]
        h_occ[h_occ.index(max(h_occ))] += jo
    if h_occ == [5]:
        return 7
    elif 4 in h_occ:
        return 6
    elif (3 in h_occ) and (2 in h_occ):
        return 5
    elif (3 in h_occ) and (1 in h_occ):
        return 4
    elif h_occ.count(2) == 2:
        return 3
    elif h_occ.count(2) == 1:
        return 2
    else:
        return 1

def n_get_hand_values(hand):
    return ['J23456789TQKA'.index(i)+1 for i in hand]

def compare_hands(fh1,fh2):
    h1 = fh1[0]
    h2 = fh2[0]
    ph1= hand_points_for(h1)
    ph2 = hand_points_for(h2)
    if ph1 > ph2:
        return -1
    elif ph1 == ph2:
        for ih1,ih2 in zip(get_hand_values(h1),get_hand_values(h2)):
            if ih1 > ih2:
                return -1
            elif ih1 == ih2:
                pass
            else:
                return 1
    elif ph2 > ph1:
        return 1
    else:
        return False

def n_compare_hands(fh1,fh2):
    h1 = fh1[0]
    h2 = fh2[0]
    ph1= n_hand_points_for(h1)
    ph2 = n_hand_points_for(h2)
    if ph1 > ph2:
        return -1
    elif ph1 == ph2:
        for ih1,ih2 in zip(n_get_hand_values(h1),n_get_hand_values(h2)):
            if ih1 > ih2:
                return -1
            elif ih1 == ih2:
                pass
            else:
                return 1
    elif ph2 > ph1:
        return 1
    else:
        return False

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    with open(path,"r") as inp:
        res = []
        hands = [i.replace("\n","").split(" ") for i in inp.readlines()]
        hands.sort(key=cmp_to_key(compare_hands),reverse=True)
        res = 0
        for i in range(len(hands)):
            res += ((i+1) * int(hands[i][1]))
        print("Part 1 solution is:", res)
        hands.sort(key=cmp_to_key(n_compare_hands),reverse=True)
        res = 0
        for i in range(len(hands)):
            res += ((i+1) * int(hands[i][1]))
        print("Part 2 solution is:", res)
