# task_manager.py

from task import Task
from user import User

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.users = []

    def create_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def assign_task(self, task, assignee):
        if isinstance(assignee, User):
            task.set_assignee(assignee)
        else:
            raise ValueError("Invalid assignee")

    def complete_task(self, task):
        task.mark_completed()

    def get_tasks(self):
        return self.tasks

    def add_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def get_users(self):
        return self.users
