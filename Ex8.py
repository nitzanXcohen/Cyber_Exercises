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


