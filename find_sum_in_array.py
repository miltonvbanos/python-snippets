"""
Milton V. Banos
Find pair that equals sum in array
"""
def	FindSum(arr, value):
    size = len(arr)
    i =	0
    while i	< size:
        j =	i +	1  # Start adding on next position
        while j	< size:
            if (arr[i] + arr[j]) == value:
                print("The pair for", value, "is:", arr[i], "&",	arr[j])
                return	True
            j += 1  # Look up next element
        i += 1  # Look up next element
    return	False

FindSum([1,2,4,5,7,9], 16)
FindSum([1,2,4,5,7,9], 10)
FindSum([8,2,4,5,7,8,3,8], 11)
FindSum([8,2,4,5,7,8,3,8], 10)
FindSum([8,2,4,5,7,8,3,8], 20)
