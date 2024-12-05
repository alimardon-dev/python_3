# from utility_tools.date_tools import current_time
# from utility_tools.math_tools import factorial
# from utility_tools.math_tools import is_prime
# from utility_tools.text_tools import word_count
# from utility_tools.text_tools import reverse_string

from utility_tools.math_tools import add
from utility_tools.math_tools import sub
import argparse

parser = argparse.ArgumentParser(description="venvienvr")

parser.add_argument("x", type=int, help="fdfd")
parser.add_argument("y", type=int,help="fdfd")
parser.add_argument("-o","--t_ops",type=str, help="fdfd")

args = parser.parse_args()

if args.t_ops == "add":
    print(f"the addition: {add(args.x, args.y)}", )
else:
    print(f"the addition: {sub(args.x, args.y)}", )


# tasks = []
# describtion =[]

