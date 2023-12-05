def parse_almanac(lines):
    seeds = [int(i) for i in lines[0].split(":")[1].split(" ") if i != ""]
    res = {}
    acc = []
    actual_map = ""
    for line in lines[2:]:
        if line == "":
            res[actual_map] = acc
            acc = []
        elif line[0].isdigit():
            acc.append([int(i) for i in line.split(" ") if i != ""])
        else: #line[0].isalpha():
            actual_map = line.replace(" map:","")
    res[actual_map] = acc
    return (seeds,res)

def triplets_to_function(triplets,in_value):
    for i in triplets:
        if (in_value >= i[1]) and (in_value < (i[1]+i[2])):
            return (in_value - i[1]) + i[0]
    return in_value

# def triplets_to_function_from_range(triplets,in_value_range):
#     for i in triplets:
#         if (in_value >= i[1]) and (in_value < (i[1]+i[2])):
#             return (in_value - i[1]) + i[0]
#     return in_value

def get_seed_location_from_almanac(almanac,seed):
    soil = triplets_to_function(almanac['seed-to-soil'],seed)
    fertilizer = triplets_to_function(almanac['soil-to-fertilizer'],soil)
    water = triplets_to_function(almanac['fertilizer-to-water'],fertilizer)
    light = triplets_to_function(almanac['water-to-light'],water)
    temperature = triplets_to_function(almanac['light-to-temperature'],light)
    humidity = triplets_to_function(almanac['temperature-to-humidity'],temperature)
    return triplets_to_function(almanac['humidity-to-location'],humidity)

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input1")
    with open(path,"r") as inp:
        lines = [i.replace("\n","") for i in inp.readlines()]
        (seeds,almanac) = parse_almanac(lines)
        print("Part 1 solution is:", min([get_seed_location_from_almanac(almanac,i) for i in seeds]))
        seed_ranges = (list(zip([seeds[i] for i in range(len(seeds)) if i % 2 == 0],[seeds[i] for i in range(len(seeds)) if i % 2 != 0])))
        #print("Part 2 solution is:", min([get_seed_location_from_almanac(almanac,i) for i in seeds]))
