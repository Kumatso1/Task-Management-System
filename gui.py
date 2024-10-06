from tkinter import *
from tkinter import Button, Label, Entry, Text, END
import tkinter as tk
from tkinter import messagebox
from task_manager import TaskManager
from admin import Admin
from task import Task
import re

"""
    This file implements graphical user interface. The graphical user
    interface has buttons which allows a user
    to create account,login,view tasks, and change login details.
    The graphical user interface also has buttons that allows admin to
    create account add the first account on this application with username
    and password, login to view tasks, add tasks, update tasks,delete tasks,
    clear all tasks, update user details, view users, delete users.
"""



def initialize_files(tasks_file='tasks.json', users_file='users.json'):
     """
    Initializes the JSON files used to store tasks and users.
    If the files don't exist, it creates them with an empty list.

    Args:
        tasks_file (str, optional): The name of the file to store tasks data.
        Defaults to 'tasks.json'.
        users_file (str, optional): The name of the file to store users data.
        Defaults to 'users.json'.
        This function initializes the JSON files used to store tasks and users.
     If the files don't exist, it creates them with an empty list.
     """
    # Import the necessary modules
     import json
     import os

    # Check if tasks file exists, create it if not
     if not os.path.exists(tasks_file):
        # Create the tasks file with an empty list
         with open(tasks_file, 'w') as file:
             json.dump([], file)

    # Check if users file exists, create it if not
     if not os.path.exists(users_file):
        # Create the users file with an empty list
         with open(users_file, 'w') as file:
             json.dump([], file)



initialize_files()


def main():

    """
      This function is the main function of the program.
      It initializes the task manager, creates the main window,
      and calls the function to display the login screen.
    """

    task_manager = TaskManager()

    root = tk.Tk()
    root.title("                                                                                                                    TASK MANAGEMENT SYSTEM ")# Add the blank space
    root.geometry("900x450")  # Set a fixed window size
    root.config(bg="#98a189")

    def show_login_screen():

        """
            This function clears the window and displays the login screen.
            It checks if an admin account exists,
            and displays appropriate options.
        """
        clear_window()    # Calling clear function to clear the window

        if task_manager.has_admin():

            # This function checks if the admin account has already been
            # created or not.If not the it takes the user to a window to create
            # an account with admin privileges before
            # any other acount can be created.
            Label(root, text="Username:",
                  bg="gold").grid(row=0, column=0, padx=10, pady=(10, 5))
            username_entry = Entry(root, bg="#42daf5")
            username_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

            Label(root, text="Password:", bg="gold").grid(row=3, column=0)
            password_entry = Entry(root, bg="#42daf5", show="*")
            password_entry.grid(row=3, column=1, padx=10, pady=(10, 5))

            Button(root, text="Login", bg="blue",
                   command=lambda: login(username_entry.get(),
                                         password_entry.get()
                                         )).grid(row=5, column=0, padx=10,
                                                 pady=(10, 5), columnspan=3)
            Button(root, text="Create Account", bg="#42f581",
                   command=show_create_account_screen).grid(row=7, column=0,
                                                            columnspan=3)
        else:
            Label(root, text="Create Admin Account"
                  ).grid(row=0, column=0, padx=10, pady=(10, 5), columnspan=2)
            show_create_admin_account_screen()

    def show_create_account_screen():
        # This function clears the window and displays
        # the screen for creating a new user account.
        clear_window()

        Label(root, text="Create Account", bg="#42f581"
              ).grid(row=0, column=0, padx=10, pady=(10, 5), columnspan=2)

        Label(root, text="Username:",
              bg="gold").grid(row=1, column=0, padx=10, pady=(10, 5))
        username_entry = Entry(root, bg="#42daf5")
        username_entry.grid(row=1, column=1, padx=10, pady=(10, 5))

        Label(root, text="Password:", bg="gold").grid(row=2, column=0)
        password_entry = Entry(root, show="*", bg="#42daf5")
        password_entry.grid(row=2, column=1)

        Label(root, text="Re-type Password:",
              bg="gold").grid(row=3, column=0, padx=10, pady=(10, 5))
        retype_password_entry = Entry(root, show="*", bg="#42daf5")
        retype_password_entry.grid(row=3, column=1, padx=10, pady=(10, ))

        Button(root, text="Create Account",  bg="#42f581",
               command=lambda: create_account(username_entry.get(),
                                              password_entry.get(),
                                              retype_password_entry.get()
                                              )).grid(row=4, column=0,
                                                      columnspan=2, padx=10,
                                                      pady=(10, 5))
        Button(root, text="Back", bg="brown",
               command=lambda: show_login_screen()).grid(row=5, column=0,
                                                         columnspan=6)

    def show_create_admin_account_screen():

        # This function displays window asking a user to create
        # admin if there is no admin already

        Label(root, text="Username:",
              bg="gold").grid(row=1, column=0, padx=10, pady=(10, 5))
        username_entry = Entry(root, bg="#42daf5")
        username_entry.grid(row=1, column=1)

        Label(root, text="Password:",
              bg="gold").grid(row=2, column=0, padx=10, pady=(10, 5))
        password_entry = Entry(root, show="*", bg="#42daf5")
        password_entry.grid(row=2, column=1, padx=10, pady=(10, 5))

        Label(root, text="Re-type Password:", bg="gold"
              ).grid(row=3, column=0, padx=10, pady=(10, 5))
        retype_password_entry = Entry(root, show="*", bg="#42daf5")
        retype_password_entry.grid(row=3, column=1, padx=10, pady=(10, 5))

        Button(root, text="Create Admin Account",
               bg="#42f581", command=lambda: create_admin_account
               (username_entry.get(), password_entry.get(),
                retype_password_entry.get())).grid(row=4, column=0,
                                                   columnspan=2)

    def create_account(username, password, retype_password):

        """
        This function creates a new user account.
        It checks if the password and re-typed password match,
        and if the username already exists.
        """

        if password != retype_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if not task_manager.create_user(username, password):
            messagebox.showerror("Error", "Username already exists.")
        else:
            messagebox.showinfo("Success", "Account created successfully.")
            show_login_screen()

    def create_admin_account(username, password, retype_password):

        """
        This function creates a new admin account.
        It checks if the password and re-typed password match,
        and if the admin username already exists.
        """

        if password != retype_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if not task_manager.create_user(username, password, role='admin'):
            messagebox.showerror("Error", "Admin username already exists.")
        else:
            messagebox.showinfo("Success",
                                "Admin account created successfully.")
            show_login_screen()

    def login(username, password):

        """
        This function handles user login.
        It checks if the username and password are valid, and directs the user
        to the appropriate dashboard based on the role.
        """

        user = task_manager.login(username, password)
        if user is None:
            messagebox.showerror("Error", "Invalid username or password.")
        else:
            if isinstance(user, Admin):
                show_admin_dashboard(user)
            else:
                show_user_dashboard(user)

    def show_user_dashboard(user):
        # This function displays the user dashboard.

        clear_window()
        Label(root, text=f"""Welcome,  {user.username}!"""
              ).grid(row=0, column=0, padx=10,
                     pady=(10, 5), columnspan=6)

        def view_tasks():

            # This function displays the user's tasks.

            clear_window()
            tasks_display = Text(root, bg="#9c6f30", fg="white")
            tasks_display.grid(row=1, column=0,
                               columnspan=6, padx=10, pady=(10, 5))
            for task in user.view_tasks():
                # Characters are above the required maximum line character
                # limit to prevent distorting the task structure
                tasks_display.insert(END, f"D: {task.id} -{task.name} - {task.start_time} to {task.end_time}\n")        
            Button(root, text="Back",
                   bg="brown", command=lambda: show_user_dashboard(user)
                   ).grid(row=2, column=0, columnspan=6)

        Button(root, text="View Tasks", bg="#3285a8", command=view_tasks
               ).grid(row=3, column=0, padx=10, pady=(10, 5))
        Button(root, text="Change Login Details", bg="#3285a8",
               command=lambda: show_change_login_details_screen(user)
               ).grid(row=3, column=1, padx=10, pady=(10, 5))
        Button(root, text="Logout", bg="#a8327d", command=show_login_screen
               ).grid(row=3, column=2, padx=10, pady=(10, 5))

    def show_admin_dashboard(admin):

        # This function displays the admin dashboard.
        clear_window()
        Label(root, text=f"Welcome, {admin.username}!"
              ).grid(row=0, column=0, padx=10, pady=(15, 5), columnspan=6)

        def view_tasks():

            # This function displays tasks on the admin dashboard

            clear_window()
            tasks_display = Text(root, bg="#9c6f30", fg="white")
            tasks_display.grid(row=1, column=0, columnspan=6)
            for task in admin.view_tasks():
                # Characters are above the required maximum line character
                # limit to prevent distorting the task structure
                tasks_display.insert(END, f"ID: {task.id} - {task.name} - {task.start_time} to {task.end_time}\n")
            Button(root, text="Back", bg="brown",
                   command=lambda: show_admin_dashboard(admin)
                   ).grid(row=2, column=0, columnspan=6)

        def add_task():

            """
            Displays the screen for adding a new task.
            """
            clear_window()

            Label(root, text="Task Name:",
                  bg="gold").grid(row=0, column=0, padx=10, pady=(10, 5))
            task_name_entry = Entry(root, bg="#42daf5")
            task_name_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

            Label(root, text="Start Time (YYYY-MM-DD HH:MM)",
                  bg="gold").grid(row=1, column=0, padx=10, pady=(10, 5))
            start_time_entry = Entry(root, bg="#42daf5")
            start_time_entry.grid(row=1, column=1, padx=10, pady=(10, 5))

            Label(root, text="End Time (YYYY-MM-DD HH:MM)",
                  bg="gold").grid(row=2, column=0, padx=10, pady=(10, 5))
            end_time_entry = Entry(root, bg="#42daf5")
            end_time_entry.grid(row=2, column=1, padx=10, pady=(10, 5))

            Button(root, text="Add Task", bg="#309c94",
                   command=lambda: add_task_action(task_name_entry.get(),
                                                   start_time_entry.get(),
                                                   end_time_entry.get()
                                                   )).grid(row=3, column=0,
                                                           padx=10,
                                                           pady=(10, 5),
                                                           columnspan=2)
            Button(root, text="Back", bg="brown",
                   command=lambda: show_admin_dashboard(admin)
                   ).grid(row=4, column=0, columnspan=6,
                          padx=10, pady=(10, 5))

        def add_task_action(name, start_time, end_time):
            """"
                Adds the task to the list after validation.
            """
            if not name or not start_time or not end_time:
                messagebox.showerror("Error", "All fields are required.")
                return
            time_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}'
            if not re.match(time_pattern,
                            start_time) or not re.match(time_pattern,
                                                        end_time):
                messagebox.showerror("Error", """Invalid time format.
                                     Use YYYY-MM-DD HH:MM.""")
                return
            # ID will be set in add_task
            task = Task(0, name, start_time, end_time)
            task_manager.add_task(task)
            messagebox.showinfo("Success", "Task added successfully.")
            show_admin_dashboard(admin)

        def update_task():

            """
            Displays the screen for updating an existing task.
            """
            clear_window()

            Label(root, text="Task ID:",
                  bg="gold").grid(row=0, column=0, padx=10, pady=(10, 5))
            task_id_entry = Entry(root, bg="#42daf5")
            task_id_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

            Label(root, text="Task Name:",
                  bg="gold").grid(row=1, column=0, padx=10, pady=(10, 5))
            task_name_entry = Entry(root, bg="#42daf5")
            task_name_entry.grid(row=1, column=1, padx=10, pady=(10, 5))

            Label(root, text="Start Time (YYYY-MM-DD HH:MM)",
                  bg="gold").grid(row=2, column=0, padx=10, pady=(10, 5))
            start_time_entry = Entry(root, bg="#42daf5")
            start_time_entry.grid(row=2, column=1, padx=10, pady=(10, 5))

            Label(root, text="End Time (YYYY-MM-DD HH:MM)",
                  bg="gold").grid(row=3, column=0, padx=10, pady=(10, 5))
            end_time_entry = Entry(root, bg="#42daf5")
            end_time_entry.grid(row=3, column=1, padx=10, pady=(10, 5))

            Button(root, text="Update Task",
                   bg="#309c94", command=lambda: update_task_action
                   (task_id_entry.get(), task_name_entry.get(),
                    start_time_entry.get(), end_time_entry.get()
                    )).grid(row=4, column=0, padx=10, pady=(10, 5),
                            columnspan=2)
            Button(root, text="Back", bg="brown",
                   command=lambda: show_admin_dashboard(admin)
                   ).grid(row=5, column=0, columnspan=6, padx=10, pady=(10, 5))

        def update_task_action(task_id, name, start_time, end_time):

            """
                Updates the task in the list after validation.
            """
            if not task_id or not name or not start_time or not end_time:
                messagebox.showerror("Error", "All fields are required.")
                return
            time_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}'
            # Characters are above the required maximum line character
            # limit to prevent distorting the task structure
            if not re.match(time_pattern, start_time) or not re.match(time_pattern, end_time):
                messagebox.showerror("Error", """Invalid time format.
                                     Use YYYY-MM-DD HH:MM.""")
                return
            try:
                task_id = int(task_id)
            except ValueError:
                messagebox.showerror("Error", "Task ID must be a number.")
                return

            if task_manager.update_task(task_id, name, start_time, end_time):
                messagebox.showinfo("Success", "Task updated successfully.")
                show_admin_dashboard(admin)
            else:
                messagebox.showerror("Error", "Task not found.")

        def delete_task():

            """
                Displays the screen for deleting an existing task.
            """
            clear_window()

            Label(root, text="Task ID:",
                  bg="gold").grid(row=0, column=0, padx=10, pady=(10, 5))
            task_id_entry = Entry(root, bg="#42daf5")
            task_id_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

            Button(root, text="Delete Task", bg="#309c94",
                   command=lambda: delete_task_action(task_id_entry.get())
                   ).grid(row=1, column=0, columnspan=2)
            Button(root, text="Back", bg="brown",
                   command=lambda: show_admin_dashboard(admin)
                   ).grid(row=2, column=0, columnspan=6, padx=10,
                          pady=(10, 5))

        def delete_task_action(task_id):

            """
                Deletes the task from the list after validation.
            """
            if not task_id:
                messagebox.showerror("Error", "Task ID is required.")
                return

            try:
                task_id = int(task_id)
            except ValueError:
                messagebox.showerror("Error", "Task ID must be a number.")
                return

            if task_manager.delete_task(task_id):
                messagebox.showinfo("Success", "Task deleted successfully.")
                show_admin_dashboard(admin)
            else:
                messagebox.showerror("Error", "Task not found.")

        def view_users():
            """
                Displays the list of users.
            """

            clear_window()
            users_display = Text(root, bg="#9c6f30")
            users_display.grid(row=1, column=0, columnspan=6)
            for user in task_manager.users:
                # Characters are above the required maximum line character
                # limit to prevent distorting the task structure
                users_display.insert(END, f"Username: {user['username']} - Role: {user['role']}\n")
            Button(root, text="Back", bg="brown",
                   command=lambda: show_admin_dashboard(admin)
                   ).grid(row=2, column=0, columnspan=6, padx=10,
                          pady=(10, 5))

        def update_user_details():
            """
                Displays the screen for updating user details.
            """

            clear_window()

            Label(root, text="Old Username:",
                  bg="gold").grid(row=0, column=0, padx=10, pady=(10, 5))
            old_username_entry = Entry(root, bg="#42daf5")
            old_username_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

            Label(root, text="New Username:",
                  bg="gold").grid(row=1, column=0, padx=10, pady=(10, 5))
            new_username_entry = Entry(root, bg="#42daf5")
            new_username_entry.grid(row=1, column=1,
                                    padx=10, pady=(10, 5))

            Label(root, text="New Password:",
                  bg="gold").grid(row=2, column=0, padx=10, pady=(10, 5))
            new_password_entry = Entry(root, show="*", bg="#42daf5")
            new_password_entry.grid(row=2, column=1, padx=10, pady=(10, 5))

            Button(root, text="Update User", bg="#309c94",
                   command=lambda: update_user_details_action(
                       old_username_entry.get(), new_username_entry.get(),
                       new_password_entry.get()
                       )).grid(row=3, column=0, padx=10, pady=(10, 5),
                               columnspan=2)
            Button(root, text="Back",
                   bg="brown", command=lambda: show_admin_dashboard(admin)
                   ).grid(row=4, column=0, padx=10, pady=(10, 5), columnspan=6)

        def update_user_details_action(old_username,
                                       new_username, new_password):

            """
               Updates user details in the list after validation.
            """
            if not old_username or not new_username or not new_password:
                messagebox.showerror("Error", "All fields are required.")
                return

            if task_manager.update_user_details(old_username,
                                                new_username, new_password):
                messagebox.showinfo("Success",
                                    "User details updated successfully.")
                show_admin_dashboard(admin)
            else:
                messagebox.showerror("Error", "User not found.")

        def delete_user():

            """
            Displays the screen for deleting a user.
            """
            clear_window()

            Label(root, text="Username:",
                  bg="gold").grid(row=0, column=0, padx=10, pady=(10, 5))
            username_entry = Entry(root, bg="#42daf5")
            username_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

            Button(root, text="Delete User",
                   command=lambda: delete_user_action(username_entry.get())
                   ).grid(row=1, column=0,  padx=10, pady=(10, 5),
                          columnspan=2)
            Button(root, text="Back",
                   bg="brown", command=lambda: show_admin_dashboard(admin)
                   ).grid(row=2, column=0, columnspan=6, padx=10, pady=(10, 5))

        def delete_user_action(username):

            """
                Deletes the user from the list after validation.
            """
            if not username:
                messagebox.showerror("Error", "Username is required.")
                return

            if task_manager.delete_user(username):
                messagebox.showinfo("Success", "User deleted successfully.")
                show_admin_dashboard(admin)
            else:
                messagebox.showerror("Error", "User not found.")

        def clear_tasks():

            """
                Clears all tasks after user confirmation.
            """
            if messagebox.askyesno("Confirm",
                                   "Are you sure you want to clear tasks?"):
                task_manager.clear_tasks()
                messagebox.showinfo("Success",
                                    "All tasks cleared successfully.")
                show_admin_dashboard(admin)

        # Position buttons in the same row (row 3) with proper spacing
        Button(root, text="View Tasks", bg="#3285a8", command=view_tasks
               ).grid(row=3, column=0, padx=10, pady=(10, 5))
        Button(root, text="Add Task", bg="#3285a8", command=add_task
               ).grid(row=3, column=1,  padx=10, pady=(10, 5))
        Button(root, text="Update Task", bg="#3285a8", command=update_task
               ).grid(row=3, column=2, padx=10, pady=(10, 5))
        Button(root, text="Delete Task", bg="#a83a32", command=delete_task
               ).grid(row=3, column=3,  padx=10, pady=(10, 5))
        Button(root, text="View Users", bg="#3285a8", command=view_users
               ).grid(row=3, column=4,  padx=10, pady=(10, 5))
        Button(root, text="Update User Details", bg="#3285a8",
               command=update_user_details).grid(row=3, column=5,
                                                 padx=10, pady=(10, 5))
        Button(root, text="Delete User", bg="#a83a32", command=delete_user
               ).grid(row=3, column=6,  padx=10, pady=(10, 5))
        Button(root, text="Clear All Tasks", bg="#ed0739",
               command=clear_tasks).grid(row=3, column=7,
                                         padx=10, pady=(10, 5))
        Button(root, text="Logout", bg="#a8327d", command=show_login_screen
               ).grid(row=3, column=8, padx=10, pady=(10, 5))

    def show_change_login_details_screen(user):
        clear_window()

        Label(root, text="Old Username:",
              bg="gold").grid(row=0, column=0, padx=10, pady=(10, 5))
        old_username_entry = Entry(root, bg="#42daf5")
        old_username_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

        Label(root, text="New Username:",
              bg="gold").grid(row=1, column=0, padx=10, pady=(10, 5))
        new_username_entry = Entry(root, bg="#42daf5")
        new_username_entry.grid(row=1, column=1, padx=10, pady=(10, 5))

        Label(root, text="New Password:",
              bg="gold").grid(row=2, column=0, padx=10, pady=(10, 5))
        new_password_entry = Entry(root, show="*", bg="#42daf5")
        new_password_entry.grid(row=2, column=1, padx=10, pady=(10, 5))

        Button(root, text="Update Details",
               bg="#309c94", command=lambda: update_login_details_action
               (user, old_username_entry.get(),
                new_username_entry.get(), new_password_entry.get()
                )).grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 5))
        Button(root, text="Back", bg="brown",
               command=lambda: show_user_dashboard(user)
               ).grid(row=4, column=0, columnspan=6)

    def update_login_details_action(user, old_username, new_username,
                                    new_password):
        if not old_username or not new_username or not new_password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if task_manager.update_user_details(old_username, new_username,
                                            new_password):
            messagebox.showinfo("Success",
                                "User details updated successfully.")
            if isinstance(user, Admin):
                show_admin_dashboard(user)
            else:
                show_user_dashboard(user)
        else:
            messagebox.showerror("Error", "User not found.")

    def clear_window():
        for widget in root.winfo_children():
            widget.destroy()

    show_login_screen()
    root.mainloop()


if __name__ == "__main__":
    main()
