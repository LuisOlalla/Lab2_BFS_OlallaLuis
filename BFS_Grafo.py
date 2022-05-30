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
    #Funcion que imprime el recorrido transversal    
    def busquedaA_transversal(self,nodo_de_inicio):
        """Imprimimos el valor de la busqueda de anchura del grafo y permite mostrar el recorrido.
        """ 
        #Nodos visitados para no tener bucles
        visitado = set()
        cola = Queue()  
        
        #Agregamos un nodo a la cola y uno en la visita
        cola.put(nodo_de_inicio)  #Agregar cola
        visitado.add(nodo_de_inicio) #Agregar visitado
         # while para poder imprimir cada nodo
        while not cola.empty():
            #sacar un vertice 
            nodo_reciente = cola.get()
            #imprimir el vertice
            print(nodo_reciente,end=" ")
            
            #Adquirir los vertices adyacentes del vertice que fue eliminado.
            for (nodo_siguiente, peso_grafo) in self.matrizA_lista_adyacencia[nodo_reciente]:
                #Marcamos como visitados a los adyacentes y se ponen en la cola
                if nodo_siguiente not in visitado:
                    cola.put(nodo_siguiente) #se pone en el nodo siguiete
                    visitado.add(nodo_siguiente) # se marca como visitado

if __name__ =="__main__":
    
    #Creamos una instancia a la clase del grafo
    g=Grafo(5, dirigido=False) #El grafo no esta dirigido y tendra 5 nodos
    
    #Agregamos bordes al grafo con un peso de 1
    g.agregar_borde_grafo(0,1) #Borde grafo de 0 a 1
    g.agregar_borde_grafo(0,2) #Borde grafo de 0 a 2
    g.agregar_borde_grafo(1,2) #Borde grafo de 1 a 2
    g.agregar_borde_grafo(1,4) #Borde grafo de 1 a 4
    g.agregar_borde_grafo(2,3) #Borde grafo de 2 a 3
     
    #vamos a imprimir la lista de adyacencia en el formulario del nodo
    g.imprime_lista_adyacencia()
   
    print("El siguiente recorrido es el primero en anchura desde el vertice 0")#Avisamos que vamos a recorrer la anchura
    #Imprimimos cada lista de las colas
    g.busquedaA_transversal(0)
    print()