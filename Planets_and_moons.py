# Jesper Lundberg
# TEINF 20
# Planets and Moons

from unicodedata import name


class Planet:

    #Konstruktor
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.moons = ()

    def __str__(self) -> str:
        return f"Name: {self.name}\nSize: {self.size}\nMoons: {self.moons}"

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_moons(self):
        return self.moons

    def add_moon(self, moon):
        self.moons.append(moon)

class Moon:

     def __init__(self, name, size):
        self.name = name
        self.size = size
        self.orbits = None

     def __str__(self) -> str:
        return f"Name: {self.name}\nSize: {self.size}\nOrbits: {self.orbits}"

     def get_name(self):
        return self.name

     def get_size(self):
        return self.size

     def get_orbit(self):
        return self.orbits

     def add_orbit(self, orbit):
        self.orbits = orbit



def main():
    pass



if __name__ == "__main__":
    main()
    tellus = Planet("Tellus", 5.101e8)
    luna = Moon("Luna", 3.8e7)

    mars = Planet("Mars", 1.448e8)
    phobos = Moon("Phobos", 1.5483e3)
    deimos = Moon("Deimos", 4.95e2)

    jupiter = Planet("Jupiter", 6.142e10)
    europa = Moon("Europa", 3.09e7)
    io = Moon("Io", 4.191e7)
    

