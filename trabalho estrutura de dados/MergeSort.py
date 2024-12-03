def mergeSort(array):

    if len(array) > 1:

        meio = len(array) // 2

        esquerda = array[:meio]
        direita = array[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        i = j = k = 0


        while i <len(esquerda) and len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1

            else:
                array[k] = direita[j]
                j += 1
            k += 1

            while i < len(esquerda):
                array[k] = esquerda[i]
                i += 1
                k += 1


strings = ["Matheus", "Lucas", "Pedro","Alberto"]
mergeSort(strings)

print("Lista em ordem alfabetica:", strings)
