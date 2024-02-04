import argparse
from itertools import repeat

from lib.convertor import mapping, convert2xy, convert2address


parser = argparse.ArgumentParser()
parser.add_argument("places", nargs="*")
args = parser.parse_args()

places = args.places

for i, place in enumerate(places):
    if place in mapping:
        place = mapping[place]
    places[i] = convert2xy(place)


def map(places):
    result = ""
    cur_letter = "A"
    for i in range(1, 17):
        row_points = []
        for k in range(1, 17):
            for place in places:
                x = place[0]
                y = place[1]
                if y == i and x == k:
                    row_points.append(cur_letter)
                    cur_letter = chr(ord(cur_letter) + 1)
                    break
            else:
                row_points.append("+")
        result += "——".join(row_points) + "\n"
        if i < 16:
            result += "  ".join(list(repeat("|", 16))) + "\n"

    return result


print(map(places))
