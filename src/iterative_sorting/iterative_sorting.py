# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        # TO-DO: find next smallest element
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
            print(arr)
    return arr


selection_sort([5, 2, 1, 4, 4, 7, 5])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print(arr)

    return arr


bubble_sort([5, 2, 1, 4, 4, 7, 5])

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
