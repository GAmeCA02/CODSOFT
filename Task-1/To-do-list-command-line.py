import json
import os

class ToDoList:
    def __init__(self, filename="todo.json"):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task
            self.save_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()

    def mark_task_as_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            self.save_tasks()

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} [{status}]")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("\n2. Update Task")
        print("\n3. Delete Task")
        print("\n4. Mark Task as Done")
        print("\n5. List Tasks")
        print("\n6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.list_tasks()
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == "3":
            todo_list.list_tasks()
            task_index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "4":
            todo_list.list_tasks()
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            todo_list.mark_task_as_done(task_index)
        elif choice == "5":
            todo_list.list_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

