class ArticuloCientifico:

    def __init__(self, *args):
        if not hasattr(self, '_ArticuloCientifico__titulo'):
            self.__titulo = ""                 
            self.__autor = ""                   
            self.__palabras_claves = [""] * 3   
            self.__publicacion = ""             
            self.__ano = 0                      
            self.__resumen = ""                 

        
        if len(args) == 2:
            self.__titulo = args[0]
            self.__autor = args[1]
            
        elif len(args) == 5:
            self.__init__(args[0], args[1])     
            self.__palabras_claves = args[2]
            self.__publicacion = args[3]
            self.__ano = args[4]
            
        elif len(args) == 6:
            self.__init__(args[0], args[1], args[2], args[3], args[4]) 
            self.__resumen = args[5]

    def imprimir(self):

        print("Título del artículo = " + self.__titulo)
        print("Autor del artículo = " + self.__autor)
        print("Palabras clave = ")
        
        for i in range(len(self.__palabras_claves)):
            print(self.__palabras_claves[i])
            
        print("Publicación = " + self.__publicacion)
        print("Año = " + str(self.__ano))
        print("Resumen = " + self.__resumen)


if __name__ == "__main__":
    palabras = ["Física", "Espacio", "Tiempo"]
    
    articulo = ArticuloCientifico(
        "La teoría especial de la relatividad", 
        "Albert Einstein", 
        palabras, 
        "Anales de Física", 
        1913, 
        "Las leyes de la física son las mismas en todos los sistemas de referencia inerciales."
    )
    
    articulo.imprimir()
