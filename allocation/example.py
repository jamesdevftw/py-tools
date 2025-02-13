import pulp

# Create a linear programming problem (Maximization)
prob = pulp.LpProblem("Satellite Resource Allocation", pulp.LpMaximize)

# Define available resources (Fuel, CPU, Bandwidth)
fuel_available = 100  # In percentage
cpu_available = 100   # In percentage
bandwidth_available = 100  # In Mbps

# Define tasks with their resource requirements
tasks = {
    "Task1": {"fuel": 20, "cpu": 25, "bandwidth": 30, "priority": 3},
    "Task2": {"fuel": 10, "cpu": 15, "bandwidth": 10, "priority": 5},
    "Task3": {"fuel": 30, "cpu": 20, "bandwidth": 50, "priority": 2},
    "Task4": {"fuel": 15, "cpu": 10, "bandwidth": 20, "priority": 4}
}

# Define a binary decision variable for each task (0 = not selected, 1 = selected)
task_vars = pulp.LpVariable.dicts("Task", tasks.keys(), cat="Binary")

# Objective: Maximize the number of tasks completed (sum of selected tasks)
prob += pulp.lpSum([task_vars[task] for task in tasks]), "Maximize tasks"

# Constraints: Resources should not exceed available resources
prob += pulp.lpSum([tasks[task]["fuel"] * task_vars[task] for task in tasks]) <= fuel_available, "Fuel constraint"
prob += pulp.lpSum([tasks[task]["cpu"] * task_vars[task] for task in tasks]) <= cpu_available, "CPU constraint"
prob += pulp.lpSum([tasks[task]["bandwidth"] * task_vars[task] for task in tasks]) <= bandwidth_available, "Bandwidth constraint"

# Solve the problem
prob.solve()

# Print the results
print(f"Status: {pulp.LpStatus[prob.status]}")
for task in tasks:
    if pulp.value(task_vars[task]) == 1:
        print(f"Task '{task}' is selected.")

# Show remaining resources
remaining_fuel = fuel_available - sum([tasks[task]["fuel"] * pulp.value(task_vars[task]) for task in tasks])
remaining_cpu = cpu_available - sum([tasks[task]["cpu"] * pulp.value(task_vars[task]) for task in tasks])
remaining_bandwidth = bandwidth_available - sum([tasks[task]["bandwidth"] * pulp.value(task_vars[task]) for task in tasks])

print(f"Remaining Fuel: {remaining_fuel}%")
print(f"Remaining CPU: {remaining_cpu}%")
print(f"Remaining Bandwidth: {remaining_bandwidth} Mbps")
