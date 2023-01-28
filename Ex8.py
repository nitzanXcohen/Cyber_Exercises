import random

for i in range(10):
    with open(f"file{i}.txt", "w") as f:
        for _ in range(100_000):
            f.write(str(random.randint(1, 1000)) + "\n")
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

threads = []

for i in range(10):
    t = threading.Thread(target=create_file, args=(i,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
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
import random

with open("numbers.txt", "w") as f:
    for _ in range(100_000):
        f.write(str(random.randint(1, 1000)) + "\n")

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

t = threading.Thread(target=create_file)
t.start()
t.join()

with open("numbers.txt", "r") as f:
    numbers = [int(x) for x in f.readlines()]

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
