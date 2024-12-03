import matplotlib.pyplot as plt

results = [
    (1000, "Merge Sort", "Random List", 0.0012),
    (1000, "Quick Sort", "Random List", 0.0011),
    (1000, "Selection Sort", "Random List", 0.0025),
    (1000, "Radix Sort", "Random List", 0.0010),
    (10000, "Merge Sort", "Random List", 0.012),
    (10000, "Quick Sort", "Random List", 0.011),
    (10000, "Selection Sort", "Random List", 0.025),
    (10000, "Radix Sort", "Random List", 0.010),
    (100000, "Merge Sort", "Random List", 0.13),
    (100000, "Quick Sort", "Random List", 0.11),
    (100000, "Selection Sort", "Random List", 2.5),
    (100000, "Radix Sort", "Random List", 0.10),
]


sizes = [10**3, 10**4, 10**5]
merge_times = [result[3] for result in results if result[1] == "Merge Sort" and result[2] == "Random List"]
quick_times = [result[3] for result in results if result[1] == "Quick Sort" and result[2] == "Random List"]
selection_times = [result[3] for result in results if result[1] == "Selection Sort" and result[2] == "Random List"]
radix_times = [result[3] for result in results if result[1] == "Radix Sort" and result[2] == "Random List"]

plt.plot(sizes, merge_times, label="Merge Sort", marker='o')
plt.plot(sizes, quick_times, label="Quick Sort", marker='o')
plt.plot(sizes, selection_times, label="Selection Sort", marker='o')
plt.plot(sizes, radix_times, label="Radix Sort", marker='o')
plt.xscale('log')  
plt.yscale('log')  
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo (s)")
plt.title("Comparação de Algoritmos de Ordenação")
plt.legend()
plt.show()
