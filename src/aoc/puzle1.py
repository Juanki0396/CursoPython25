from argparse import ArgumentParser

def parse_instruction(ins: str) -> int | None:
    num = None
    if ins[0] == "R":
        num = int(ins[1:])
    elif ins[0] == "L":
        num = -int(ins[1:])
    return num

def move_dial(dial:int, ins:int) -> int:
    """
    Actualiza el valor del dial en función de la instrucción.
    
    :param dial: Description
    :type dial: int
    :param ins: Description
    :type ins: int
    :return: Description
    :rtype: int
    """
    ans = dial + ins
    while ans < 0:
        ans = 100 + ans
    while ans > 99:
        ans -= 100
    return ans


parser = ArgumentParser("puzle1", description="Solución al AoC25 día uno")
parser.add_argument("path", type=str, help="Ruta al input")

args = parser.parse_args()

dial = 50
password = 0

with open(args.path, "r") as file:
    for line in file:
        ins = parse_instruction(line)
        dial = move_dial(dial, ins)
        if dial == 0:
            password += 1

print(f"La contraseña es {password}")