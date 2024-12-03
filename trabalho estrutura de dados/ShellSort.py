import time

#intervalo Shell
def shellSortShell(array, n):
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = array[i]
            j = i
            while j >= intervalo and array[j - intervalo] > temp:
                array[j] = array[j - intervalo]
                j -= intervalo
            array[j] = temp
        intervalo //= 2

#intervalo Knuth
def shellSortKnuth(array, n):
    intervalo = 1
    while intervalo < n // 3:
        intervalo = intervalo * 3 + 1
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = array[i]
            j = i
            while j >= intervalo and array[j - intervalo] > temp:
                array[j] = array[j - intervalo]
                j -= intervalo
            array[j] = temp
        intervalo //= 3

#intervalo Hibbard
def shellSortHibbard(array, n):
    intervalo = 1
    while intervalo < n:
        intervalo = 2 * intervalo + 1
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = array[i]
            j = i
            while j >= intervalo and array[j - intervalo] > temp:
                array[j] = array[j - intervalo]
                j -= intervalo
            array[j] = temp
        intervalo = (intervalo - 1) // 2

def measure_time(sort_function, array):
    start_time = time.time()
    sort_function(array, len(array))
    end_time = time.time()
    return end_time - start_time

data = [10, 9, 8, 7, 6, 5, 4, 3, 1]
data_knuth = data.copy()
data_hibbard = data.copy()

time_shell = measure_time(shellSortShell, data.copy())
time_knuth = measure_time(shellSortKnuth, data_knuth)
time_hibbard = measure_time(shellSortHibbard, data_hibbard)

print(f"Tempo de execução (Shell): {time_shell:.6f} segundos")
print(f"Tempo de execução (Knuth): {time_knuth:.6f} segundos")
print(f"Tempo de execução (Hibbard): {time_hibbard:.6f} segundos")

