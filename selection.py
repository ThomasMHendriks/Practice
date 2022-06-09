import sys
'''
Selection sort script that sorts a list of integers passed in as a argument.
Add the numbers seperated by comma's as a command line argument. Ex: 4,8,321,126,3,465,45,64,21,65,5,9,10
'''
if len(sys.argv) != 2:
    sys.exit(
        "Please add exactly one list of number divided by comma's to sort as argument")

if __name__ == "__main__":
    array = map(int, sys.argv[1].split(','))
    array = list(array)

    if len(array) < 2:
        print(array)
        sys.exit()

    # Sort the array
    for i in range(len(array) - 1):
        maximum = None

        for j in range(len(array) - i - 1):
            if maximum == None:
                maximum = j
            elif array[maximum] < array[j]:
                maximum = j

        # Swap the highest value to the back of the array
        if array[len(array) - i - 1] < array[maximum]:
            temp = array[len(array) - i - 1]
            array[len(array) - i - 1] = array[maximum]
            array[maximum] = temp

    # Print the in place sorted array
    print(array)

else:
    sys.exit("Script is imported")
