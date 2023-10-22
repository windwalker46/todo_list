# Import the datetime module for handling date inputs and operations
import datetime
from database_operations import fetch_all_tasks_from_db, initialize_database, add_task_to_db, mark_task_as_done_in_db, delete_task_from_db
# This list will store all our tasks. Each task is a dictionary.

# This function displays the main menu of the app to the user.
def display_menu():
    print("\nTo-Do List App:")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    # Get the task description from the user.
    task_description = input("Enter the task description: ")
    
    # Input and validate the priority level.
    while True:
        priority = input("Enter the task priority (High/Medium/Low): ").lower()
        if priority in ["high", "medium", "low"]:
            break
        else:
            print("Invalid priority! Please choose between High, Medium, or Low.")
    
    # Input and validate the due date.
    while True:
        due_date_str = input("Enter the due date (YYYY-MM-DD): ")
        try:
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format! Please enter in the format YYYY-MM-DD.")
    
    # Add the task to the database.
    add_task_to_db(task_description, priority, due_date)
    print("Task added successfully!")

def list_tasks():
    tasks = fetch_all_tasks_from_db()
    if not tasks:
        print("No tasks found!")
        return
    for index, task in enumerate(tasks):
        task_id, description, status, priority, due_date = task
        print(f"{index + 1}. {description} - {status} - {priority} - {due_date}")

    return tasks

def mark_task_as_done():
    tasks = list_tasks()
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        task_id, _, _, _, _ = tasks[task_number - 1]
        mark_task_as_done_in_db(task_id)
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def delete_task():
    tasks = list_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        task_id, _, _, _, _ = tasks[task_number - 1]
        delete_task_from_db(task_id)
        print("Task deleted!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def main():
    # Initialize the database
    initialize_database()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_task_as_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


# This line ensures that the main() function is called only when this script is run directly, not when imported elsewhere.
if __name__ == "__main__":
    main()
