from argparse import ArgumentParser 
from functools import reduce

def get_range(ins:str) -> range:
    limits = ins.split("-")
    return range(int(limits[0]), int(limits[1]) + 1)

def is_id_invalid(id:int) -> bool:
    id_str = str(id)
    len_id = len(id_str) 
    if len_id % 2 != 0:
        return False
    midpoint = (len_id // 2)
    return (id_str[0:midpoint] == id_str[midpoint:])

parser = ArgumentParser("puzle2", description="Solución al AoC25 día dos")
parser.add_argument("path", type=str, help="Ruta al input")

args = parser.parse_args()

rangos = None
with open(args.path, "r") as file:
    rangos = [r for r in file.readline().strip().split(",")]

total = 0

for r in rangos:
    total += sum(filter(is_id_invalid, get_range(r)))

print(total)