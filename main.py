# Import functions from task_manager.task_utils package
None
from task_manager.task_utils import *
from task_manager import task_utils

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            try:
                add_task(title, description, due_date)
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            if not task_utils.tasks:
                print("There are no tasks.")
                continue

            view_pending_tasks()

            try:
                index = int(input("Enter task number to mark as complete: "))
                mark_task_as_complete(index - 1)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            progress = calculate_progress()
            print(f"Task Progress: {progress:.2f}%")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
