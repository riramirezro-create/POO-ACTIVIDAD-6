class Profesor:
    
    def _imprimir(self):
        print("Es un Profesor")


class ProfesorTitular(Profesor):
    
    def __init__(self):
        self.años = 0
        
    def _imprimir(self):
        print("Es un Profesor Titular")
        
    def _imprimirAños(self):
        print("Años = " + str(self.años))


def main():

    profesor1 = Profesor()
    profesor1._imprimir()
    
    profesor2 = ProfesorTitular()
    
    profesor2._imprimir()
    
    profesor2._imprimirAños()


if __name__ == "__main__":
    main()
