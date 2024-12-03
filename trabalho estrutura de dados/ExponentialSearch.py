def expionentialSearch(array, X):
    n = len(array)
    if n == 0:
        return -1
    
    if array[0] == X:
        return 0

    
    i = 1
    while i < n and array[i] < X:
        i *= 2


    esquerda = i // 2
    direita = min(i, n-1) 

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if array[meio] == X:
            return meio
        elif array[meio] < X:
            esquerda = meio +1
        else:
            direita = meio - 1    

    return -1


array = [3,5,18,29,45]
n = len(array)
X = 29
resultado = expionentialSearch(array, X)
if resultado == -1:
    print("Elemento não encontrado no array")
else:
    print(f"Elemento foi encontrado no indice {resultado}") 