from threading import Thread
from time import sleep

def thread_function(n, result):
    sleep(n)
    print("Appending %d..." % n)
    result.append(n)


def make_thread(amount_to_sleep, result):
    thread = Thread(target=thread_function, args=(amount_to_sleep, result))
    thread.start()  # this will run thread_function in a thread
    
    # thread.join() # This will block until the thread is done
    # print('thread finished')


# Sorting algorithm
def sleep_sort(numbers):
    # result = [n for n in numbers]
    result = []
    for n in numbers:
        make_thread(n, result)
           
    while len(result) != len(numbers):
        1
    return result

if __name__ == "__main__":
    print(sleep_sort([3, 0, 1, 2]))