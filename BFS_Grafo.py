#Luis Olalla
#Inteligencia Artificial
# 6to semestre
# Codigo Busqueda por anchura
#Importamos coleccion queue que maneja FIFO, primero en entrar y primero en salir
from queue import Queue
#Clase grafo en donde vamos a definir los objetos y constructor
class Grafo:
    #Constructor del grafo
    def __init__(self, numero_nodos, dirigido=True):
        """
        El método init nos ayuda a inicializar los atributos de nuestro objeto,
        utilizamos self para representar a la instancia de la clase Grafo,
        tenemos los parámetros numero nodos y la dirección que es dirigida.
        """    
         #Asignamos que el numero de nodos de la matriz  es igual al numero de nodos del grafo    
        self.matrizA_numero_nodos = numero_nodos
        #Creamos el rango de los nodos de la matriz 
        self.matrizA_nodos = range(self.matrizA_numero_nodos)
       #Asignamos la dirección de nuestro grafo para saber si es dirigido o no
        self.matrizA_dirigido = dirigido
        #Implementamos un diccionario de datos para la lista de adyacencia y almacenar los nodos
        self.matrizA_lista_adyacencia = {nodo: set() for nodo in self.matrizA_nodos}        