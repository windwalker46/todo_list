# Import the datetime module for handling date inputs and operations
import datetime

# This list will store all our tasks. Each task is a dictionary.
tasks = []

# This function displays the main menu of the app to the user.
def display_menu():
    print("\nTo-Do List App:")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

# This function allows the user to add a task.
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
    
    # Create the task dictionary and add it to the global tasks list.
    task = {
        "description": task_description, 
        "status": "not done",
        "priority": priority,
        "due_date": due_date
    }
    tasks.append(task)
    print("Task added successfully!")

# This function lists all the tasks stored in the tasks list.
def list_tasks():
    if not tasks:
        print("No tasks found!")
        return
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['description']} - {task['status']} - {task['priority']} - Due on {task['due_date']}")

# This function allows the user to mark a specified task as done.
def mark_task_as_done():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        tasks[task_number - 1]["status"] = "done"
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number!")

# This function allows the user to delete a specified task.
def delete_task():
    list_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        del tasks[task_number - 1]
        print("Task deleted!")
    except (ValueError, IndexError):
        print("Invalid task number!")

# This is the main driver function that manages the user's input and calls the appropriate functions.
def main():
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
