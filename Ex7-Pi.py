import threading
import random
points_inside = 0

def compute_pi():
    global points_inside
    trials_per_batch = 1000000
    num_batches = int(input("Enter number of batches: "))
    for i in range(num_batches):
        for j in range(trials_per_batch):
            x = random.random()
            y = random.random()
            if x*x + y*y < 1:
                points_inside += 1
        pi_estimate = 4 * points_inside / (i * trials_per_batch + trials_per_batch)
        print("Real value of Pi: 3.14...")
        print("Calculated value of Pi: ", pi_estimate)
        print("Number of attempts: ", i * trials_per_batch + trials_per_batch)
compute_thread = threading.Thread(target=compute_pi)
input("Press enter to start the calculation...")
compute_thread.start()

input("Press enter to stop the calculation...")

compute_thread.join()

# print final result

pi_estimate = 4 * points_inside / (num_batches * trials_per_batch)

print("Real value of Pi: 3.14...")

print("Calculated value of Pi: ", pi_estimate)

print("Number of attempts: ", num_batches * trials_per_batch)

