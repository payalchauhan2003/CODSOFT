class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        status = '[X]' if self.completed else '[ ]'
        return f'{status} {self.description}'


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks):
                print(f'{index + 1}. {task}')

    def update_task_description(self, task_index, new_description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

# Example usage
def main():
    todo_list = ToDoList()

    while True:
        print("\nCOMMANDS:")
        print("1. Add task")
        print("2. Complete task")
        print("3. List tasks")
        print("4. Update task description")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.list_tasks()
            task_index = int(input("Enter task index to complete: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            todo_list.list_tasks()
            task_index = int(input("Enter task index to update: ")) - 1
            new_description = input("Enter new description: ")
            todo_list.update_task_description(task_index, new_description)
        elif choice == '5':
            todo_list.list_tasks()
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()
