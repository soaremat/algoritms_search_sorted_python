import time
import random
from BinarySearch import binary_search
from InterpolationSearch import interpolation_search
from JumpSearch import jump_search
from ExponentialSearch import exponential_search

def measure_time(search_function, arr, target):
    start_time = time.time()
    search_function(arr, target)
    end_time = time.time()
    return end_time - start_time

sizes = [10**4, 10**5, 10**6]
algorithms = {
    "Binary Search": binary_search,
    "Interpolation Search": interpolation_search,
    "Jump Search": jump_search,
    "Exponential Search": exponential_search
}
results = []

for size in sizes:
    arr = list(range(size)) 
    targets = {
        "Best Case": arr[0],  
        "Average Case": arr[size // 2],  
        "Worst Case": size + 1  
    }

    for case, target in targets.items():
        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm, arr, target)
            results.append((size, name, case, time_taken))

print(f"{'Size':<10} {'Algorithm':<20} {'Case':<15} {'Time (s)':<10}")
for size, name, case, time_taken in results:
    print(f"{size:<10} {name:<20} {case:<15} {time_taken:<10.6f}")
