import random
import time

def ternarySearch(array, left, right, X):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if array[mid1] == X:
            return mid1
        if array[mid2] == X:
            return mid2

        if X < array[mid1]:
            return ternarySearch(array, left, mid1 - 1, X)
        elif X > array[mid2]:
            return ternarySearch(array, mid2 + 1, right, X)
        else:
            return ternarySearch(array, mid1 + 1, mid2 - 1, X)

    return -1

def binarySearch(array, left, right, X):
    while right >= left:
        mid = left + (right - left) // 2
        
        if array[mid] == X:
            return mid
        elif array[mid] > X:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def measure_time(search_function, array, X, search_type="Ternary"):
    start_time = time.time()
    if search_type == "Ternary":
        result = search_function(array, 0, len(array) - 1, X)
    else:
        result = search_function(array, 0, len(array) - 1, X)
    end_time = time.time()
    return result, end_time - start_time

# Teste com uma lista ordenada
array = sorted(random.sample(range(1, 10001), 1000))  # Lista ordenada de 1000 elementos
X = random.choice(array)  # Escolhendo um valor aleatório para testar

# Medindo o tempo de execução do Ternary Search
ternary_result, ternary_time = measure_time(ternarySearch, array, X, search_type="Ternary")
print(f"Ternary Search: {ternary_result} encontrado em {ternary_time:.6f} segundos")

# Medindo o tempo de execução do Binary Search
binary_result, binary_time = measure_time(binarySearch, array, X, search_type="Binary")
print(f"Binary Search: {binary_result} encontrado em {binary_time:.6f} segundos")
