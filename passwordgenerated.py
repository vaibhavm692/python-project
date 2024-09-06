import random
import string
import tkinter as tk

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Create the input field for password length
        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = tk.Entry(master, width=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create the checkbox for password complexity
        self.complexity_label = tk.Label(master, text="Password Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=10, pady=10)
        self.complexity_var = tk.IntVar()
        self.complexity_checkbox = tk.Checkbutton(master, text="Include special characters", variable=self.complexity_var)
        self.complexity_checkbox.grid(row=1, column=1, padx=10, pady=10)

        # Create the button to generate the password
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Create the label to display the generated password
        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10)
        self.password_display = tk.Label(master, text="")
        self.password_display.grid(row=3, column=1, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 8:
                self.password_display.config(text="Password length should be at least 8 characters.")
                return
        except ValueError:
            self.password_display.config(text="Invalid input. Please enter a number.")
            return

        all_characters = string.ascii_letters + string.digits
        if self.complexity_var.get():
            all_characters += string.punctuation

        password = ''.join(random.choice(all_characters) for i in range(length))
        self.password_display.config(text=password)

root = tk.Tk()
password_generator = PasswordGenerator(root)
root.mainloop()