from lab6 import insertion_sort
from lab6 import selection_sort
from timeit import default_timer as timer
import random
#https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html


def generate_list(n:int):
    return [random.randint(0, n) for i in range(n)]

print("Selection Sorts:")
test1 = generate_list(1000)
# start = timer()
# print(selection_sort(test1))
# print(f"List size 1000: {timer() - start}")

test2 = generate_list(2000)
# start = timer()
# print(selection_sort(test2))
# print(f"List size 2000: {timer() - start}")

test3 = generate_list(4000)
# start = timer()
# print(selection_sort(test3))
# print(f"List size 4000: {timer() - start}")

test4 = generate_list(8000)
# start = timer()
# print(selection_sort(test4))
# print(f"List size 8000: {timer() - start}")

# test5 = generate_list(16000)
# start = timer()
# print(selection_sort(test5))
# print(f"List size 16000: {timer() - start}")
#
# test6 = generate_list(32000)
# start = timer()
# print(selection_sort(test6))
# print(f"List size 32000: {timer() - start}")
#
# test7 = generate_list(100000)
# start = timer()
# print(selection_sort(test7))
# print(f"List size 100000: {timer() - start}")
#
# test8 = generate_list(500000)
# start = timer()
# print(selection_sort(test8))
# print(f"List size 500000: {timer() - start}")
#
# test9 = generate_list(1000000)
# start = timer()
# print(selection_sort(test9))
# print(f"List size 1000000: {timer() - start}")
#
# test10 = generate_list(10000000)
# start = timer()
# print(selection_sort(test10))
# print(f"List size 10000000: {timer() - start}")



print("Insertion Sorts:")
start = timer()
print(insertion_sort(test1))
print(f"List size 1000: {timer() - start}")

start = timer()
print(insertion_sort(test2))
print(f"List size 2000: {timer() - start}")

start = timer()
print(insertion_sort(test3))
print(f"List size 4000: {timer() - start}")

start = timer()
print(insertion_sort(test4))
print(f"List size 8000: {timer() - start}")
#
# start = timer()
# print(insertion_sort(test5))
# print(f"List size 16000: {timer() - start}")
#
# start = timer()
# print(insertion_sort(test6))
# print(f"List size 32000: {timer() - start}")
#
# start = timer()
# print(insertion_sort(test7))
# print(f"List size 100000: {timer() - start}")
#
# start = timer()
# insertion_sort(test8)
# print(f"List size 500000: {timer() - start}")
#
# start = timer()
# insertion_sort(test9)
# print(f"List size 1000000: {timer() - start}")
#
# start = timer()
# insertion_sort(test10)
# print(f"List size 1000000: {timer() - start}")



