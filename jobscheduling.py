def job_scheduling(deadlines, profits):
    # Combine the deadlines and profits into a list of (deadline, profit) tuples
    jobs = list(zip(deadlines, profits))

    # Sort the jobs in descending order of profits
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Find the maximum deadline among all jobs
    max_deadline = max(deadlines)

    # Create a list to keep track of the scheduled jobs
    schedule = [None] * max_deadline

    # Schedule the jobs
    total_profit = 0
    for deadline, profit in jobs:
        # Find the latest available slot before the deadline
        slot = deadline - 1
        while slot >= 0 and schedule[slot] is not None:
            slot -= 1

        # If a slot is available, schedule the job
        if slot >= 0:
            schedule[slot] = profit
            total_profit += profit

    return total_profit


# Take input from the user
num_jobs = int(input("Enter the number of jobs: "))
deadlines = []
profits = []

for i in range(num_jobs):
    deadline = int(input(f"Enter the deadline for job {i + 1}: "))
    profit = int(input(f"Enter the profit for job {i + 1}: "))
    deadlines.append(deadline)
    profits.append(profit)

# Call the job scheduling function
max_profit = job_scheduling(deadlines, profits)

# Print the maximum profit
print("Maximum Profit:", max_profit)
