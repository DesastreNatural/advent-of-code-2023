def calculate_manhattan_distance_between(a,b):
    (label_a,(ax,ay)) = a
    (label_b,(bx,by)) = b
    return(abs(ax - bx) + abs(ay - by))

def label_galaxies(universe):
    galaxy_counter = 1
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == '#':
                universe[i][j] = str(galaxy_counter)
                galaxy_counter += 1
    return universe

def get_galaxies_coordinates_from(universe):
    coordinates = []
    galaxy_counter = 1
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == '#':
                coordinates.append((galaxy_counter,(i,j)))
                galaxy_counter += 1
    return coordinates

def rotate_universe(universe):
    return [list(i) for i in zip(*universe)]

def single_directed_scan_anomalies_correction(universe):
    new_universe = []
    for i in range(len(universe)):
        if all([j == "." for j in universe[i]]):
            new_universe.append((["."] * len(universe[0])))
        new_universe.append(universe[i])
    return new_universe

def correct_gravity_anomalies(universe):
    return rotate_universe(single_directed_scan_anomalies_correction(rotate_universe(single_directed_scan_anomalies_correction(universe))))

# def recalculate_gravity_anomalies_directly_on(coord,universe):
#     ncoord = [i for i in coord]
#     for i in range(len(universe)):
#         if all([j == "." for j in universe[i]]):
#             print(i)
#             for g in range(len(coord)):
#                 (label,(x,y)) = coord[g]
#                 if x > i:
#                     print(coord[g], "->", (label,(x+1,y)))
#                     ncoord[g] = (label,(x+1,y))
#     rotated_universe = rotate_universe(universe)
#     for i in range(len(rotated_universe)): 
#         if all([j == "." for j in rotated_universe[i]]):
#             print(i)
#             for g in range(len(coord)):
#                 (label,(x,y)) = coord[g]
#                 if y > i:
#                     print(coord[g], "->", (label,(x,y+1)))
#                     ncoord[g] = (label,(x,y+1))
#     return ncoord

def recalculate_gravity_anomalies_directly_on(coord,universe,CORRECTION=999999):
    h_anomaly = []
    for i in range(len(universe)):
        if all([j == "." for j in universe[i]]):
            h_anomaly.append(i)
    v_anomaly = []
    rotated_universe = rotate_universe(universe)
    for i in range(len(rotated_universe)): 
        if all([j == "." for j in rotated_universe[i]]):
            v_anomaly.append(i)
    for g in range(len(coord)):
        (label,(x,y)) = coord[g]
        h_correction = [x > i for i in h_anomaly].count(True) * CORRECTION
        v_correction = [y > i for i in v_anomaly].count(True) * CORRECTION
        coord[g] = (label,(x+h_correction,y+v_correction))
    return coord

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(__file__),"input")
    with open(path,"r") as inp:
        universe = [list(i.replace("\n","")) for i in inp.readlines()]
        universe_image = correct_gravity_anomalies(universe)
        coord = get_galaxies_coordinates_from(universe_image)
        labeled_universe = label_galaxies(universe_image)
        distances = []
        for i in range(len(coord)):
            for j in range(i+1,len(coord)):
                distances.append(calculate_manhattan_distance_between(coord[i],coord[j]))
        print("Part 1 solution is:", sum(distances))
        ncoord = get_galaxies_coordinates_from(universe)
        ncoord = recalculate_gravity_anomalies_directly_on(ncoord,universe)
        ndistances = []
        for i in range(len(ncoord)):
            for j in range(i+1,len(ncoord)):
                ndistances.append(calculate_manhattan_distance_between(ncoord[i],ncoord[j]))
        print("Part 2 solution is:", sum(ndistances))




