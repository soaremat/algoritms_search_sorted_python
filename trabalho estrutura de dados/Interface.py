
from MergeSort import merge_sort
from QuickSort import quick_sort
from SelectionSort import selection_sort
from BinarySearch import binary_search
from InterpolationSearch import interpolation_search
from BucketSort import bucket_sort

def main():
    print("Escolha uma das opções abaixo:")
    print("1 - Merge Sort")
    print("2 - Quick Sort")
    print("3 - Selection Sort")
    print("4 - Binary Search")
    print("5 - Interpolation Search")
    print("6 - Bucket Sort")

    opcao = int(input("Digite o número da sua escolha: "))

    if opcao in [1, 2, 3, 6]:  # Algoritmos de ordenação
        lista = input("Digite os elementos da lista separados por vírgulas: ")
        lista = [int(x) for x in lista.split(",")]

        if opcao == 1:
            print("Lista ordenada usando Merge Sort:")
            print(merge_sort(lista))
        elif opcao == 2:
            print("Lista ordenada usando Quick Sort:")
            print(quick_sort(lista))
        elif opcao == 3:
            print("Lista ordenada usando Selection Sort:")
            print(selection_sort(lista))
        elif opcao == 6:
            print("Lista ordenada usando Bucket Sort:")
            print(bucket_sort(lista))

    elif opcao in [4, 5]:  # Algoritmos de busca
        lista = input("Digite os elementos da lista ordenada separados por vírgulas: ")
        lista = [int(x) for x in lista.split(",")]

        elemento = int(input("Digite o elemento a ser buscado: "))

        if opcao == 4:
            resultado = binary_search(lista, elemento, 0, len(lista) - 1)
            if resultado != -1:
                print(f"Elemento encontrado no índice {resultado}.")
            else:
                print("Elemento não encontrado.")
        elif opcao == 5:
            resultado = interpolation_search(lista, elemento)
            if resultado != -1:
                print(f"Elemento encontrado no índice {resultado}.")
            else:
                print("Elemento não encontrado.")

    else:
        print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
