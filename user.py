class User:
    def __init__(self, username, tasks):

        """
        Initializes a new User object.

        Args:
            username (str): The username of the user.
            tasks (list): A list of tasks associated with the user.
        """
        self.username = username
        self.tasks = tasks

    def view_tasks(self):

        """
        Returns the list of tasks associated with the user.

        Returns:
            list: The list of tasks for the user.
        """
        return self.tasks
