import tkinter as tk
from tkinter import messagebox

# Create the main application window
app = tk.Tk()
app.title("To-Do List Application")
app.geometry("500x500")

# Task list to store tasks
tasks = []

# Function to add a new task
def add_task():
    task_text = task_entry.get()
    if task_text != "":
        tasks_listbox.insert(tk.END, task_text)
        tasks.append({"description": task_text, "completed": False})
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to mark a task as completed
def mark_as_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task_text = tasks[selected_task_index]["description"]
        if not tasks[selected_task_index]["completed"]:
            tasks[selected_task_index]["completed"] = True
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, f"{task_text} - Completed")
        else:
            messagebox.showinfo("Info", "Task is already completed.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Function to clear all tasks
def clear_all_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        tasks_listbox.delete(0, tk.END)

# Create and position widgets
title_label = tk.Label(app, text="To-Do List Application", font=("Arial", 16))
title_label.pack(pady=10)

task_entry = tk.Entry(app, width=30)
task_entry.pack(pady=5)

# Frame to hold buttons
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

mark_completed_button = tk.Button(button_frame, text="Mark as Completed", command=mark_as_completed)
mark_completed_button.grid(row=0, column=2, padx=5)

clear_button = tk.Button(button_frame, text="Clear All Tasks", command=clear_all_tasks)
clear_button.grid(row=0, column=3, padx=5)

# Listbox to display tasks with a scrollbar
tasks_listbox = tk.Listbox(app, width=50, height=10, selectmode=tk.SINGLE)
tasks_listbox.pack(pady=5)

# Adding a scrollbar to the listbox
scrollbar = tk.Scrollbar(app)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# Run the application
app.mainloop()
