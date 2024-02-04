import argparse
from itertools import permutations

from lib.convertor import mapping, convert2xy, convert2address
from lib.distance import distance


parser = argparse.ArgumentParser()
parser.add_argument("start_place")
parser.add_argument("end_place")
parser.add_argument("places", nargs="*")
args = parser.parse_args()


start_place = args.start_place
end_place = args.end_place

if start_place in mapping:
    start_place = mapping[start_place]
if end_place in mapping:
    end_place = mapping[end_place]

start_place = convert2xy(start_place)
end_place = convert2xy(end_place)

places = []
for p in args.places:
    if p in mapping:
        p = mapping[p]
    places.append(convert2xy(p))


def walk(start_place, end_place, places):
    shortest_paths = []
    shortest_path_len = None

    perms = permutations(places)
    for p in perms:
        path = [start_place] + list(p) + [end_place]
        path_len = 0
        for i in range(len(path) - 1):
            x1 = path[i][0]
            y1 = path[i][1]
            x2 = path[i + 1][0]
            y2 = path[i + 1][1]
            path_len += distance(x1, y1, x2, y2)

        if not shortest_paths:
            shortest_paths = [path]
            shortest_path_len = path_len

        if path_len == shortest_path_len:
            if path not in shortest_paths:
                shortest_paths.append(path)
        elif path_len < shortest_path_len:
            shortest_paths = [path]
            shortest_path_len = path_len

    return shortest_paths


for path in walk(start_place, end_place, places):
    path_output = []
    for place in path:
        address = convert2address(place[0], place[1])
        for name, _address in mapping.items():
            if address == _address:
                path_output.append(name)
                break
        else:
            path_output.append(address)
    print(" ".join(path_output))
