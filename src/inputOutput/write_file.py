with open("inputOutput/prueba.txt", "w") as file:
    file.write("Hola Buenos días\n")
    file.write("Que tal\n")
    file.writelines([
        "Me llamo Paco\n",
        "Tengo 18 años\n"
    ])

with open("inputOutput/prueba.txt", "a") as file:
    file.write("Que me estas contando\n")
    