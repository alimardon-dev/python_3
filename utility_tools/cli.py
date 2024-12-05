import argparse
from parsing import add, sub

parser = argparse.ArgumentParser(description="venvienvr")

parser.add_argument("x", type=int, help="fdfd")
parser.add_argument("y", type=int,help="fdfd")
parser.add_argument("-o","--t_ops",type=str, help="fdfd")

args = parser.parse_args()

if args.t_ops == "add":
    print(f"the addition: {add(args.x, args.y)}", )
else:
    print(f"the addition: {sub(args.x, args.y)}", )