class Persona():
    n_personas = 0


    def __init__(self, nombre, edad, fecha_nacimiento="1/1/2000"):
        self._nombre = nombre
        self._edad = edad
        self.__fecha_nacimiento = fecha_nacimiento
        Persona.n_personas += 1

    @staticmethod
    def saludo_universal():
        print("Hola a todos")

    @classmethod
    def get_n_personas(cls):
        return cls.n_personas

    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    def __str__(self):
        return f"Persona(nombre={self._nombre}, edad={self._edad}, fecha_nacimiento={self.__fecha_nacimiento})"
    
    def __eq__(self, persona):
        return self._nombre == persona.get_nombre() and self._edad == persona.get_edad() and self.__fecha_nacimiento == persona.get_fecha_nacimiento
    
    def saludar(self, persona):
        print(f"Saludos de parte de {self.get_nombre()} para {persona.get_nombre()}")

class Trabajador(Persona):

    def __init__(self, nombre, edad, fecha_nacimiento="1/1/2000", trabajo="Fontanero"):
        super().__init__(nombre, edad, fecha_nacimiento)
        self._trabajo = trabajo

    def get_trabajo(self):
        return self._trabajo
    
    def saludar(self, persona):
        super().saludar(persona)
        print("Que majos son los trabajadores")

if __name__ == "__main__":
    p1 = Persona("Paco", 20, "3/4/2005")
    p2 = Persona("María", 25)
    t1 = Trabajador("Fernando", "30", "6/6/1995", "Electricista")


    print(f"{p1.get_nombre()}: {p1.get_edad()} años")
    p2.saludar(p1)
    print(p2)
    Persona.saludo_universal()

    if p1 == p2:
        print("son la misma persona")
    else:
        print("No son la misma persona")

    print(f"Número de personas: {Persona.get_n_personas()}")

    t1.saludar(p2)