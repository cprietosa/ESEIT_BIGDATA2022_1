import numpy as np
import argparse


def calcular_extremos(lista_numeros, verbose=1):
    """calcula el valor minimo y maximo de una lista de numeros

    Args:
        lista_numeros (lista):lista de numeros con valores enteros

    Returns:
        tuple: (minimo,maximo)
    """

    min_val = np.min(lista_numeros)
    max_val = np.max(lista_numeros)

    if verbose == 1:
        print('calcular_extremos')
        print('minimo', min)
        print('maximo', max)
    else:
        pass
    return min,max

    print('calcular_extremos')
    print('minimo', min_val)
    print('maximo', max_val)
    return min_val, max_val

def calcular_valores_centrales(lista_numeros, verbose =1):
    """calcula la media y la desviacion estandar de una lista de numeros

    Args:
        lista_numeros (lista): lista de numeros con valores enteros

    Returns:
        tupla: (media, desviacion estandar)
    """

    media   = np.mean(lista_numeros)
    dev_std = np.std(lista_numeros)

    if verbose == 1:
        print('calcular_valores_centrales')
        print('media', media)
        print('desv_std', dev_std)
    else:
        pass
    return media, dev_std

    print('calcular_valores_centrales')
    print('media', media)
    print('desv std', dev_std)
    return media, dev_std

def calcular_suma(lista_numeros, verbose =1):
    '''
    Calcula la suma de una lista de numeros
    Args:
        lista_numeros : lista de numeros
    '''
    resultado = np.sum(lista_numeros)

    if verbose == 1:
        print('calcular_suma')
        print('suma', resultado)
    else:
        pass
    return resultado

    print('calcular_suma')
    print('suma', resultado)
    return resultado

def calcular_valores(lista_numeros, verbose = 1):
    suma             = calcular_suma(lista_numeros, verbose)
    media, dev_std   = calcular_valores_centrales(lista_numeros, verbose)
    min_val, max_val = calcular_extremos(lista_numeros, verbose)
    return suma, media, dev_std, min_val, max_val

def main():
    parser = argparse.ArgumentParser
    parser.add_argument("--verbose", type=int, default=1, help="para decir si imprime informacon")


    args = parser.parse_arg()

    verbose = args.verbose



    lista_numeros = [1, 5, 8, 3, 45, 93]
    suma, media, dev_std, min_val, max_val = calcular_valores(lista_numeros,verbose)
    print(suma, media, dev_std, min_val, max_val)

if __name__ == '__main__':
    main()

