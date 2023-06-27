class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = False

class TaskManagementSystem:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, title, description):
        task = Task(self.task_id_counter, title, description)
        self.tasks.append(task)
        self.task_id_counter += 1

    def mark_task_as_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                print(f"Task with ID {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")

    def view_task_details(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                print("Task Details:")
                print(f"ID: {task.task_id}")
                print(f"Title: {task.title}")
                print(f"Description: {task.description}")
                print(f"Status: {'Completed' if task.completed else 'Not Completed'}")
                return
        print(f"Task with ID {task_id} not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("All Tasks:")
        for task in self.tasks:
            print(f"ID: {task.task_id} | Title: {task.title} | Status: {'Completed' if task.completed else 'Not Completed'}")

# Example usage
task_system = TaskManagementSystem()

# Adding tasks
task_system.add_task("Complete Project", "Finish the project report by Friday.")
task_system.add_task("Buy Groceries", "Buy fruits, vegetables, and milk.")

# Listing all tasks
task_system.list_all_tasks()

# Viewing task details
task_system.view_task_details(1)
task_system.view_task_details(3) # Task not found

# Marking task as completed
task_system.mark_task_as_completed(2)
task_system.view_task_details(2)

# Listing all tasks again
task_system.list_all_tasks()
