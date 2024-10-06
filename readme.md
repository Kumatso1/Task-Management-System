## Task Manager Application

## Note:
This task management was locally developed on  my pc and then used to GitHub repository after its completion.

## Description
This task manager application is designed based on modular design principles. It manages tasks that need to be achieved at a particular time and within a specific duration. There are two types of users interacting with the system: a user and an admin.

## sers: 
Users can create an account and log in to view available tasks and update their login details.
## Admins: 
Admins can create an admin account, log in, view tasks, add tasks, update tasks, delete tasks, clear tasks, update user details, and delete users.

## Improvements Implemented
This application includes several improvements:

Users can create accounts and log in after the account has been successfully created.
Users can also change their login details like username and password.
Admins have additional functionalities, such as deleting users who are no longer part of the team.
Utilizes JSON files to store data instead of Python .txt files for improved data access.
Developed using Tkinter to provide an interactive GUI.

## How to Run This Application
Download the Task Management System Folder:

Ensure you have all necessary files in the folder, including task_manager.py, file_manager.py, admin.py, task.py, user.py, gui.py, tasks.json, users.json, and any other required modules.
Prepare the Environment:

Delete existing JSON files (tasks.json and users.json) if you want to start with a clean slate. This will remove any existing stored data. You can delete users.json file only if you just want to be allowed to create admin account.

# Run the Application:
Execute the gui.py file to launch the application. You can do this by running the command python gui.py in your terminal or by opening and running the file in an IDE.

# Admin and User Operations:

# Admin Users:
Only admin users can perform CRUD (Create, Read, Update, Delete) operations on users.json and tasks.json.
Admins can log in to view, add, update, delete, and clear tasks. They can also update user details and delete users.
# Standard Users:
Standard users can create an account and log in to view tasks and update their user details.
Standard users are not allowed to perform CRUD operations on tasks or user data.

# Testing 
The test file for this application is tests.py 
To  perform testing, type 'python manage.py test' on the terminal after navigationg to the project and press enter to run the tests.

# User Guide
# Creating an Admin Account
Run the application and create admin account. You can only be allow to create admin account 
if there is no existing admin account, so to be able to create admin account, delete contents of users.json file. This will ensure that the first account created is an admin account after that no any other admin account can be created for security reason.
Enter the desired username and password. Re-type the password and click on create admin account button.
Log in using the newly created admin account to manage tasks and users.

# Creating a User Account
Run the application and create a new user account.
Enter the desired username and password.Re-type the password and click on create account button.
Log in using the newly created user account to view tasks and update your login details.

# Admin Functionalities
View Tasks: Log in as an admin and choose the option to view all tasks.
Add Task: Log in as an admin and choose the option to add a new task.
Update Task: Log in as an admin, view the list of tasks, and choose a task to update.
Delete Task: Log in as an admin, view the list of tasks, and choose a task to delete.
Clear Tasks: Log in as an admin and choose the option to clear all tasks.
Update User Details: Log in as an admin, view the list of users, and choose a user to update their details.
Delete User: Log in as an admin, view the list of users, and choose a user to delete.

# User Functionalities
View Tasks: Log in as a user and choose the option to view all tasks.
Update User Details: Log in as a user and choose the option to update your username and password.

# Additional Notes
Ensure you have the required dependencies installed to run the application. You can typically install dependencies using pip install -r requirements.txt if a requirements.txt file is provided.
This application uses Tkinter for the GUI, so ensure that Tkinter is installed and properly configured on your system.