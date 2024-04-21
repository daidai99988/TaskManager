# task.py

class Task:
    def __init__(self, title, description, assignee=None):
        self.title = title
        self.description = description
        self.assignee = assignee
        self.completed = False

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_assignee(self):
        return self.assignee

    def set_assignee(self, assignee):
        self.assignee = assignee

    def is_completed(self):
        return self.completed

    def mark_completed(self):
        self.completed = True
