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

def apply_triplet_to_range(triplet,r):
    (start,end) = r
    (dest,source,l) = triplet
    range_from_triplet = (source,source + l)
    intersection = (max(r[0],range_from_triplet[0]), min(r[-1],range_from_triplet[-1]))
    res = [(intersection[0]+(dest-source),intersection[1]+(dest-source))] if len(range(intersection[0],intersection[1])) != 0 else []

def apply_triplets_to_range(triplets,r):
    res = []
    for triplet in triplets:
        print("r:",r)
        print("triplet:",triplet)
        print(apply_triplet_to_range(triplet,r))
        res += apply_triplet_to_range(triplet,r)
    return res

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
        s_ranges = (list(zip([seeds[i] for i in range(len(seeds)) if i % 2 == 0],[seeds[i] for i in range(len(seeds)) if i % 2 != 0])))
        #range --> [start,end[
        seeds_ranges = [(i[0],i[0]+i[1]) for i in s_ranges]
        print(seeds_ranges)
        print(apply_triplets_to_range(almanac['seed-to-soil'],seeds_ranges[0]))
        #print("Part 2 solution is:", min([get_seed_location_from_almanac(almanac,i) for i in seeds]))
