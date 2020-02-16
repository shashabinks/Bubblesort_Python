# Bubblesort in Python

def bubble_sort(arr):

    arrLength = len(arr) - 1

    for i in range(arrLength):  # pass
        for j in range(arrLength-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [2,1,3,5]

print(bubble_sort(arr))
