import tkinter as tk
from tkinter import messagebox, font as tkFont, ttk
import json
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Maximize window for Linux/other platforms
        try:
            self.root.state('zoomed')  # Windows
        except:
            self.root.attributes('-fullscreen', True)  # Linux and others

        self.filename = "todo.json"
        self.load_tasks()

        # Custom Fonts
        self.header_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.task_font = tkFont.Font(family="Helvetica", size=14)

        # Create the side panel frame
        side_panel = tk.Frame(root, bg="#007acc", width=200)
        side_panel.pack(side=tk.LEFT, fill=tk.Y)

        # Header
        header = tk.Label(root, text="My To-Do List", bg="#007acc", fg="white", pady=10, font=self.header_font)
        header.pack(fill=tk.X)

        # Task Frame
        task_frame = tk.Frame(root, bg="#f0f0f0")
        task_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Task List with Scrollbar
        self.tasks_canvas = tk.Canvas(task_frame, bg="#f0f0f0")
        self.tasks_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(task_frame, orient="vertical", command=self.tasks_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tasks_frame = tk.Frame(self.tasks_canvas, bg="#f0f0f0")
        self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="nw")

        self.tasks_frame.bind("<Configure>", lambda e: self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all")))
        self.tasks_canvas.configure(yscrollcommand=scrollbar.set)

        # Entry Field
        self.entry = tk.Entry(side_panel, width=20, font=self.task_font, bg="#f7f7f7", fg="#333")
        self.entry.pack(pady=20)

        # Buttons in Side Panel
        add_button = tk.Button(side_panel, text="Add Task", command=self.add_task, width=15, bg="#28a745", fg="white", font=self.task_font)
        add_button.pack(pady=10)

        update_button = tk.Button(side_panel, text="Update Task", command=self.update_task, width=15, bg="#007acc", fg="white", font=self.task_font)
        update_button.pack(pady=10)

        delete_button = tk.Button(side_panel, text="Delete Task", command=self.delete_task, width=15, bg="#dc3545", fg="white", font=self.task_font)
        delete_button.pack(pady=10)

        mark_done_button = tk.Button(side_panel, text="Mark as Done", command=self.mark_as_done, width=15, bg="#ffc107", fg="white", font=self.task_font)
        mark_done_button.pack(pady=10)

        # Initialize tasks
        self.task_checkboxes = []
        self.display_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.save_tasks()
            self.entry.delete(0, tk.END)
            self.display_tasks()

    def update_task(self):
        selected_task = self.get_selected_task_index()
        if selected_task is not None:
            new_task = self.entry.get()
            if new_task:
                self.tasks[selected_task]["task"] = new_task
                self.save_tasks()
                self.entry.delete(0, tk.END)
                self.display_tasks()

    def delete_task(self):
        selected_task = self.get_selected_task_index()
        if selected_task is not None:
            self.tasks.pop(selected_task)
            self.save_tasks()
            self.display_tasks()

    def mark_as_done(self):
        selected_task = self.get_selected_task_index()
        if selected_task is not None:
            self.tasks[selected_task]["done"] = True
            self.save_tasks()
            self.display_tasks()

    def get_selected_task_index(self):
        for idx, var in enumerate(self.task_checkboxes):
            if var.get():
                return idx
        return None

    def display_tasks(self):
        # Clear existing checkboxes
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        self.task_checkboxes = []
        for idx, task in enumerate(self.tasks):
            var = tk.IntVar(value=1 if task["done"] else 0)
            checkbox = tk.Checkbutton(self.tasks_frame, text=task["task"], variable=var, onvalue=1, offvalue=0, font=self.task_font, bg="#f0f0f0")
            checkbox.pack(anchor="w", pady=2)
            self.task_checkboxes.append(var)

        self.tasks_frame.update_idletasks()
        self.tasks_canvas.config(scrollregion=self.tasks_canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

