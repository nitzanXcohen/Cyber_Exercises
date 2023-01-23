import threading

import random

# global variable to keep track of number of points inside the circle

points_inside = 0

def compute_pi():

    global points_inside

    # number of trials per batch

    trials_per_batch = 1000000

    # get number of batches from user

    num_batches = int(input("Enter number of batches: "))

    for i in range(num_batches):

        for j in range(trials_per_batch):

            x = random.random()

            y = random.random()

            if x*x + y*y < 1:

                points_inside += 1

        # print result after each batch

        pi_estimate = 4 * points_inside / (i * trials_per_batch + trials_per_batch)

        print("Real value of Pi: 3.14...")

        print("Calculated value of Pi: ", pi_estimate)

        print("Number of attempts: ", i * trials_per_batch + trials_per_batch)

# create a thread to run the computation

compute_thread = threading.Thread(target=compute_pi)

# wait for user input to start the calculation

input("Press enter to start the calculation...")

compute_thread.start()

# wait for user input to stop the calculation

input("Press enter to stop the calculation...")

compute_thread.join()

# print final result

pi_estimate = 4 * points_inside / (num_batches * trials_per_batch)

print("Real value of Pi: 3.14...")

print("Calculated value of Pi: ", pi_estimate)

print("Number of attempts: ", num_batches * trials_per_batch)

