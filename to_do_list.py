import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager - To-Do List")
        self.master.geometry("600x500")
        self.master.configure(bg="#2C3E50")  # Background color
        
        # Title label
        self.title_label = tk.Label(master, text="Task Manager", font=("Helvetica", 18, "bold"), fg="#F7DC6F", bg="#2C3E50")
        self.title_label.pack(pady=10)
        
        # Description label
        self.description_label = tk.Label(master, text="Manage your tasks easily: Add, Edit, Delete, and Mark tasks as complete.", 
                                          font=("Helvetica", 12), fg="#D5DBDB", bg="#2C3E50")
        self.description_label.pack(pady=5)
        
        # Task Entry field
        self.task_entry = tk.Entry(master, font=("Helvetica", 14), bg="#34495E", fg="#F7DC6F", insertbackground="#F7DC6F")
        self.task_entry.pack(pady=5)
        
        # Buttons for task operations
        self.add_button = tk.Button(master, text="Add Task", font=("Helvetica", 12, "bold"), bg="#1ABC9C", fg="white", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.delete_button = tk.Button(master, text="Delete Task", font=("Helvetica", 12, "bold"), bg="#E74C3C", fg="white", command=self.delete_task)
        self.delete_button.pack(pady=5)
        
        self.complete_button = tk.Button(master, text="Mark as Complete", font=("Helvetica", 12, "bold"), bg="#5DADE2", fg="white", command=self.complete_task)
        self.complete_button.pack(pady=5)
        
        # Task List display with scrollbar
        self.task_listbox = tk.Listbox(master, font=("Helvetica", 12), bg="#1C2833", fg="#F7DC6F", height=10, selectbackground="#5DADE2")
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.task_listbox)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        # Message label for status updates
        self.message_label = tk.Label(master, text="", font=("Helvetica", 12), fg="#F7DC6F", bg="#2C3E50")
        self.message_label.pack(pady=5)
        
        # Task list (for storing tasks in memory)
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.message_label.config(text="Task added successfully.")
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
    
    def delete_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            self.tasks.remove(selected_task)
            self.update_task_list()
            self.message_label.config(text="Task deleted successfully.")
        except:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
    
    def complete_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            index = self.tasks.index(selected_task)
            self.tasks[index] = selected_task + " (Completed)"
            self.update_task_list()
            self.message_label.config(text="Task marked as complete.")
        except:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Running the To-Do List Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
