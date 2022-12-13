import concurrent.futures
import time


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 1000


def find_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


# concurrent_features_ThreadPoolExecutor

def main():
    started_at1 = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        factorial_result1 = executor.map(find_factorial, num_list)

    threads_exec_time = time.time() - started_at1
    print(f'Time_Thread: {threads_exec_time}')
    print(len(list(factorial_result1)))

# concurrent_features_ProcessPoolExecutor

    started_at2 = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        factorial_result2 = executor.map(find_factorial, num_list)

    process_exec_time = time.time() - started_at2
    print(f'Time_Process: {process_exec_time}')
    print(len(list(factorial_result2)))

    if threads_exec_time < process_exec_time:
        print(f'Optimal method is ThreadPoolExecutor. Speed test: {threads_exec_time}.')
    else:
        print(f'Optimal method is ProcessPoolExecutor. Speed test: {process_exec_time}.')


if __name__ == '__main__':
    main()
