#1 without multithreading
import random
import time

start = time.time()

for i in range(10):
    with open(f"file_{i}.txt", "w") as f:
        for j in range(100000):
            f.write(str(random.randint(1, 1000)) + "\n")

end = time.time()
print(f"Time taken to create files: {end - start:.2f} seconds")

start = time.time()

sum = 0
count = 0
for i in range(10):
    with open(f"file_{i}.txt", "r") as f:
        for line in f:
            sum += int(line)
            count += 1

average = sum / count

end = time.time()
print(f"Time taken to calculate average: {end - start:.2f} seconds")


#1 with multithreading
import random
import time
import threading

start = time.time()


def create_files(i):
    with open(f"file_{i}.txt", "w") as f:
        for j in range(100000):
            f.write(str(random.randint(1, 1000)) + "\n")

threads = []
for i in range(10):
    thread = threading.Thread(target=create_files, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print(f"Time taken to create files: {end - start:.2f} seconds")

start = time.time()


sum = 0
count = 0
def calculate_average(i):
    nonlocal sum, count
    with open(f"file_{i}.txt", "r") as f:
        for line in f:
            sum += int(line)
            count += 1

threads = []
for i in range(10):
    thread = threading.Thread(target=calculate_average, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

average = sum / count

end = time.time()
print(f"Time taken to calculate average: {end - start:.2f} seconds")


#2 with and without multithreading
import random
import time
import threading

def calculate_amounts(filename):
    with open(filename, 'w') as f:
        for i in range(100000):
            number = str(random.randint(1, 1000))
            f.write(number + '\n')
    with open(filename, 'r') as f:
        values = [int(line.strip()) for line in f]
    sum_values = sum(values)
    sum_first_digits = sum([int(str(value)[0]) for value in values])
    sum_last_digits = sum([int(str(value)[-1]) for value in values])
    print(f'Sum of all values: {sum_values}')
    print(f'Sum of all first digits: {sum_first_digits}')
    print(f'Sum of all last digits: {sum_last_digits}')

def calculate_amounts_threaded(filename):
    t = threading.Thread(target=calculate_amounts, args=(filename,))
    t.start()
    t.join()

if __name__ == '__main__':
    filename = 'numbers.txt'
    start_time = time.time()
    calculate_amounts(filename)
    print(f'Time without multithreading: {time.time() - start_time:.2f} seconds')
    start_time = time.time()
    calculate_amounts_threaded(filename)
    print(f'Time with multithreading: {time.time() - start_time:.2f} seconds')

#3 with and without multithreading
import matplotlib.pyplot as plt
import numpy as np
import time
import threading

def draw_graph(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()

def draw_graph_threaded(x_values, y_values):
    t = threading.Thread(target=draw_graph, args=(x_values, y_values))
    t.start()
    t.join()

if __name__ == '__main__':
    x_values = np.linspace(-10, 10, 1000)
    y_values = (x_values**3 - 6)/(2 - x_values**2)
    start_time = time.time()
    draw_graph(x_values, y_values)
    print(f'Time without multithreading: {time.time() - start_time:.2f} seconds')
    start_time = time.time()
    draw_graph_threaded(x_values, y_values)
    print(f'Time with multithreading: {time.time() - start_time:.2f} seconds')


#6 deadlock
import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_1():
    lock1.acquire()
    print("Thread 1 acquired lock 1")
    lock2.acquire()
    print("Thread 1 acquired lock 2")

def thread_2():
    lock2.acquire()
    print("Thread 2 acquired lock 2")
    lock1.acquire()
    print("Thread 2 acquired lock 1")

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()
