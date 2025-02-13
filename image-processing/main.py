import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps, ImageEnhance
from scipy.ndimage import gaussian_filter
import numpy as np

def upload_image():
    global current_image, original_image
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    if file_path:
        try:
            # Open the selected image
            original_image = Image.open(file_path)
            current_image = original_image.resize((250, 250))  # Resize image to fit the canvas if necessary
            image_tk = ImageTk.PhotoImage(current_image)
            
            # Display image on the canvas
            canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
            canvas.image = image_tk  # Keep a reference to the image
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")
    else:
        messagebox.showinfo("Info", "No file selected")

# Function to apply noise reduction using Gaussian filter
def reduce_noise():
    global current_image
    if current_image:
        # Convert the image to a numpy array
        image_array = np.array(current_image)

        # Apply Gaussian filter to reduce noise
        denoised_array = gaussian_filter(image_array, sigma=1)  # Adjust sigma for more/less smoothing

        # Convert the denoised array back to an image
        denoised_image = Image.fromarray(np.uint8(denoised_array))

        # Resize to fit canvas
        denoised_image = denoised_image.resize((250, 250))

        # Convert to Tkinter compatible format
        denoised_image_tk = ImageTk.PhotoImage(denoised_image)

        # Display the denoised image on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=denoised_image_tk)
        canvas.image = denoised_image_tk
        current_image = denoised_image  # Update current image
    else:
        messagebox.showinfo("Info", "No image to apply noise reduction")


def convert_to_grayscale():
    global current_image
    if current_image:
        # Convert the image to grayscale
        grayscale_image = current_image.convert("L")  # "L" mode is for grayscale
        grayscale_image = grayscale_image.resize((250, 250))  # Resize to fit canvas

        # Convert the grayscale image to Tkinter compatible format
        grayscale_image_tk = ImageTk.PhotoImage(grayscale_image)
        
        # Display the grayscale image on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=grayscale_image_tk)
        canvas.image = grayscale_image_tk  # Keep a reference to the image
        current_image = grayscale_image  # Update current image to grayscale
    else:
        messagebox.showinfo("Info", "No image to convert")


# Function to rotate the image by 90 degrees
def rotate_image():
    global current_image
    if current_image:
        rotated_image = current_image.rotate(90, expand=True)
        rotated_image = rotated_image.resize((250, 250))  # Resize to fit canvas

        rotated_image_tk = ImageTk.PhotoImage(rotated_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=rotated_image_tk)
        canvas.image = rotated_image_tk
        current_image = rotated_image  # Update current image
    else:
        messagebox.showinfo("Info", "No image to rotate")

# Function to invert the colors of the image
def invert_image():
    global current_image
    if current_image:
        inverted_image = ImageOps.invert(current_image.convert("RGB"))  # Invert colors
        inverted_image = inverted_image.resize((250, 250))  # Resize to fit canvas

        inverted_image_tk = ImageTk.PhotoImage(inverted_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=inverted_image_tk)
        canvas.image = inverted_image_tk
        current_image = inverted_image  # Update current image
    else:
        messagebox.showinfo("Info", "No image to invert")

# Function to adjust the brightness of the image
def adjust_brightness():
    global current_image
    if current_image:
        enhancer = ImageEnhance.Brightness(current_image)
        brightened_image = enhancer.enhance(1.5)  # Increase brightness by 1.5 times
        brightened_image = brightened_image.resize((250, 250))  # Resize to fit canvas

        brightened_image_tk = ImageTk.PhotoImage(brightened_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=brightened_image_tk)
        canvas.image = brightened_image_tk
        current_image = brightened_image  # Update current image
    else:
        messagebox.showinfo("Info", "No image to adjust")



# Create the main window
root = tk.Tk()
root.title("Image Upload and Grayscale Conversion")

# Create a button to upload an image
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Create a button to convert the image to grayscale
grayscale_button = tk.Button(root, text="Convert to Grayscale", command=convert_to_grayscale)
grayscale_button.pack(pady=10)


# Create a button to rotate the image by 90 degrees
rotate_button = tk.Button(root, text="Rotate Image 90°", command=rotate_image)
rotate_button.pack(pady=10)

# Create a button to invert the colors of the image
invert_button = tk.Button(root, text="Invert Colors", command=invert_image)
invert_button.pack(pady=10)

# Create a button to adjust the brightness of the image
brightness_button = tk.Button(root, text="Increase Brightness", command=adjust_brightness)
brightness_button.pack(pady=10)

# Create a button to apply noise reduction
noise_reduction_button = tk.Button(root, text="Reduce Noise", command=reduce_noise)
noise_reduction_button.pack(pady=10)


# Create a canvas to display the image
canvas = tk.Canvas(root, width=250, height=250)
canvas.pack()

# Global variables to store the current and original images
current_image = None
original_image = None

# Start the Tkinter event loop
root.mainloop()
