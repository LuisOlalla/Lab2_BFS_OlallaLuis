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
        
        #Realizamos el borde del grafo        
    def agregar_borde_grafo(self,nodo_1,nodo_2, peso_grafo=1):
        """ Definimos los bordes del grafo, aumentamos los nodos y asignamos el peso del grafo. """        
        self.matrizA_lista_adyacencia[nodo_1].add((nodo_2,peso_grafo)) #Aumentamos el segundo nodo en el primer nodo
        #If cuando el nodo no este dirigido
        if not self.matrizA_dirigido:
            #Agregamos el primer nodo al segundo nodo en su lista.
            self.matrizA_lista_adyacencia[nodo_2].add((nodo_1,peso_grafo))    
            
             #Imprimimos la representacion del grafo   
    def imprime_lista_adyacencia(self):
        
        """Imprimimos el grafo en base a la lista de adyacencia
        """  
         # Realizamos un for para recorrer por la lista de adyacencia       
        for llaves in self.matrizA_lista_adyacencia.keys():
            print("nodo",llaves,":",self.matrizA_lista_adyacencia[llaves]) #Imprimimos el nodo