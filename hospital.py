import tkinter as tk
from tkinter import messagebox

class HospitalQueueSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Queue System")

        # Priority queue: each element is a tuple (age, name)
        self.queue = []

        # UI Layout
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(pady=10)

        self.canvas = tk.Canvas(self.display_frame, width=400, height=330, bg="white", relief="solid", borderwidth=1)
        self.canvas.pack()

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        tk.Button(self.buttons_frame, text="Call Patient", command=self.call_patient, bg="red", fg="white").grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Add Patient", command=self.add_patient, bg="green", fg="white").grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Update Patient", command=self.update_patient, bg="orange", fg="black").grid(row=0, column=2, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Front", command=self.front, bg="blue", fg="white").grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Back", command=self.back, bg="purple", fg="white").grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Length", command=self.length, bg="yellow", fg="black").grid(row=1, column=2, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Is Empty?", command=self.is_empty, bg="pink", fg="black").grid(row=2, column=1, padx=5, pady=5)

        self.update_display()

    def update_display(self):
        """Update the patient display in the canvas."""
        self.canvas.delete("all")
        y = 10
        for age, name in sorted(self.queue, reverse=True):  # Sort by priority (age, descending)
            self.canvas.create_text(10, y, anchor="nw", text=f"{name}, Age: {age}", fill="black")
            y += 20

    def call_patient(self):
        """Call the patient with the highest priority."""
        if self.queue:
            patient = self.queue.pop(0)  # Remove the first patient (highest priority)
            messagebox.showinfo("Call Patient", f"Calling: {patient[1]}, Age: {patient[0]}")
            self.update_display()
        else:
            messagebox.showerror("Error", "No patients in the queue!")

    def add_patient(self):
        """Add a new patient to the queue."""
        def save_patient():
            try:
                name = name_entry.get()
                age = int(age_entry.get())
                if name and age >= 0:
                    self.queue.append((age, name))
                    self.queue.sort(reverse=True)  # Ensure queue is sorted by age (descending)
                    self.update_display()
                    add_window.destroy()
                else:
                    messagebox.showerror("Error", "Invalid input!")
            except ValueError:
                messagebox.showerror("Error", "Age must be a number!")

        add_window = tk.Toplevel(self.root)
        add_window.title("Add Patient")
        tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(add_window, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        age_entry = tk.Entry(add_window)
        age_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(add_window, text="Add", command=save_patient).grid(row=2, column=0, columnspan=2, pady=10)

    def update_patient(self):
        """Update the details of a patient in the queue."""
        def save_update():
            try:
                name = name_entry.get()
                age = int(age_entry.get())
                for i, (a, n) in enumerate(self.queue):
                    if n == name:
                        self.queue[i] = (age, name)
                        self.queue.sort(reverse=True)  # Re-sort queue
                        self.update_display()
                        update_window.destroy()
                        return
                messagebox.showerror("Error", "Patient not found!")
            except ValueError:
                messagebox.showerror("Error", "Age must be a number!")

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Patient")
        tk.Label(update_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(update_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(update_window, text="New Age:").grid(row=1, column=0, padx=5, pady=5)
        age_entry = tk.Entry(update_window)
        age_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(update_window, text="Update", command=save_update).grid(row=2, column=0, columnspan=2, pady=10)

    def front(self):
        """Show the patient with the highest priority."""
        if self.queue:
            patient = self.queue[0]
            messagebox.showinfo("Front Patient", f"Front: {patient[1]}, Age: {patient[0]}")
        else:
            messagebox.showerror("Error", "Queue is empty!")

    def back(self):
        """Show the patient with the lowest priority."""
        if self.queue:
            patient = self.queue[-1]
            messagebox.showinfo("Back Patient", f"Back: {patient[1]}, Age: {patient[0]}")
        else:
            messagebox.showerror("Error", "Queue is empty!")

    def length(self):
        """Show the number of patients in the queue."""
        messagebox.showinfo("Queue Length", f"Length: {len(self.queue)}")

    def is_empty(self):
        """Check if the queue is empty."""
        if not self.queue:
            messagebox.showinfo("Queue Status", "The queue is empty.")
        else:
            messagebox.showinfo("Queue Status", "The queue is not empty.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalQueueSystem(root)
    root.mainloop()
