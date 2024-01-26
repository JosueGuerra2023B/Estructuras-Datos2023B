#Guerra JoSUE
#EJEMPLO1
def pasarParametro(referencia, valor):
    referencia *= 2
    valor *= 2
    print("mensaje de la función: ", referencia, valor)

lista = ["a", "b", "c"]
dato = "abc"
print("La lista original: ", lista, dato)
pasarParametro(lista, dato)
print("Lista continua: ", lista, dato)

