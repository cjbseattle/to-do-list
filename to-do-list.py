import os

TODO_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file into a list."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_tasks(tasks):
    """Save all tasks to the file."""
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    """Display the current list of tasks."""
    if not tasks:
        print("\n✅ No tasks found — you're all caught up!\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"  {i}. {task}")
        print()

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"➕ Added: '{task}'")
    else:
        print("⚠️  Task cannot be empty.")

def remove_task(tasks):
    """Remove a task by its number."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️  Removed: '{removed}'")
        else:
            print("⚠️  Invalid task number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")

def clear_tasks(tasks):
    """Delete all tasks."""
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == "y":
        tasks.clear()
        save_tasks(tasks)
        print("🧹 All tasks cleared.")
    else:
        print("❌ Cancelled.")

def main():
    """Main menu loop."""
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Clear all tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            clear_tasks(tasks)
        elif choice == "5":
            print("👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("⚠️  Invalid choice, please try again.")

if __name__ == "__main__":
    main()
