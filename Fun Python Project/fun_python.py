import tkinter as tk
import random

def on_button_click():
    friend_name = name_entry.get()
    if friend_name.strip():
        output_label.config(text=f"Hello, {friend_name}! Nice to see you!", fg="green")
        error_label.config(text="")  # Clear any previous error message
    else:
        output_label.config(text="")
        error_label.config(text="Error: Please enter a valid name.", fg="red")

def simulate_internet_speed():
    progress_label.config(text="Testing Internet Speed...", fg="blue")
    update_progress(1)

def update_progress(i):
    if i <= 100:
        progress_label.config(text=f"Loading... {i}%", fg="blue")
        window.after(50, update_progress, i + 1)  # Schedule next update
    else:
        progress_label.config(text="Internet Speed Test Complete!", fg="green")
        display_name_and_nickname()

def generate_funny_nickname():
    nicknames = [
        "Captain Giggles",
        "Silly Goose",
        "Professor Chuckles",
        "Sir Snort-a-lot",
        "Lady Laughsalot",
        "Wacky Wombat",
        "Giggle Monster",
        "Goofy Giraffe",
        "Cheeky Chimp",
        "Banana Pants"
    ]
    return random.choice(nicknames)

def display_name_and_nickname():
    friend_name = name_entry.get()
    if friend_name.strip():
        nickname = generate_funny_nickname()
        nickname_label.config(text=f"{friend_name}'s funny nickname is: {nickname}", fg="purple")
    else:
        nickname_label.config(text="Please enter a name to get a nickname.", fg="red")

# Create the main window
window = tk.Tk()
window.title("Friendly Greeting App")
window.geometry("500x500")
window.config(bg="#f0f0f0")  # Set background color

# Create and place input box
name_label = tk.Label(window, text="Enter your friend's name:", font=("Helvetica", 12), bg="#f0f0f0")
name_label.pack(pady=10)

name_entry = tk.Entry(window, width=30, font=("Helvetica", 12))
name_entry.pack(pady=10)

# Create and place a button
greet_button = tk.Button(window, text="Greet", command=on_button_click, font=("Helvetica", 12), bg="#4CAF50", fg="white")
greet_button.pack(pady=10)

# Create and place output label
output_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#f0f0f0")
output_label.pack(pady=20)

# Create and place error message label
error_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f0f0f0")
error_label.pack(pady=5)

# Create and place progress label
progress_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#f0f0f0")
progress_label.pack(pady=10)

# Create and place a button to simulate internet speed
test_button = tk.Button(window, text="Test Internet Speed", command=simulate_internet_speed, font=("Helvetica", 12), bg="#2196F3", fg="white")
test_button.pack(pady=10)

# Create and place nickname label
nickname_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#f0f0f0")
nickname_label.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
