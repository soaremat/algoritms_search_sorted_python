
def bucketSortGrades(grades, num_buckets=10):
    if len(grades) == 0:
        return grades

    buckets = [[] for _ in range(num_buckets)]

    for grade in grades:
        index = int(grade // (100 / num_buckets))
        if index == num_buckets:  
            index -= 1
        buckets[index].append(grade)

    sorted_grades = []
    for bucket in buckets:
        sorted_grades.extend(sorted(bucket))

    return sorted_grades

def interpolationSearch(array, target):
    low, high = 0, len(array) - 1

    while low <= high and target >= array[low] and target <= array[high]:
        if low == high:
            if array[low] == target:
                return low
            return -1

        pos = low + ((target - array[low]) * (high - low) // (array[high] - array[low]))

        if array[pos] == target:
            return pos
        elif array[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


grades = [75, 95, 45, 60, 89, 38, 85, 99, 12, 67, 74, 88]

sorted_grades = bucketSortGrades(grades)
print("Notas ordenadas em ordem crescente:")
print(sorted_grades)

target_grade = 89

result = interpolationSearch(sorted_grades, target_grade)

if result != -1:
    print(f"A nota {target_grade} foi encontrada na posição {result}.")
else:
    print(f"A nota {target_grade} não foi encontrada.")
