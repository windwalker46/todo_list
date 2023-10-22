import sqlite3
import datetime

# Initialize SQLite database
def initialize_database():
    # Connect to the database (it will create 'todo_list.db' if it doesn't exist)
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    
    # Create tasks table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'not done',
        priority TEXT NOT NULL,
        due_date DATE NOT NULL
    )
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

# Function to add a task to the database
def add_task_to_db(description, priority, due_date):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO tasks (description, priority, due_date)
    VALUES (?, ?, ?)
    ''', (description, priority, due_date))
    
    conn.commit()
    conn.close()

# Function to fetch all tasks from the database
def fetch_all_tasks_from_db():
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, description, status, priority, due_date FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def mark_task_as_done_in_db(task_id):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE tasks SET status = "done" WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def delete_task_from_db(task_id):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
