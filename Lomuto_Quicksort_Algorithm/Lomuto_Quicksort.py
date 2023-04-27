import random


def lomutoQuicksort(A, i, j):
    if i < j:
        p = lomutoPatrition(A, i, j)
        lomutoQuicksort(A, i, p - 1)
        lomutoQuicksort(A, p + 1, j)


def lomutoPatrition(A, i, j):
    pivot = A[j]
    l = i - 1
    for k in range(i, j):
        if A[k] <= pivot:
            l += 1
            A[l], A[k] = A[k], A[l]
    A[l + 1], A[j] = A[j], A[l + 1]
    return l + 1


n = 50
A = [random.randint(0, 99) for i in range(n)]

print("Unsorted table: ")
print(A)

lomutoQuicksort(A, 0, n - 1)

print("Sorted table: ")
print(A)
