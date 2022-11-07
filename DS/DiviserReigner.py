def findMaxMin(arr):

    minn = 10000000
    maxx = -10000000

    if len(arr) == 1:
        minn, maxx = arr[0], arr[0]
        return minn, maxx

    if len(arr) == 2:
        if arr[0] >= arr[1]:
            minn, maxx = arr[1], arr[0]

        else:
            minn, maxx = arr[0], arr[1]

        return minn, maxx

    mid = len(arr)//2
    minn = min(findMaxMin(arr[:mid])[0], findMaxMin(arr[mid:])[0])
    maxx = max(findMaxMin(arr[:mid])[1], findMaxMin(arr[mid:])[1])

    return minn, maxx

#print(findMaxMin([1, -1, 3, 4, 1000, -100]))

def finddups(arr, dict = {}):

    if arr[0] == arr[len(arr)-1]:
        if arr[0] in dict:
            dict[arr[0]] += len(arr)
        else:
            dict[arr[0]] = len(arr)

        return

    mid = len(arr) // 2
    finddups(arr[:mid], dict)
    finddups(arr[mid:], dict)

#dict = {}
#finddups([2,2,2,4,4,5,5,6,8,8,9], dict)
#print(dict)

def findpeak(arr):

    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        if arr[1] > arr[0]:
            return arr[1]

    mid = len(arr) // 2
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]

    else:
        if arr[mid+1] < arr[mid-1]:
            return findpeak(arr[:mid])
        else:
            return findpeak(arr[mid:])


print(findpeak([10,8,6,5,3,2]))