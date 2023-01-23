import random

# Create 10 files, each containing 100,000 random numbers

for i in range(10):

    with open(f"file{i}.txt", "w") as f:

        for _ in range(100_000):

            f.write(str(random.randint(1, 1000)) + "\n")

# Read contents of all files and calculate average

numbers = []

for i in range(10):

    with open(f"file{i}.txt", "r") as f:

        numbers += [int(x) for x in f.readlines()]

average = sum(numbers) / len(numbers)

print(average)


#2
import random

import threading

average = 0

lock = threading.Lock()

def create_file(i):

    with open(f"file{i}.txt", "w") as f:

        for _ in range(100_000):

            f.write(str(random.randint(1, 1000)) + "\n")

def calculate_average(numbers):

    global average

    with lock:

        average += sum(numbers)

# Create 10 threads, each responsible for creating a single file containing 100,000 random numbers

threads = []

for i in range(10):

    t = threading.Thread(target=create_file, args=(i,))

    t.start()

    threads.append(t)

for t in threads:

    t.join()

# Create a separate thread for reading contents of all files and calculating average of all numbers

threads = []

for i in range(10):

    with open(f"file{i}.txt", "r") as f:

        numbers = [int(x) for x in f.readlines()]

        t = threading.Thread(target=calculate_average, args=(numbers,))

        t.start()

        threads.append(t)

for t in threads:

    t.join()

average = average / (10*100_000)

print(average)

#3
print(average)

#3
import random

# Create a file containing 100,000 random numbers
with open("numbers.txt", "w") as f:
    for _ in range(100_000):
        f.write(str(random.randint(1, 1000)) + "\n")

# Read contents of the file and calculate sum of all values, sum of all first digits and sum of all last digits
with open("numbers.txt", "r") as f:
    numbers = [int(x) for x in f.readlines()]
    all_sum = sum(numbers)
    first_sum = sum([int(x[0]) for x in numbers])
    last_sum = sum([int(x[-1]) for x in numbers])
print("All sum:", all_sum)
print("First sum:", first_sum)
print("Last sum:", last_sum)

#4

import random
import threading

all_sum = 0
first_sum = 0
last_sum = 0
lock = threading.Lock()

def create_file():
    with open("numbers.txt", "w") as f:
        for _ in range(100_000):
            f.write(str(random.randint(1, 1000)) + "\n")

def calculate_all_sum(numbers):
    global all_sum
    with lock:
        all_sum += sum(numbers)

def calculate_first_sum(numbers):
    global first_sum
    with lock:
        first_sum += sum([int(x[0]) for x in numbers])

def calculate_last_sum(numbers):
    global last_sum
    with lock:
        last_sum += sum([int(x[-1]) for x in numbers])

# Create a thread for creating a file containing 100,000 random numbers
t = threading.Thread(target=create_file)
t.start()
t.join()

# Read contents of the file
with open("numbers.txt", "r") as f:
    numbers = [int(x) for x in f.readlines()]

# Create separate threads for calculating sum of all values, sum of all first digits and sum of all last digits
t1 = threading.Thread(target=calculate_all_sum, args=(numbers,))
t2 = threading.Thread(target=calculate_first_sum, args=(numbers,))
t3 = threading.Thread(target=calculate_last_sum, args=(numbers,))
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All sum:", all_sum)
print("First sum:", first_sum)
print("Last sum:", last_sum)

#5 graph without
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x-2)**2/(x**3-6)

x = np.linspace(-10, 10, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of (x-2)^2/(x^3-6)')
plt.show()

# with
import matplotlib.pyplot as plt
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

def f(x):
    return (x-2)**2/(x**3-6)

x = np.linspace(-10, 10, 100)
y = []

with ThreadPoolExecutor() as executor:
    future_to_x = {executor.submit(f, xi): xi for xi in x}
    for future in as_completed(future_to_x):
        y.append(future.result())

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of (x-2)^2/(x^3-6)')
plt.show()


#5 with
import matplotlib.pyplot as plt
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

def f(x):
    return (x-2)**2/(x**3-6)

x = np.linspace(-10, 10, 100)
y = []

with ThreadPoolExecutor() as executor:
    future_to_x = {executor.submit(f, xi): xi for xi in x}
    for future in as_completed(future_to_x):
        y.append(future.result())

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of (x-2)^2/(x^3-6)')
plt.show()









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












"""
Average calculation: Without multithreading:Program creates 10 files, each containing 100,000 random numbers.Time taken to create files is measured.Program reads contents of all files and calculates average of all numbers.Time taken to calculate average is measured.
With multithreading:
Program creates 10 threads, each responsible for creating a single file containing 100,000 random numbers.Time taken to create files is measured.Program creates a separate thread for reading contents of all files and calculating average of all numbers.Time taken to calculate average is measured.
With 100 files each containing 10,000 numbers:
Program creates 100 threads, each responsible for creating a single file containing 10,000 random numbers.Time taken to create files is measured.Program creates a separate thread for reading contents of all files and calculating average of all numbers.Time taken to calculate average is measured.Calculation of amounts: Without multithreading:Program creates a file containing 100,000 random numbers.Time taken to create file is measured.Program reads contents of the file and calculates sum of all values, sum of all first digits and sum of all last digits.Time taken to calculate amounts is measured.
With multithreading:
Program creates a thread for creating a file containing 100,000 random numbers.Time taken to create file is measured.Program creates separate threads for calculating sum of all values, sum of all first digits and sum of all last digits.Time taken to calculate amounts is measured.
Drawing a graph: It may be possible to draw each point in a separate thread, depending on the implementation. However, care must be taken to ensure that the threads do not interfere with each other and the final graph is accurate.
"""

