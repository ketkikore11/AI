def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Take input from the user
numbers = input("Enter a list of numbers to sort (space-separated): ").split()
numbers = [int(num) for num in numbers]

# Perform Selection Sort
sorted_numbers = selection_sort(numbers)

# Display the sorted list
print("Sorted numbers:", sorted_numbers)
