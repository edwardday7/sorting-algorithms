#!/usr/bin/env python3


def bubble_sort(arr):
    for i in range(len(arr)):   # Largest element will bubble to the end
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]


def main():
    arr = [2, 4, 12, 1, 7, 8]
    print("Before: ", arr)
    bubble_sort(arr)
    print("After: ", arr)

if __name__ == "__main__":
    main()