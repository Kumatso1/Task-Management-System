class Task:

    """
    Represents a task with an ID, name, start time, and end time.

    Attributes:
        id (int): Unique identifier for the task.
        name (str): Name of the task.
        start_time (datetime): The datetime object representing the start
        time of the task.end_time (datetime): The datetime object
        representing the end time of the task.
    """
    def __init__(self, id, name, start_time, end_time):
        self.id = id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):

        """
        Returns a string representation of the task in the format:
        "Task ID: {id}, Name: {name}, Start: {start_time}, End: {end_time}"

        Returns:
            str: String representation of the task.
        """

        return f"""Task ID: {self.id}, Name: {self.name},
        Start: {self.start_time}, End: {self.end_time}"""
