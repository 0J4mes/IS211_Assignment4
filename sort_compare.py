import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order"""
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    time_taken = time.time() - start
    return time_taken

def shell_sort(a_list):
    start = time.time()
    sublistcount = len(a_list) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(a_list, startposition, sublistcount)
        sublistcount = sublistcount // 2
    time_taken = time.time() - start
    return time_taken

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    start = time.time()
    sorted_list = sorted(a_list)
    time_taken = time.time() - start
    return time_taken

if __name__ == "__main__":
    list_sizes = [500, 1000, 5000]
    for the_size in list_sizes:
        # Python Sort
        total_time = 0
        for _ in range(100):
            mylist = get_me_random_list(the_size)
            time_spent = python_sort(mylist)
            total_time += time_spent
        avg_time = total_time / 100
        print(f"Python sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        # Insertion Sort
        total_time = 0
        for _ in range(100):
            mylist = get_me_random_list(the_size)
            time_spent = insertion_sort(mylist)
            total_time += time_spent
        avg_time = total_time / 100
        print(f"Insertion sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")

        # Shell Sort
        total_time = 0
        for _ in range(100):
            mylist = get_me_random_list(the_size)
            time_spent = shell_sort(mylist)
            total_time += time_spent
        avg_time = total_time / 100
        print(f"Shell sort took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
