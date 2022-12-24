import random
from random_words import RandomWords
import time
from statistics import mean
from sort_functions import *


int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(round(random.uniform(0.1, 100.0), 2))
    str_list.append(w.random_word())


sort_algorithms = [bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort, heap_sort]

for sort_fn in sort_algorithms:
    time_check_int = []
    time_check_float = []
    time_check_str = []

    for i in range(0, 11):
        cur_time = time.time()
        sort_fn(int_list)
        time_check_int.append(time.time() - cur_time)
        cur_time = time.time()
        sort_fn(float_list)
        time_check_float.append(time.time() - cur_time)
        cur_time = time.time()
        sort_fn(str_list)
        time_check_str.append(time.time() - cur_time)

    print(f"Average execution time for INT {sort_fn.__name__}: {mean(time_check_int)}")
    print(f"Average execution time for FLOAT {sort_fn.__name__}: {mean(time_check_float)}")
    print(f"Average execution time for STR {sort_fn.__name__}: {mean(time_check_str)}")
