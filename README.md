# 🗂️ Task Tracking System

A lightweight, command-line based task tracking system for small teams. Built with Python, it helps manage tasks effectively without the need for heavy project management tools or external databases.

## 📌 Project Overview

This system allows users to:

- ✅ Create tasks with essential information
- 📋 View all tasks or filter by assignee/status
- ✏️ Update task status
- ❌ Delete tasks
- 🧠 Experience error-handled and user-friendly CLI interactions

## 🎓 Course Info

**COMP1002 - Advanced Python**  
**Project Date**: 23.05.2025  
**Team Members**:
- Celal Çatal - 232010020019  
- Melih Kaan Direk - 232010020015  
- Müşerref Ebru Erden - 232010020012  

## 🛠️ Technologies Used

- **Language**: Python 3.x  
- **Libraries**:
  - `json` – For data persistence
  - `datetime` – For date parsing and validation
- **Tools**:
  - CLI (Command-Line Interface)
  - Local JSON file storage (`tasks.json`)

## 📂 File Structure

```bash
tasktraking/
├── task_manager.py      # Main script for managing tasks
├── tasks.json           # Data file storing task information
└── README.md            # Project documentation
```

## ⚙️ How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/task-tracking-system.git
   cd task-tracking-system
   ```

2. **Run the Script:**
   ```bash
   python task_manager.py
   ```

> Make sure Python 3.x is installed and available in your system PATH.

## 🧩 Features

### ✅ Task Creation
- Add title, description, assignee, due date, and status.
- Validates input (e.g., empty fields and incorrect date formats).

### 📋 Task Listing & Filtering
- Display all tasks.
- Filter tasks by assignee or status.

### ✏️ Task Updating
- Update the status of a task using its index.
- Status options: `"Not Started"`, `"In Progress"`, `"Completed"`

### ❌ Task Deletion
- Remove tasks after user confirmation.
- Index validation ensures safe deletion.

### 🧠 Error Handling
- Handles invalid inputs and provides clear user prompts.
- Ensures smooth user experience through try-except blocks.

## 🧪 Sample Use

```bash
Welcome to Task Tracking System
1. Add Task
2. View Tasks
3. Filter Tasks
4. Update Task Status
5. Delete Task
6. Exit
Choose an option: _
```

## 🚧 Challenges & Solutions

| Challenge                             | Solution                                                   |
|--------------------------------------|------------------------------------------------------------|
| Invalid date formats or empty inputs | Input validation and exception handling                    |
| Data persistence without a database  | Local JSON file (`tasks.json`) used for data storage       |
| Keep the tool simple and accessible  | Pure Python + clear CLI without external libraries         |

## 🌱 Future Improvements

- 🔍 Search and sort tasks (e.g., by deadline)
- ⏰ Deadline reminders with scheduled alerts
- 🖥️ Optional GUI (Tkinter)

## 📄 License

This project is intended for educational purposes under the [MIT License](LICENSE).

---

_Designed to be simple, effective, and usable from any terminal window._

