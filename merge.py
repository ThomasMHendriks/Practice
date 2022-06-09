import sys
'''
Merge sort script that sorts a list of integers passed in as a argument.
Add the numbers seperated by comma's as a command line argument like. Ex: 4,8,321,126,3,465,45,64,21,65,5,9,10
'''
if len(sys.argv) != 2:
    sys.exit("Please add exactly one array to sort as argument")


def merge(arr):
    # Base case
    if len(arr) == 1:
        return arr

    # create subarrays and call recursively
    mid = len(arr) // 2
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    i, j, sorted = 0, 0, []

    # add the subarrays to the empty array sorted based on size
    while i < len(left) or j < len(right):

        # check if one of the 2 arrays is empty
        if i >= len(left):
            sorted.append(right[j])
            j += 1
        elif j >= len(right):
            sorted.append(left[i])
            i += 1

        # if both arrays are not empty, add both
        else:
            if left[i] <= right[j]:
                sorted.append(left[i])
                i += 1
            else:
                sorted.append(right[j])
                j += 1

    return sorted


# Code to parse the input and call the merge function
if __name__ == "__main__":
    array = map(int, sys.argv[1].split(','))
    array = list(array)

    print(merge(array))

else:
    sys.exit("Script is imported")
