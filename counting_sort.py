#!/usr/bin/env python3

def counting_sort(arr):

    max_num = max(arr)      # Find the maximum number for a range

    count_list = [0] * (max_num + 1)       # Initialize list of occurences to 0s
    
    for num in arr:
        count_list[num] += 1           # Count the occurences

    i = 0
    for j in range(max_num + 1):
         for _ in range(count_list[j]):
             arr[i] = j
             i += 1

    return arr

def main():

    arr = [1, 3, 4, 2, 1, 6, 2, 3, 6]
    print("Before: ", arr)
    counting_sort(arr)
    print("After: ", arr)



if __name__ == "__main__":

    main()