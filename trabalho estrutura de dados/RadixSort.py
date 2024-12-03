def countingSort(array, exp, base=10):
    n = len(array)
    output = [0] * n
    count = [0] * base

    for i in range(n):
        index = array[i] // exp
        count[index % base] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = array[i] // exp
        output[count[index % base] - 1] = array[i]
        count[index % base] -= 1
        i -= 1

    for i in range(n):
        array[i] = output[i]

def radixSort(array, base=10):
    max_val = max(array)
    exp = 1
    while max_val // exp > 0:
        countingSort(array, exp, base)
        exp *= base

    return array

# Teste com diferentes tamanhos de números
array_2_digits = [12, 45, 23, 56, 34, 78, 67, 89]
array_5_digits = [12345, 67890, 54321, 98765, 23456, 87654]
array_10_digits = [1234567890, 9876543210, 1029384756, 5647382910]

print("Array de 2 dígitos ordenado:", radixSort(array_2_digits))
print("Array de 5 dígitos ordenado:", radixSort(array_5_digits))
print("Array de 10 dígitos ordenado:", radixSort(array_10_digits))
