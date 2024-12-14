
#https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html
from timeit import default_timer as timer
import random

def generate_list(n:int):
    return [random.randint(0, n) for i in range(n)]

def sequential_search(a:list[int], item):
    start = timer()
    for val in a:
        if val == item:
            end = timer()
            print(f"Time required: {end - start} seconds")
            return True
    end = timer()
    print(f"Time required: {end-start}")
    return False

def binary_search(a:list[int], item, low, high):
    mid = (high+low)//2
    #print(f"low: {low}, high: {high}")
    if a[mid] == item:
        return True
    elif low > high: #if they cross, there is no item
        return False
    elif a[mid] < item: #if current is less than the target, low is middle + 1
        return binary_search(a, item, mid+1, high)
    elif a[mid] > item: #if current is greater than the target, high is middle - 1
        return binary_search(a, item, low, mid-1)

range_len = 999999
ex = generate_list(range_len)

#print(ex)
#start = timer()
print("Sequential Search:\n")
print(sequential_search(ex, 555))
print(sequential_search(ex, 1750))
print(sequential_search(ex, 4850))
print(sequential_search(ex, 9053))
print(sequential_search(ex, 8564))
print(sequential_search(ex, 57575))
#print(f"Time required: {timer()-start}")


ex = sorted(ex)
print("Binary Search:\n")
start = timer()
print(binary_search(ex, 555, 0, range_len-1))
print(f"Time required: {timer()-start}")

start = timer()
print(binary_search(ex, 1750, 0, range_len-1))
print(f"Time required: {timer()-start}")

start = timer()
print(binary_search(ex, 4850, 0, range_len-1))
print(f"Time required: {timer()-start}")

start = timer()
print(binary_search(ex, 9053, 0, range_len-1))
print(f"Time required: {timer()-start}")

start = timer()
print(binary_search(ex, 8564, 0, range_len-1))
print(f"Time required: {timer()-start}")

start = timer()
print(binary_search(ex, 57575, 0, range_len-1))
print(f"Time required: {timer()-start}")
