import re


mapping = dict()

with open("mistopis.txt") as f:
    rows = f.read().split("\n")

for r in rows:
    coords, name = r.split()
    mapping[name] = coords


def convert2xy(address):
    m = re.match("([a-z])(\d+)", address)
    x = int(m.group(2))
    y = ord(m.group(1)) - ord("a") + 1
    return x, y


def convert2address(x, y):
    x = str(x)
    y = chr(ord("a") + y - 1)
    return f"{y}{x}"
