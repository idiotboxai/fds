'''
Write a Python program to store first year percentage of students in array. Write
function for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.'''


def selection_sort(a):
    # O(n^2)
    n = 0
    for _ in a:
        n += 1

    for i in range(n - 1):
        min_index = i
        for j in range(i, n):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        print(a)


def bubble_sort(a):
    # O(n^2)
    n = 0
    for _ in a:
        n += 1

    for _ in range(n):
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
            print(a)


a = [7, 5, 4, 9, 2, 10, 3]

print("Unsorted Array: ", a)
bubble_sort(a)
print("Sorted Array: ", a)

