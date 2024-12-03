import time
import random

def selectionSort(array, mostrar_passos=False):
    for index in range(0, len(array)):
        min_index = index

        for direita in range(index + 1, len(array)):
            if array[direita] < array[min_index]:
                min_index = direita

        array[index], array[min_index] = array[min_index], array[index]

        if mostrar_passos:
            print(f"Passo {index + 1}: {array}")

def measure_time(sort_function, array, mostrar_passos=False):
    start_time = time.time()
    sort_function(array, mostrar_passos)
    end_time = time.time()
    return end_time - start_time

small_list = random.sample(range(1, 101), 10)
medium_list = random.sample(range(1, 10001), 1000)
large_list = random.sample(range(1, 100001), 10000)

print("Passo a Passo da Lista Pequena:")
small_time = measure_time(selectionSort, small_list.copy(), mostrar_passos=True)
print(f"Tempo de execução para lista pequena (10 elementos): {small_time:.6f} segundos\n")

medium_time = measure_time(selectionSort, medium_list.copy())
large_time = measure_time(selectionSort, large_list.copy())

print(f"Tempo de execução para lista média (1000 elementos): {medium_time:.6f} segundos")
print(f"Tempo de execução para lista grande (10000 elementos): {large_time:.6f} segundos")
