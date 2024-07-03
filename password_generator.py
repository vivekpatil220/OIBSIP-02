import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to generate the password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_chars=''):
    character_set = ''
    if use_upper:
        character_set += string.ascii_uppercase
    if use_lower:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    if not character_set:
        raise ValueError("No character types selected")

    # Exclude specified characters
    character_set = ''.join(c for c in character_set if c not in exclude_chars)

    if len(character_set) == 0:
        raise ValueError("No characters available for password generation after exclusions")

    # Generate the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    
    # Ensure at least one of each selected type
    if use_upper and not any(c.isupper() for c in password):
        password = password[:-1] + random.choice(string.ascii_uppercase)
    if use_lower and not any(c.islower() for c in password):
        password = password[:-1] + random.choice(string.ascii_lowercase)
    if use_digits and not any(c.isdigit() for c in password):
        password = password[:-1] + random.choice(string.digits)
    if use_symbols and not any(c in string.punctuation for c in password):
        password = password[:-1] + random.choice(string.punctuation)
    
    return password

# Function to handle the generation and display of the password
def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer")
        
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()
        exclude_chars = exclude_entry.get()
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_chars)
        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Function to copy the password to clipboard
def copy_to_clipboard():
    pyperclip.copy(result_var.get())
    messagebox.showinfo("Clipboard", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Advanced Password Generator")

# Create and place widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).grid(row=1, column=0, padx=10, pady=5)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).grid(row=2, column=0, padx=10, pady=5)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=3, column=0, padx=10, pady=5)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=4, column=0, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", )
copy_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Add exclude characters entry
tk.Label(root, text="Exclude Characters:").grid(row=8, column=0, padx=10, pady=10)
exclude_entry = tk.Entry(root)
exclude_entry.grid(row=8, column=1, padx=10, pady=10)

# Run the application
root.mainloop()

