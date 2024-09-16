import tkinter as tk
from tkinter import messagebox
import os

def add_task():
    task = task_entry.get().strip()
    task_entry.delete(0, tk.END)
    
    if task:
        if task in task_list:
            messagebox.showinfo("Duplicate Task", "This task already exists.")
            return
        with open('tasklist.txt', "a") as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        listbox.insert(tk.END, task)
    else:
        messagebox.showwarning("Empty Task", "You must enter a task.")

def delete_task():
    task = listbox.get(tk.ANCHOR)
    if task:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(tk.ANCHOR)

def open_task_file():
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            task = task.strip()
            if task:
                task_list.append(task)
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        with open('tasklist.txt', 'w') as file:
            pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x605+400+100")
root.resizable(False, False)

task_list = []

# Load images
try:
    Image_icon = tk.PhotoImage(file="Image/task.png")
    TopImage = tk.PhotoImage(file="Image/topbar.png")
    dockImage = tk.PhotoImage(file="Image/dock.png")
    Delet_icon = tk.PhotoImage(file="Image/delete.png")
except tk.TclError:
    messagebox.showerror("Image Error", "Error loading images. Ensure image files are available.")

root.iconphoto(False, Image_icon)

# Top bar
tk.Label(root, image=TopImage).pack()
tk.Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)
tk.Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b").place(x=130, y=20)

# Main frame
frame = tk.Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)
task_entry = tk.Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()
tk.Button(frame, text="ADD", font="arial 20", width=6, bg="#5a95ff", fg="#fff", bd=0, command=add_task).place(x=300, y=0)

# Listbox
frame1 = tk.Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))
listbox = tk.Listbox(frame1, font=("arial", 12), width=40, height=16, bg='#32405b', fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

open_task_file()

# Delete button
tk.Button(root, image=Delet_icon, bd=0, command=delete_task).pack(side=tk.BOTTOM, pady=13)

root.mainloop()
