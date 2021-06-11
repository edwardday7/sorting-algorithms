#!/usr/bin/env python3


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
    
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge arrays
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] == left_arr[i]
                i += 1
            else:
                arr[k] == right_arr[j]
                j += 1
            k += 1
        
        while i < len(left_arr):    # still elements missing
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1



def main():
    l = [2, 3, 8, 1, 4, 6, 9]
    print("Before: ", l)
    merge_sort(l)
    print("After: ", l)

if __name__ == "__main__":
    main()