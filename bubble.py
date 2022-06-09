import sys
'''
Bubble sort script that sorts a list of integers passed in as a argument.
Add the numbers seperated by comma's as a command line argument like. Ex: 4,8,321,126,3,465,45,64,21,65,5,9,10
'''
if len(sys.argv) != 2:
    sys.exit("Please add exactly one array to sort as argument")

if __name__ == "__main__":
    array = map(int, sys.argv[1].split(','))
    array = list(array)

    # Loop through the array nearly array size * array size times while letting the biggest elements "bubble" to the back of the array
    for i in range(len(array) - 1):
        swap_made = False

        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap_made = True

        # Can finish early if all elements are in order after x loop cycles
        if swap_made == False:
            break

    print(array)

else:
    sys.exit("Script is imported")
