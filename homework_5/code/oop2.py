import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """An own exception to raise it when the deadline comes around"""
    pass


class Person:
    """Simulates a usual Person. A parent class to Student and Homework class"""

    def __init__(self, last_name, first_name) -> None:
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    """Represents a typical homework which can be given to the student"""

    def __init__(self, text, deadline) -> None:
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        """Checks whether the homework is still active (the deadline has not yet passed) """
        return datetime.datetime.now() < self.created + self.deadline


class Student(Person):
    """A representation of the typical student, which can do homework"""

    def do_homework(self, homework, solution):
        if not homework.is_active():
            raise DeadlineError('You are late')
        return HomeworkResult(self, homework, solution)


class Teacher(Person):
    """A representation of the typical teacher which can give a homework to students"""
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text, deadline):
        """Creates an object of Homework class"""
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_result):
        """Chechs whether the homework is done correctly"""
        max_length_solution = 5
        if len(homework_result.solution) > max_length_solution:
            cls.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        """Reset homeworks"""
        if homework is None:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework, None)


class HomeworkResult:
    """Represents a Homework result"""

    def __init__(self, author, homework, solution):
        if not isinstance(homework, Homework):
            raise TypeError('You have given an object that is not a Homework')
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()
