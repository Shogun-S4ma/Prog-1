# --- Implementación de una Pila sin objetos ---

# Pila vacía
pila = []

# --- Funciones básicas ---
def esta_vacia(pila):
    return len(pila) == 0 #Si la fila no tiene caracteres, está vacía, por lo que devuelve un True como resultado

def apilar(pila, elemento):  # Push
    pila.append(elemento) 
    print(f"Se apiló: {elemento}")
#Se añade un elemento con ".append", en este caso, "Plato 1", imprimiendo cuál elemento se añadió
def desapilar(pila):  # Pop
    if not esta_vacia(pila): 
        elemento = pila.pop()
        print(f"Se desapiló: {elemento}")
        return elemento
    else:
        print("La pila está vacía. No se puede desapilar.")
#se desapila un elemento de la fila, en caso de que esta tenga al menos uno, de lo contrario imprime el mensaje de la línea 20
def ver_tope(pila):  # Peek
    if not esta_vacia(pila):
        print(f"Elemento en el tope: {pila[-1]}") #Con "peek", la pila imprime el elemento más reciente en la pila, en este caso el plato 3
        return pila[-1]
    else:
        print("La pila está vacía.") #si la pila no tiene ningúun elemento, se imprime el mensaje anterior.

def mostrar_pila(pila):
    print("Estado actual de la pila:", pila) #Posteriormente, se muestra el estado actual de la pila tras excluir el elemento más reciente 


# --- Uso paso a paso ---
print("¿La pila está vacía?", esta_vacia(pila)) #Se imprime "¿La pila está vacía?" seguido a la función de la línea 7, con un True o False según los elementos en la fila

apilar(pila, "Caja de gallletas")
apilar(pila, "Caja de zapatos")
apilar(pila, "Caja metálica")
#Se apilan los 3 elementos, en este caso, platos
mostrar_pila(pila) #Se muestra el estado de la pila, con todos los elementos en ella
ver_tope(pila) #Se muestra el último elemento añadido

desapilar(pila) #Se desapila el último elemento
mostrar_pila(pila) #Se muestra la pila nuevamente tras eliminar el último elemento

desapilar(pila) 
desapilar(pila) #Se desapila tanto el elemento 2 y 1, por lo que esta queda vacía
desapilar(pila)  # Intento extra #Se desapila nuevamente, como la pila no tiene elementos, entonces se usa el "else" definido en la función

print("¿La pila está vacía?", esta_vacia(pila)) #Por último, pregunta si la pila está vacía. como se revisa la pila y tiene 0 elementos, True es el mensaje que salta como resultado

#Test
apilar(pila, "Caja vacía"), apilar(pila, "Caja de pólvora"), apilar(pila, "Caja con cajas dentro de otras cajas") #Añado 3 elementos
mostrar_pila(pila)
desapilar(pila)
mostrar_pila(pila) #Muestro la pila con los elementos, quito uno, muestro la pila nuevamente con el último elemento fuera
