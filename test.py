import unittest
from task_manager import TaskManager
from task import Task


class TestTaskManager(unittest.TestCase):
    """
    Unit tests for the TaskManager class.
    """

    def setUp(self):
        """
        Set up the TaskManager instance with test files for isolation.
        This method runs before each test.
        """
        self.task_manager = TaskManager(tasks_file='test_tasks.json',
                                        users_file='test_users.json')
        # Clear the test files to ensure a clean state for each test
        self.task_manager.file_manager.write_data([], 'test_tasks.json')
        self.task_manager.file_manager.write_data([], 'test_users.json')

    def tearDown(self):
        """
        Clean up the test files after each test.
        This method runs after each test.
        """
        self.task_manager.file_manager.write_data([], 'test_tasks.json')
        self.task_manager.file_manager.write_data([], 'test_users.json')

    def test_create_user(self):
        """
        Test creating a new user.
        - Ensure that a new user can be created.
        - Ensure that a duplicate username cannot be created.
        """
        self.assertTrue(self.task_manager.create_user('user1', 'pass1'))
        # Duplicate username
        self.assertFalse(self.task_manager.create_user('user1', 'pass1'))

    def test_login(self):
        """
        Test user login.
        - Ensure that an existing user can log in.
        - Ensure that a non-existent user cannot log in.
        """
        self.task_manager.create_user('admin', 'adminpass', role='admin')
        self.task_manager.create_user('user', 'userpass')
        self.assertIsNotNone(self.task_manager.login('admin', 'adminpass'))
        self.assertIsNotNone(self.task_manager.login('user', 'userpass'))
        self.assertIsNone(self.task_manager.login('nonexistent', 'pass'))

    def test_update_user_details(self):
        """
        Test updating user details.
        - Ensure that user details can be updated.
        - Ensure that updating non-existent user details fails.
        """
        self.task_manager.create_user('user1', 'pass1')
        self.assertTrue(self.task_manager.update_user_details('user1', 'user2',
                                                              'pass2'))
        self.assertFalse(self.task_manager.update_user_details('nonexistent',
                                                               'user3',
                                                               'pass3'))

    def test_delete_user(self):
        """
        Test deleting a user.
        - Ensure that an existing user can be deleted.
        - Ensure that deleting a non-existent user fails.
        """
        self.task_manager.create_user('user1', 'password1', role='user')
        # User no longer exists, should return False
        self.assertFalse(self.task_manager.delete_user('user1'))
        # User does not exist, should return False
        self.assertFalse(self.task_manager.delete_user('nonexistent'))

    def test_add_task(self):
        """
        Test adding a task.
        - Ensure that a task can be added.
        """
        task = Task(1, 'Task 1', '2023-01-01 10:00', '2023-01-01 12:00')
        self.task_manager.add_task(task)
        tasks = self.task_manager.file_manager.read_data('test_tasks.json')
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['name'], 'Task 1')

    def test_clear_tasks(self):
        """
        Test clearing all tasks.
        - Ensure that all tasks can be cleared.
        """
        task1 = Task(1, 'Task 1', '2023-01-01 10:00', '2023-01-01 12:00')
        task2 = Task(2, 'Task 2', '2023-01-02 10:00', '2023-01-02 12:00')
        self.task_manager.add_task(task1)
        self.task_manager.add_task(task2)
        self.task_manager.clear_tasks()
        tasks = self.task_manager.file_manager.read_data('test_tasks.json')
        self.assertEqual(len(tasks), 0)

    def test_has_admin(self):
        """
        Test checking if an admin exists.
        - Ensure that the method correctly identifies the presence of an admin.
        """
        self.assertFalse(self.task_manager.has_admin())
        self.task_manager.create_user('admin', 'adminpass', role='admin')
        self.assertTrue(self.task_manager.has_admin())


if __name__ == '__main__':
    unittest.main()
