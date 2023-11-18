def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                print(f"Elementos no ordenados encontrados: {arr[j]}, {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"Realizando swap: {arr[j]}, {arr[j + 1]}")
                print(f"Lista actualizada: {arr}")
    print("Lista ordenada por bubble sort:", arr)


def quick_sort(arr, bajo, alto):
    if bajo < alto:
        pi = particion(arr, bajo, alto)

        print(f"Diviendo la lista en dos: {arr[bajo:pi] + ['¨[<- Menores | Mayores ->]'] + arr[pi + 1:]}")
        quick_sort(arr, bajo, pi - 1)
        quick_sort(arr, pi + 1, alto)


def particion(arr, bajo, alto):
    pivote = arr[alto]
    print(f"Pivote elegido: {pivote}")
    i = bajo - 1

    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]

    return i + 1


def main():
    lista = [95, 36, 42, 0, 32, 58, 73, 28, 43, 12, 50]
    print(f"Lista a ordenar: {lista}")
    bubble_sort(lista.copy())
    print("--------------------------------------------")
    print("Ordenando la lista con Quick Sort")
    print(f"Lista a ordenar:{lista}")
    quick_sort(lista, 0, len(lista) - 1)
    print(f"Lista ordenada por quick sort: {lista}")


if __name__ == '__main__':
    main()
