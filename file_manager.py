import json
import os


class FileManager:
    """
    A class for managing tasks and user data stored in JSON files.

    This class provides methods for reading and writing data to JSON files.
    """
    def __init__(self, tasks_file='tasks.json', users_file='users.json'):

        """
        Initializes the FileManager object with file paths.

        Args:
            tasks_file (str, optional): Path to the file containing task data.
            Defaults to 'tasks.json'.
            users_file (str, optional): Path to the file containing user data.
            Defaults to 'users.json'.
        """
        self.tasks_file = tasks_file
        self.users_file = users_file

    def read_data(self, file_path):

        """
        Reads data from a JSON file.

        This method attempts to read data from the specified file path.
        If the file does not exist,
        an empty list is returned. Any errors encountered during file opening
        or JSON decoding are caught
        and an empty list is returned in those cases as well.

        Args:
            file_path (str): Path to the JSON file to read.

        Returns:
            list: The data loaded from the JSON file,
            or an empty list on errors.
        """
        if not os.path.exists(file_path):
            return []
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_data(self, data, file_path):

        """
        Writes data to a JSON file.

        This method writes the provided data to
        the specified file path in JSON format.
        The data is indented for readability.

        Args:
            data (list): The data to write to the JSON file.
            file_path (str): Path to the JSON file to write to.
        """
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
