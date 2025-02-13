import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Global list to store sentences and their corresponding labels
phrases = []
labels = []

# Predefined positive and negative sentences for pretraining
positive_phrases = [
    "I love this!", 
    "This is amazing!", 
    "Great job!", 
    "So happy!", 
    "Wonderful experience!",
    "I feel fantastic today!", 
    "This is excellent!", 
    "I am so excited!", 
    "Everything is perfect!", 
    "Absolutely wonderful!"
]

negative_phrases = [
    "I hate this.", 
    "This is terrible.", 
    "So bad.", 
    "Worst experience.", 
    "I am disappointed.", 
    "This is awful.", 
    "I don't like this at all.", 
    "Very poor quality.", 
    "I regret this.", 
    "Such a bad decision."
]

# Function to handle "Positive" button click
def add_positive():
    phrase = input_box.get()
    if phrase:
        phrases.append(phrase)
        labels.append(1)  # 1 for Positive
        input_box.delete(0, tk.END)  # Clear input box
    else:
        messagebox.showwarning("Input Error", "Please enter a phrase.")

# Function to handle "Negative" button click
def add_negative():
    phrase = input_box.get()
    if phrase:
        phrases.append(phrase)
        labels.append(0)  # 0 for Negative
        input_box.delete(0, tk.END)  # Clear input box
    else:
        messagebox.showwarning("Input Error", "Please enter a phrase.")

# Function to train and classify the sentences
def train_and_classify():
    if len(phrases) < 2:
        messagebox.showwarning("Data Error", "Please enter at least two phrases.")
        return

    # Convert phrases into a bag of words representation
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(phrases)
    y = labels

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Clear both output boxes before displaying results
    positive_output_box.delete(1.0, tk.END)
    negative_output_box.delete(1.0, tk.END)
    
    # Display accuracy
    positive_output_box.insert(tk.END, f"Model trained. Accuracy: {accuracy:.2f}\n\n")

    # Classify each phrase and add them to appropriate output box
    for phrase in phrases:
        vectorized_input = vectorizer.transform([phrase])
        prediction = model.predict(vectorized_input)
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        
        if sentiment == "Positive":
            positive_output_box.insert(tk.END, f"'{phrase}' -> {sentiment}\n")
        else:
            negative_output_box.insert(tk.END, f"'{phrase}' -> {sentiment}\n")

# Add the predefined phrases to the dataset for pretraining
phrases.extend(positive_phrases)
labels.extend([1] * len(positive_phrases))  # 1 for positive

phrases.extend(negative_phrases)
labels.extend([0] * len(negative_phrases))  # 0 for negative

# Set up the main window
root = tk.Tk()
root.title("Sentiment Analysis")

# Create the input box for the user to enter phrases
input_box = tk.Entry(root, width=50)
input_box.pack(pady=10)

# Create the "Positive" button
positive_button = tk.Button(root, text="Positive", command=add_positive)
positive_button.pack(pady=5)

# Create the "Negative" button
negative_button = tk.Button(root, text="Negative", command=add_negative)
negative_button.pack(pady=5)

# Create the "Enter" button to train and classify
enter_button = tk.Button(root, text="Enter", command=train_and_classify)
enter_button.pack(pady=10)

# Create two text boxes for output: one for positive and one for negative
positive_output_box = tk.Text(root, width=60, height=10)
positive_output_box.pack(pady=5)
positive_output_box.insert(tk.END, "Positive Sentiments:\n\n")

negative_output_box = tk.Text(root, width=60, height=10)
negative_output_box.pack(pady=5)
negative_output_box.insert(tk.END, "Negative Sentiments:\n\n")

# Start the Tkinter event loop
root.mainloop()
