def ordenamiento_seleccion(lista):
    n = len(lista)
    
    # Iterar sobre todos los elementos de la lista
    for i in range(n):
        # Encontrar el índice del elemento mínimo en la parte no ordenada de la lista
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
                
        # Intercambiar el elemento mínimo con el primer elemento de la parte no ordenada
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
        
    return lista

# Ejemplo de uso
lista = [64, 25, 12, 22, 11]
print("Lista original:", lista)
print("Lista ordenada por selección:", ordenamiento_seleccion(lista))