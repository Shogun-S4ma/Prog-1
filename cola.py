# --- Implementación de una Cola sin objetos ---

# Cola vacía
cola = []

# --- Funciones básicas ---
def esta_vacia(cola):
    return len(cola) == 0
#Si no hay caractéres, entonces la cola está vacía, dando "True" en la terminal.
def encolar(cola, elemento):  # Enqueue
    cola.append(elemento)
    print(f"Se encoló: {elemento}")
#Se añade un elemento con append, mostrando que se encoló con print
def desencolar(cola):  # Dequeue
    if not esta_vacia(cola):
        elemento = cola.pop(0)
        print(f"Se desencoló: {elemento}")
        return elemento
    else:
        print("La cola está vacía. No se puede desencolar.")
#Se desencola ún elemento, si no hay ninguno, salta el "else"
def ver_frente(cola):  # Front
    if not esta_vacia(cola):
        print(f"Elemento al frente: {cola[0]}")
        return cola[0]
    else:
        print("La cola está vacía.")
#Muestra el elemento que está en la posición 0, o el primer elemento en la cola, el primero que llegó
def mostrar_cola(cola):
    print("Estado actual de la cola:", cola)
#Muestra todos los elementos que hay en la cola

# --- Uso paso a paso ---
print("¿La cola está vacía?", esta_vacia(cola)) #Nuevamente, muestra que la cola, actualmente está vacía con "True"

encolar(cola, "Revelations: Persona")
encolar(cola, "Persona 2: Innocent sin")
encolar(cola, "Persona 3 FES")
#Añade los 3 elementos anteriores a la cola
mostrar_cola(cola) #Muestra los elementos actuales en la cola
ver_frente(cola) #Muestra el primer elemento añadido

desencolar(cola) #Quita el primer elemento de la cola, el que está en la posición 0
mostrar_cola(cola) #Muestra la cola con los cambios hechos

desencolar(cola) #Quita el elemento 2 y lo notifica en la terminal
desencolar(cola) #Quita el elemento 3 y lo muestra
desencolar(cola)  # Intento extra, No quita nada, por lo que muestra que no se puede desencolar gracias a "Else"

print("¿La cola está vacía?", esta_vacia(cola)) #Muestra si está vacía, en este caso lo está, mostrando "True"
#Prueba
encolar(cola, "Persona 4")
encolar(cola, "Persona 5")
mostrar_cola(cola)
print("La cola sigue vacía?", esta_vacia(cola))
#Como añadí 2 elementos a la cola, entonces salta "False"
ver_frente(cola)