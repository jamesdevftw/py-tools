import tkinter as tk
from tkinter import messagebox
import pulp

# Function to run the optimization with PuLP
def run_optimization():
    try:
        # Retrieve user input for resources and tasks
        fuel_available = float(fuel_entry.get())
        cpu_available = float(cpu_entry.get())
        bandwidth_available = float(bandwidth_entry.get())

        # Define tasks with resource requirements (you can expand this as needed)
        tasks = {
            "Security patch test": {"fuel": 20, "cpu": 25, "bandwidth": 30, "priority": 3},
            "Rotate solar panel - Alpha": {"fuel": 10, "cpu": 15, "bandwidth": 10, "priority": 5},
            "Daily data upload": {"fuel": 30, "cpu": 20, "bandwidth": 50, "priority": 2},
            "Critical systems test": {"fuel": 15, "cpu": 10, "bandwidth": 20, "priority": 4}
        }

        # Create a linear programming problem (Maximization)
        prob = pulp.LpProblem("Satellite Resource Allocation", pulp.LpMaximize)

        # Define binary decision variable for each task
        task_vars = pulp.LpVariable.dicts("Task", tasks.keys(), cat="Binary")

        # Objective: Maximize the number of tasks completed (sum of selected tasks)
        prob += pulp.lpSum([task_vars[task] for task in tasks]), "Maximize tasks"

        # Constraints: Resources should not exceed available resources
        prob += pulp.lpSum([tasks[task]["fuel"] * task_vars[task] for task in tasks]) <= fuel_available, "Fuel constraint"
        prob += pulp.lpSum([tasks[task]["cpu"] * task_vars[task] for task in tasks]) <= cpu_available, "CPU constraint"
        prob += pulp.lpSum([tasks[task]["bandwidth"] * task_vars[task] for task in tasks]) <= bandwidth_available, "Bandwidth constraint"

        #Task dependencies
        #prob += task_vars["Task3"] <= task_vars["Task1"], "Dependency: Task3 depends on Task1"


        # Solve the problem
        prob.solve()

        # Collect results and remaining resources
        selected_tasks = []
        remaining_fuel = fuel_available - sum([tasks[task]["fuel"] * pulp.value(task_vars[task]) for task in tasks])
        remaining_cpu = cpu_available - sum([tasks[task]["cpu"] * pulp.value(task_vars[task]) for task in tasks])
        remaining_bandwidth = bandwidth_available - sum([tasks[task]["bandwidth"] * pulp.value(task_vars[task]) for task in tasks])

        for task in tasks:
            if pulp.value(task_vars[task]) == 1:
                selected_tasks.append(task)

        # Show the results in the Tkinter window
        result_text = f"Status: {pulp.LpStatus[prob.status]}\n"
        result_text += "Selected Tasks:\n"
        for task in selected_tasks:
            result_text += f"- {task}\n"

        result_text += f"\nRemaining Fuel: {remaining_fuel}%\n"
        result_text += f"Remaining CPU: {remaining_cpu}%\n"
        result_text += f"Remaining Bandwidth: {remaining_bandwidth} Mbps"

        # Display the results in the result label
        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for the resources!")

# Create the Tkinter window
root = tk.Tk()
root.title("Satellite Resource Allocation")
root.geometry("500x500")

# Create labels and entries for user input
tk.Label(root, text="Fuel Available (%)").pack(pady=5)
fuel_entry = tk.Entry(root)
fuel_entry.pack(pady=5)

tk.Label(root, text="CPU Available (%)").pack(pady=5)
cpu_entry = tk.Entry(root)
cpu_entry.pack(pady=5)

tk.Label(root, text="Bandwidth Available (Mbps)").pack(pady=5)
bandwidth_entry = tk.Entry(root)
bandwidth_entry.pack(pady=5)

# Button to run optimization
run_button = tk.Button(root, text="Run Optimization", command=run_optimization)
run_button.pack(pady=20)

# Label to display the optimization results
result_label = tk.Label(root, text="Optimization results will appear here.", justify=tk.LEFT)
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
