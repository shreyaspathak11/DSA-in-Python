
def partitionArray(arr: List[int], low: int, high: int) -> int:
    """
    This function partitions the array based on the pivot element and returns the index of the pivot element.

    Parameters:
    arr (List[int]): The input array to be partitioned.
    low (int): The starting index of the partitioning range.
    high (int): The ending index of the partitioning range.

    Returns:
    int: The index of the pivot element after partitioning.
    """

    # Choose the pivot element (in this case, the element at the 'low' index)
    pivot = arr[low]

    # Initialize two pointers 'i' and 'j' to the start and end of the partitioning range
    i = low
    j = high

    # Continue partitioning until 'i' crosses 'j'
    while i < j:
        # Move 'i' towards the right until it finds an element greater than the pivot or reaches the end of the range
        while arr[i] <= pivot and i <= high-1:
            i += 1

        # Move 'j' towards the left until it finds an element smaller than or equal to the pivot or reaches the start of the range
        while arr[j] > pivot and j >= low+1:
            j -= 1

        # If 'i' and 'j' have not crossed each other, swap the elements at 'i' and 'j'
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element (at 'low') with the element at 'j' to put the pivot in its correct position
    arr[low], arr[j] = arr[j], arr[low]

    # Return the index of the pivot element after partitioning
    return j


def quickSort(arr: List[int], low: int, high: int):
    """
    This function implements the Quick Sort algorithm to sort the input array.

    Parameters:
    arr (List[int]): The input array to be sorted.
    low (int): The starting index of the range to be sorted.
    high (int): The ending index of the range to be sorted.
    """

    # Check if there are elements to sort (i.e., 'low' is less than 'high')
    if low < high:
        # Get the index of the partitioning element using the partitionArray function
        p_index = partitionArray(arr, low, high)

        # Recursively sort the left and right subarrays, excluding the pivot element
        quickSort(arr, low, p_index-1)
        quickSort(arr, p_index+1, high)
