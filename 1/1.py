def f_extr(l):
    res = ""
    for i in l:
        if i in '0123456789':
            res += i
            break
    for j in reversed(l):
        if j in '0123456789':
            res += j
            break
    return int(res)

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0 }

def F_extr(l):
    res = ""
    for i in range(len(l)):
        for n in numbers.keys():
            if n in l[:i]:
                res += str(numbers[n])
                break
        if len(res) == 1:
            break
        if l[i] in '0123456789':
            res += l[i]
            break
        if len(res) == 1:
            break
    for j in reversed(range(len(l))):
        for n in numbers.keys():
            if n in l[j:]:
                res += str(numbers[n])
                break
        if len(res) == 2:
            break
        if l[j] in '0123456789':
            res += l[j]
            break
        if len(res) == 2:
            break
    return int(res[0]+res[-1])

if __name__ == '__main__':
    import os 
    path = os.path.join(os.path.dirname(__file__),"input")
    
    with open(path,"r") as inp:
        lines = inp.readlines()[:]
        print("Part 1 solution is", sum([f_extr(i) for i in lines]))
        print("Part 2 solution is", sum([F_extr(i) for i in lines]))

    
    