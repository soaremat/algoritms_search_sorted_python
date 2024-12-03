def bucketSort(array, num_buckets=10):
    if len(array) == 0:
        return array

    if isinstance(array[0], float):
        return bucketSortFloats(array)
    elif isinstance(array[0], int):
        return bucketSortIntegers(array, num_buckets)
    else:
        raise TypeError("Array deve conter apenas números inteiros ou flutuantes.")

def bucketSortFloats(array):
    n = len(array)
    buckets = [[] for _ in range(n)]

    for num in array:
        index = int(n * num)
        if index == n:
            index = n - 1
        buckets[index].append(num)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array

def bucketSortIntegers(array, num_buckets=10):
    min_val, max_val = min(array), max(array)
    bucket_range = (max_val - min_val) // num_buckets + 1
    buckets = [[] for _ in range(num_buckets)]

    for num in array:
        index = (num - min_val) // bucket_range
        buckets[index].append(num)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array


array_floats = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print("Array ordenado (flutuantes) em ordem crescente:")
print(bucketSort(array_floats))

array_integers = [42, 32, 33, 52, 37, 47, 51]
print("Array ordenado (inteiros) em ordem crescente:")
print(bucketSort(array_integers))
