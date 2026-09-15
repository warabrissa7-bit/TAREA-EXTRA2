class GestionAutos:

    def __init__(self, color_inicial="Blanco", gasolina_inicial=10.0):
        
        self.__colores = []
        self.__gasolinas = []
        
       
        self.__colores.append(color_inicial)
        self.__gasolinas.append(float(gasolina_inicial))
    
    
    def agregarAuto(self, color, gasolina):
        self.__colores.append(color)
        self.__gasolinas.append(float(gasolina))


   
    def incrementarGasolina(self, posicion):
        if 0 <= posicion < len(self.__gasolinas):
            self.__gasolinas[posicion] += 5.0
        else:
            print("Posición de auto no válida.")

    def cambiarColor(self, posicion, nuevo_color):
        if 0 <= posicion < len(self.__colores):
            self.__colores[posicion] = nuevo_color
        else:
            print("Posición de auto no válida.")

    def totalGasolinaDosAutos(self, pos1, pos2):
        if 0 <= pos1 < len(self.__gasolinas) and 0 <= pos2 < len(self.__gasolinas):
            suma = self.__gasolinas[pos1] + self.__gasolinas[pos2]
            print(f"Total de gasolina entre el Auto {pos1} y Auto {pos2}: {suma} litros")
        else:
            print("Una o ambas posiciones de auto no son válidas.")
            
    def mostrar(self):
        for i in range(len(self.__colores)):
            print(f"Auto [{i}] -> Color: {self.__colores[i]}, Gasolina: {self.__gasolinas[i]} litros")


class Main():
    print(" EJECUCIÓN DE PRUEBA: GESTIÓN DE AUTOS ")
    
   
    g = GestionAutos() 
    
    
    g.agregarAuto("Rojo", 45.0)
    
    print("\n--- Estado Inicial de los Autos ---")
    g.mostrar()
    print("" * 50)
    
    
    g.incrementarGasolina(0)
    print("c) Después de incrementar la gasolina (en el Auto 0):")
    g.mostrar()
    print("" * 50)
    
    
    g.cambiarColor(0, "Azul Metálico")
    print("d) Después de cambiar el color (en el Auto 0):")
    g.mostrar()
    print("" * 50)

    
    
    print("e) Ejecución de la suma de gasolina:")
    g.totalGasolinaDosAutos(0, 1)