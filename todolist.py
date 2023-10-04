class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = "Incomplete"
        print(f'Task "{task}" added successfully!')

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f'Task "{task}" removed successfully!')
        else:
            print(f'Task "{task}" not found.')

    def mark_as_complete(self, task):
        if task in self.tasks:
            self.tasks[task] = "Complete"
            print(f'Task "{task}" marked as complete!')
        else:
            print(f'Task "{task}" not found.')

    def display_tasks(self):
        print("\nTo-Do List:")
        for task, status in self.tasks.items():
            print(f'[{status}] {task}')
        print()


def main():
    todo_list = ToDoList()

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            task = input("Enter the task to mark as complete: ")
            todo_list.mark_as_complete(task)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting the To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
