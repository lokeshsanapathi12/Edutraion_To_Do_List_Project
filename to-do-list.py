import tkinter as tk
from tkinter import messagebox

incomplete_tasks = []
complete_tasks = []

def refresh_listbox():
    to_do_listbox.delete(0, tk.END)
    for index, task in enumerate(incomplete_tasks):
        to_do_listbox.insert(tk.END, f"{index + 1}) {task}")

def add_task():
    task = task_entry.get()
    if not task.strip():
        messagebox.showwarning("Warning", "Enter a task!")
        return
    incomplete_tasks.append(task)
    refresh_listbox()
    task_entry.delete(0, tk.END)

def update_task():
    try:
        task_index = to_do_listbox.curselection()[0]
        task = incomplete_tasks[task_index]
        task_label.config(text="Update Task:")
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task)

        def submit_update():
            new_task = task_entry.get()
            if not new_task.strip():
                messagebox.showwarning("Warning", "Enter a task!")
                return
            incomplete_tasks[task_index] = new_task
            refresh_listbox()
            task_entry.delete(0, tk.END)
            task_label.config(text="Enter Task:")
            add_button.config(text="Add Task", command=add_task)

        add_button.config(text="Submit", command=submit_update)
    except:
        messagebox.showwarning("Warning", "Select a task to update!")

def delete_task():
    try:
        task_index = to_do_listbox.curselection()[0]
        del incomplete_tasks[task_index]
        refresh_listbox()
        messagebox.showinfo("Success", "Task deleted.")
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_done():
    try:
        task_index = to_do_listbox.curselection()[0]
        task = incomplete_tasks.pop(task_index)
        complete_tasks.append(task)
        refresh_listbox()
        done_listbox.insert(tk.END, task)
        messagebox.showinfo("Success", "Task marked as done.")
    except:
        messagebox.showwarning("Warning", "Select a task to mark as done!")

# -------- UI Setup --------

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")
root.configure(bg="white")

# Title
title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="white")
title_label.pack(pady=10)

# Task Entry
task_frame = tk.Frame(root, bg="white")
task_frame.pack(pady=10)

task_label = tk.Label(task_frame, text="Enter Task:", font=("Arial", 11), bg="white")
task_label.pack(side=tk.LEFT, padx=5)

task_entry = tk.Entry(task_frame, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(task_frame, text="Add Task", width=10, command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

# Action Buttons
action_frame = tk.Frame(root, bg="white")
action_frame.pack(pady=5)

tk.Button(action_frame, text="Update Task", width=15, command=update_task).pack(side=tk.LEFT, padx=5)
tk.Button(action_frame, text="Delete Task", width=15, command=delete_task).pack(side=tk.LEFT, padx=5)
tk.Button(action_frame, text="Mark As Done", width=15, command=mark_done).pack(side=tk.LEFT, padx=5)

# Incomplete Tasks
tk.Label(root, text="Incomplete Tasks:", font=("Arial", 12, "bold"), bg="white").pack(pady=(20, 5), anchor="w", padx=20)

todo_frame = tk.Frame(root)
todo_frame.pack(padx=20, pady=5, fill=tk.X)

to_do_listbox = tk.Listbox(todo_frame, width=65, height=8)
to_do_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar1 = tk.Scrollbar(todo_frame, command=to_do_listbox.yview)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
to_do_listbox.config(yscrollcommand=scrollbar1.set)

# Completed Tasks
tk.Label(root, text="Completed Tasks:", font=("Arial", 12, "bold"), bg="white").pack(pady=(20, 5), anchor="w", padx=20)

done_frame = tk.Frame(root)
done_frame.pack(padx=20, pady=5, fill=tk.X)

done_listbox = tk.Listbox(done_frame, width=65, height=8)
done_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar2 = tk.Scrollbar(done_frame, command=done_listbox.yview)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
done_listbox.config(yscrollcommand=scrollbar2.set)

# Exit Button
tk.Button(root, text="Exit", command=root.destroy, width=60).pack(pady=20)

root.mainloop()