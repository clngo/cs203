

def selection_sort(l:list) -> list:
    comparisons = 0
    for idx in range(len(l)-1): #start by checking the first element; no need to check last element since the last element be switched
        #print(f"{idx}: {l}")
        for idx2 in range(idx+1, len(l)): #comparing element after first
            comparisons += 1
            if l[idx] > l[idx2]: #if current element is greater, swap so the lower value is in the front
                l[idx], l[idx2] = l[idx2], l[idx]
    return comparisons

def insertion_sort(l:list) -> list:
    comparisons = 0
    for idx in range(1, len(l)):
        idx2 = idx-1
        while idx2 >= 0:
            if l[idx] < l[idx2]:
                l[idx], l[idx2] = l[idx2], l[idx]
                idx2 -= 1
                idx -= 1
                comparisons += 1

            else:
                break
    return comparisons

example = [54, 26, 93, 17, 77, 34, 44, 55, 77]
example2 = [4, 3, 2, 10, 12, 1, 5, 6]
example3 = [10, 8, 7, 23, 2, 1, 9, 3]

# print(selection_sort(example))
# print(selection_sort(example2))

#
# print(insertion_sort(example))
# print(insertion_sort(example2))
# print(insertion_sort(example3))

