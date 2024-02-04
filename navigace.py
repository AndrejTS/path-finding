import argparse

from lib.convertor import mapping, convert2xy, convert2address


parser = argparse.ArgumentParser()
parser.add_argument("start_place")
parser.add_argument("end_place")
args = parser.parse_args()

start_place = args.start_place
end_place = args.end_place

if start_place in mapping:
    start_place = mapping[start_place]
if end_place in mapping:
    end_place = mapping[end_place]

start_place = convert2xy(start_place)
end_place = convert2xy(end_place)


def find_paths(start_place, end_place):
    complete_paths = []
    incomplete_paths = []
    incomplete_paths.append([(start_place[0], start_place[1])])

    while incomplete_paths:
        actual_path = incomplete_paths[0]
        cur_position = actual_path[-1]
        x = cur_position[0]
        y = cur_position[1]
        if x == end_place[0] and y == end_place[1]:
            complete_paths.append(actual_path)
            incomplete_paths.pop(0)
            continue
        directions = get_directions(x, y, end_place[0], end_place[1])
        for d in directions:
            if d == "right":
                incomplete_paths.append(actual_path + [(x + 1, y)])
            if d == "left":
                incomplete_paths.append(actual_path + [(x - 1, y)])
            if d == "down":
                incomplete_paths.append(actual_path + [(x, y + 1)])
            if d == "up":
                incomplete_paths.append(actual_path + [(x, y - 1)])
        incomplete_paths.pop(0)

    return complete_paths


def get_directions(x1, y1, x2, y2):
    directions = []
    if x2 > x1:
        directions.append("right")
    elif x2 < x1:
        directions.append("left")

    if y2 > y1:
        directions.append("down")
    elif y2 < y1:
        directions.append("up")

    return directions


for path in find_paths(start_place, end_place):
    path_output = []
    for place in path:
        path_output.append(convert2address(place[0], place[1]))
    print(" ".join(path_output))
