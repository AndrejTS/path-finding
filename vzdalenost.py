import argparse

from lib.convertor import mapping, convert2xy, convert2address
from lib.distance import distance


junction_distance = 20

parser = argparse.ArgumentParser()
parser.add_argument("place_one")
parser.add_argument("place_two")
args = parser.parse_args()

place_one = args.place_one
place_two = args.place_two

if place_one in mapping:
    place_one = mapping[place_one]
if place_two in mapping:
    place_two = mapping[place_two]

place_one = convert2xy(place_one)
place_two = convert2xy(place_two)

print(
    distance(place_one[0], place_one[1], place_two[0], place_two[1]) * junction_distance
)
