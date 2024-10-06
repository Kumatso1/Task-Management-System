from file_manager import FileManager
from task import Task
from admin import Admin
from user import User


class TaskManager:
    def __init__(self, tasks_file='tasks.json', users_file='users.json'):

        """
        Initializes the TaskManager object.

        Args:
            tasks_file (str, optional): The filename for storing tasks data.
            Defaults to 'tasks.json'.
            users_file (str, optional): The filename for storing users data.
            Defaults to 'users.json'.
        """
        self.file_manager = FileManager(tasks_file, users_file)
        self.tasks = [self.dict_to_task(task) for task in
                      self.file_manager.read_data(tasks_file)]
        self.users = self.file_manager.read_data(users_file)

    def dict_to_task(self, task_dict):

        """
        Converts a dictionary containing task data (id, name, start_time,
        end_time) to a Task object.

        Args:
            task_dict (dict): A dictionary representing a task.

        Returns:
            Task: A Task object created from the dictionary.
        """
        return Task(
            task_dict['id'],
            task_dict['name'],
            task_dict['start_time'],
            task_dict['end_time']
        )

    def has_admin(self):

        """
        Checks if there is at least one admin user present in the system.

        Returns:
            bool: True if there's an admin user, False otherwise.
        """
        return any(user['role'] == 'admin' for user in self.users)

    def create_user(self, username, password, role='user'):

        """
        Creates a new user with the specified username, password,
        and role (admin or user).

        Args:
            username (str): The username for the new user.
            password (str): The password for the new user.
            role (str, optional):The role for the new user ('admin' or 'user').
            Defaults to 'user' role since the admin role is only created if no
            admin exists.

        Returns:
            bool: True if the user is created successfully,
            False otherwise (if username already exists).
        """
        if any(user['username'] == username for user in self.users):
            return False
        self.users.append({'username': username, 'password': password,
                           'role': role})
        self.file_manager.write_data(self.users, self.file_manager.users_file)
        return True

    def login(self, username, password):

        """
        Authenticates a user based on the provided username and password.

        If successful, returns an Admin object if the user is an admin,
        otherwise returns a User object. If login fails, returns None.

        Args:
            username (str): The username for login.
            password (str): The password for login.

        Returns:
            Admin/User/None: An Admin object if the user is admin,
            a User object otherwise, or None on failed login.
        """
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                if user['role'] == 'admin':
                    return Admin(username, self.tasks)
                return User(username, self.tasks)
        return None

    def update_user_details(self, old_username, new_username, new_password):

        """
        Updates the details of an existing user.

        Args:
            old_username (str): The current username of the user.
            new_username (str): The new username for the user.
            new_password (str): The new password for the user.

        Returns:
            bool: True if the user details are updated successfully,
            False otherwise (user not found).
        """
        for user in self.users:
            if user['username'] == old_username:
                user['username'] = new_username
                user['password'] = new_password
                self.file_manager.write_data(self.users,
                                             self.file_manager.users_file)
                return True
        return False

    def delete_user(self, username):

        """
        Deletes a user by username.

        Args:
            username (str): The username of the user to be deleted.

        Returns:
            bool: True if the user is deleted successfully,
            False otherwise (user not found).
        """

        if username in self.users:
            del self.users[username]
            return True
        return False

    def clear_tasks(self):

        """
        Clears all tasks from the system.

        Returns:
            bool: True after clearing the tasks.
        """
        self.tasks = []
        self.file_manager.write_data(self.tasks, self.file_manager.tasks_file)
        return True

    def add_task(self, task):

        """
        Adds a new task to the system.

        Args:
            task (Task): The task to be added.

        Returns:
            bool: True after adding the task.
        """
        # Generate a unique task ID
        max_id = max((task.id for task in self.tasks), default=0)
        task.id = max_id + 1
        self.tasks.append(task)
        self.file_manager.write_data([task.__dict__ for task in self.tasks],
                                     self.file_manager.tasks_file)
        return True

    def update_task(self, task_id, name, start_time, end_time):

        """
        Updates an existing task.

        Args:
            task_id (int): The ID of the task to be updated.
            name (str): The new name for the task.
            start_time (str): The new start time for the task.
            end_time (str): The new end time for the task.

        Returns:
            bool: True if the task is updated successfully,
            False otherwise (task not found).
        """
        for task in self.tasks:
            if task.id == task_id:
                task.name = name
                task.start_time = start_time
                task.end_time = end_time
                self.file_manager.write_data([task.__dict__ for task in
                                             self.tasks],
                                             self.file_manager.tasks_file)
                return True
        return False

    def delete_task(self, task_id):

        """
        Deletes a task by ID.

        Args:
            task_id (int): The ID of the task to be deleted.

        Returns:
            bool: True after deleting the task.
        """

        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.rearrange_task_ids()
        self.file_manager.write_data([task.__dict__ for task in self.tasks],
                                     self.file_manager.tasks_file)
        return True

    def rearrange_task_ids(self):
        for i, task in enumerate(self.tasks):
            task.id = i + 1
        self.file_manager.write_data([task.__dict__ for task in self.tasks],
                                     self.file_manager.tasks_file)
