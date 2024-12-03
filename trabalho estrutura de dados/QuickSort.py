import random
import time

def quickSort(array, low, high, pivot_choice='first'):
    if low < high:
        pi = partition(array, low, high, pivot_choice)
        quickSort(array, low, pi - 1, pivot_choice)  
        quickSort(array, pi + 1, high, pivot_choice)  

def partition(array, low, high, pivot_choice):
    if pivot_choice == 'first':
        pivot = array[low]
    elif pivot_choice == 'last':
        pivot = array[high]
    elif pivot_choice == 'middle':
        pivot = array[(low + high) // 2]
    
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]  
    return i + 1

def measure_time(sort_function, array, pivot_choice='first'):
    start_time = time.time()
    sort_function(array, 0, len(array) - 1, pivot_choice)
    end_time = time.time()
    return end_time - start_time

# Lista desordenada e quase ordenada
array_desordenado = random.sample(range(1, 10001), 1000)
array_quase_ordenado = list(range(1, 1001))  # Lista quase ordenada
array_quase_ordenado[-1], array_quase_ordenado[500] = array_quase_ordenado[500], array_quase_ordenado[-1]  # Troca dois elementos para tornar "quase ordenada"

# Testes de desempenho
print("Desempenho em lista desordenada:")
for pivot_choice in ['first', 'last', 'middle']:
    array_copy = array_desordenado.copy()
    time_taken = measure_time(quickSort, array_copy, pivot_choice)
    print(f"Critério {pivot_choice}: {time_taken:.6f} segundos")

print("\nDesempenho em lista quase ordenada:")
for pivot_choice in ['first', 'last', 'middle']:
    array_copy = array_quase_ordenado.copy()
    time_taken = measure_time(quickSort, array_copy, pivot_choice)
    print(f"Critério {pivot_choice}: {time_taken:.6f} segundos")
