import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    time_taken = time.time() - start
    return found, time_taken

def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    time_taken = time.time() - start
    return found, time_taken

def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    time_taken = time.time() - start
    return found, time_taken

def binary_search_recursive(a_list, item):
    start = time.time()
    def recursive_helper(a_list, item):
        if len(a_list) == 0:
            return False
        else:
            midpoint = len(a_list) // 2
            if a_list[midpoint] == item:
                return True
            else:
                if item < a_list[midpoint]:
                    return recursive_helper(a_list[:midpoint], item)
                else:
                    return recursive_helper(a_list[midpoint + 1:], item)

    found = recursive_helper(a_list, item)
    time_taken = time.time() - start
    return found, time_taken

if __name__ == "__main__":
    list_sizes = [500, 1000, 5000]
    for the_size in list_sizes:
        # Sequential search
        total_time = 0
        for _ in range(100):
            mylist = get_me_random_list(the_size)
            found, time_spent = sequential_search(mylist, 99999999)
            total_time += time_spent
        avg_time = total_time / 100
        print(f"Sequential Search took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        # Similar benchmarking for the other search functions
        # ordered_sequential_search, binary_search_iterative, binary_search_recursive
