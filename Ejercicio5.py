from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self):
        self._sonido = None
        self._alimentos = None
        self._hábitat = None
        self._nombreCientífico = None

    @abstractmethod
    def getNombreCientífico(self) -> str:
        pass

    @abstractmethod
    def getSonido(self) -> str:
        pass

    @abstractmethod
    def getAlimentos(self) -> str:
        pass

    @abstractmethod
    def getHábitat(self) -> str:
        pass

class Cánido(Animal, ABC):
    pass


class Perro(Cánido):
    
    def getSonido(self) -> str:
        return "Ladrido"

    def getAlimentos(self) -> str:
        return "Carnívoro"

    def getHábitat(self) -> str:
        return "Doméstico"

    def getNombreCientífico(self) -> str:
        return "Canis lupus familiaris"


class Lobo(Cánido):
    
    def getSonido(self) -> str:
        return "Aullido"

    def getAlimentos(self) -> str:
        return "Carnívoro"

    def getHábitat(self) -> str:
        return "Bosque"

    def getNombreCientífico(self) -> str:
        return "Canis lupus"


class Felino(Animal, ABC):
    pass


class León(Felino):
    
    def getSonido(self) -> str:
        return "Rugido"

    def getAlimentos(self) -> str:
        return "Carnívoro"

    def getHábitat(self) -> str:
        return "Praderas"

    def getNombreCientífico(self) -> str:
        return "Panthera leo"


class Gato(Felino):
    
    def getSonido(self) -> str:
        return "Maullido"

    def getAlimentos(self) -> str:
        return "Ratones"

    def getHábitat(self) -> str:
        return "Doméstico"

    def getNombreCientífico(self) -> str:
        return "Felis silvestris catus"


class Prueba:
    
    @staticmethod
    def main():
        animales = [None] * 4
        
        animales[0] = Gato()
        animales[1] = Perro()
        animales[2] = Lobo()
        animales[3] = León()

        for animal in animales:
            print(animal.getNombreCientífico())
            print("Sonido: " + animal.getSonido())
            print("Alimentos: " + animal.getAlimentos())
            print("Hábitat: " + animal.getHábitat())
            print()


if __name__ == "__main__":
    Prueba.main()
