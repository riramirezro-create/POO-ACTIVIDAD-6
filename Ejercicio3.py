class Profesor:

    def _imprimir(self):
      
        print("Es un profesor.")


class ProfesorTitular(Profesor):

    def _imprimir(self):
        print("Es un profesor titular.")


class Prueba:
  
    @staticmethod
    def main():

        profesor1: Profesor = ProfesorTitular()
        
        profesor1._imprimir()

if __name__ == "__main__":
    Prueba.main()
