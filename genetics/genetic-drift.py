import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt

# Function to simulate genetic drift
def simulate_genetic_drift():
    try:
        # Get input values for population size and number of generations
        population_size = int(population_size_entry.get())
        generations = int(generations_entry.get())
        allele_a_freq = float(allele_a_entry.get())

        if population_size <= 0 or generations <= 0 or not (0 <= allele_a_freq <= 1):
            raise ValueError("Invalid input. Ensure values are correct.")

    except ValueError as e:
        messagebox.showerror("Input Error", f"Error: {str(e)}")
        return

    # Initialize population with allele frequencies
    population = [random.choices(['A', 'a'], [allele_a_freq, 1-allele_a_freq], k=2) for _ in range(population_size)]
    
    allele_a_frequencies = []

    # Simulate over generations
    for gen in range(generations):
        # Count the number of 'A' alleles in the population
        num_a_alleles = sum(1 for individual in population for allele in individual if allele == 'A')
        
        # Calculate the frequency of 'A' allele in the population
        allele_a_freq = num_a_alleles / (2 * population_size)
        allele_a_frequencies.append(allele_a_freq)
        
        # Create new generation based on genetic drift
        population = [random.choices(['A', 'a'], [allele_a_freq, 1-allele_a_freq], k=2) for _ in range(population_size)]

    # Plot allele frequency over generations
    plt.plot(range(generations), allele_a_frequencies, marker='o')
    plt.xlabel('Generations')
    plt.ylabel('Frequency of allele A')
    plt.title('Genetic Drift Simulation')
    plt.grid(True)
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Genetic Drift Simulator")

# Set window size
root.geometry("400x350")

# Labels and Entry fields for input
tk.Label(root, text="Population Size:").pack(pady=5)
population_size_entry = tk.Entry(root)
population_size_entry.pack(pady=5)

tk.Label(root, text="Number of Generations:").pack(pady=5)
generations_entry = tk.Entry(root)
generations_entry.pack(pady=5)

tk.Label(root, text="Initial Frequency of Allele A (0-1):").pack(pady=5)
allele_a_entry = tk.Entry(root)
allele_a_entry.pack(pady=5)

# Simulate Button
simulate_button = tk.Button(root, text="Simulate Genetic Drift", command=simulate_genetic_drift)
simulate_button.pack(pady=20)

# Start Tkinter event loop
root.mainloop()
