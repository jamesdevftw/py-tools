import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from recipe import calculate_ingredients  # Import the function

def on_calculate():
    try:
        servings = int(entry_servings.get())
        result_text.set(calculate_ingredients(servings))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of servings.")

# Create main window
root = tk.Tk()
root.title("Recipe Scaler")
root.geometry("350x250")
root.configure(bg="#f0f0f0")

# Style configuration
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Frame for input
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# User input
ttk.Label(frame, text="Enter number of servings:").grid(row=0, column=0, padx=5, pady=5)
entry_servings = ttk.Entry(frame, width=10)
entry_servings.grid(row=0, column=1, padx=5, pady=5)

# Calculate button
button_calculate = ttk.Button(root, text="Calculate", command=on_calculate)
button_calculate.pack(pady=10)

# Output result
result_text = tk.StringVar()
label_result = ttk.Label(root, textvariable=result_text, justify="left", background="#f0f0f0")
label_result.pack(pady=10)

# Run the application
root.mainloop()
