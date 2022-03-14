import random
import time


# insertion sort
def insertion_sort(arr):
    for a in range(1, len(arr)):
        for b in range(a, 0 ,-1):
            if arr[b] < arr[b-1]:
                arr[b], arr[b-1] = arr[b-1], arr[b]
            else:
                break
    return arr

# quick sort
def split(values, first, last):
    splitVal = values[first]
    saveFirst = first

    first += 1
    while(True):
        onCorrectSide = True
        while(onCorrectSide):
            if(values[first] > splitVal):
                onCorrectSide = False
            else:
                first += 1
                onCorrectSide = (first <= last)

        onCorrectSide = (first <= last)

        while(onCorrectSide):
            if(values[last] <= splitVal):
                onCorrectSide = False
            else:
                last -= 1
                onCorrectSide = (first <= last)

        if(first < last):
            values[first], values[last] = values[last], values[first]
            first += 1
            last -= 1

        if (first > last):
            break
        
    splitPoint = last
    values[saveFirst], values[splitPoint] = values[splitPoint], values[saveFirst]

    return splitPoint


    
def quick_sort(values, first, last):
    if (first < last):
        splitPoint = split(values, first, last)
        quick_sort(values, first, splitPoint - 1)
        quick_sort(values, splitPoint + 1, last)
        return values


if __name__ == "__main__":
    l = [random.randint(1, 1000) for _ in range(80000)]
    start = time.time()
    quick_sort(l, 0, 79999)
    print(time.time()-start, '초')

