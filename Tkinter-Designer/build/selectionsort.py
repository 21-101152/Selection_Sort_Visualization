def selection_sort(array_rectangles):
    min_idx = 0
    for i in range(0, len(array_rectangles)-1):
        for j in range(i+1, len(array_rectangles)):
            if array_rectangles[j]< array_rectangles[min_idx]:
                min_idx = j
        array_rectangles[i], array_rectangles[min_idx] = array_rectangles[min_idx], array_rectangles[i]
    return array_rectangles

array_rectangles = [6,5,3,234,34,5,2,5,4,4,23,2434]
print (selection_sort(array_rectangles))