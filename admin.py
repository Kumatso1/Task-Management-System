from user import User
from task import Task
""" This admin module is created to give administrative privileges to one actor who is going to be 
    responsible for adding tasks, updating tasks, deleting tasks, resetting tasks, giving administrative 
    privileges to another actor by creating admin account for him/her. Admin is also responsible for removing 
    user which will not allow such a user to login on this application again. """
class Admin(User):

    # defining admin class which utilizes User class attributes which are accessed 
    # by importing User class from user.py file. 

    def __init__(self, username, tasks):
        super().__init__(username, tasks)

    def add_task(self, task):
        # This function will allow admin to add task to the list of other task

        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks
        
