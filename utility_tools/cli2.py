import click
from parsing import add, sub


@click.command()

@click.option("x", type=int, help="fdfd")
@click.option("x", type=int, help="fdfd")
@click.option("-o",'--t_ops', type=str, help="fdfd")

def hello(x, y, t_ops="add"):
    if t_ops == "add":
        print(f"the addition: {add(x, y)}", )
    else:
        print(f"the addition: {sub(x, y)}", )
hello()