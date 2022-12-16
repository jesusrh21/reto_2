def fibonacci()->list:
    """
    funcion que escribe los primeros 50 numeros de la serie de Fibonacci

    Atributos:
     - None

    Return:
     - serief : list 
    """
    serief = [] # lista que contendrá la serie de fibonacci
    for i in range(0,50): # ciclo for para controlar el limite de iteraciones
        if i == 0 or i == 1: # si los valores son 0 y 1 los agrego directamente los 2 primeros
            serief.append(i)
        else: # Para el 3er valor buscar los 2 antecesores en la lista y sumarlos 
            serief.append(
                serief[i-2] + serief[i-1]
            )      
    return serief


if __name__ == '__main__':
    print(fibonacci())