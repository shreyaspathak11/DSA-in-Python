
def binarySearch(nums: [int], low: int, high: int, target: int):
    if low > high:
        return -1  # Base case
    
    # Perform the steps:
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return binarySearch(nums, mid + 1, high, target)
    return binarySearch(nums, low, mid - 1, target)

def search(nums: [int], target: int):
    return binarySearch(nums, 0, len(nums) - 1, target)

if __name__ == "__main__":
    a = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 6
    ind = search(a, target)
    if ind == -1:
        print("The target is not present.")
    else:
        print("The target is at index:", ind) 


 

logn (base is 2)