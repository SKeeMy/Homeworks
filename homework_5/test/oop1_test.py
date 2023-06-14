import unittest
from datetime import datetime, timedelta
from code.oop1 import Homework, Student, Teacher


class HomeworkTest(unittest.TestCase):
    def test_is_active(self):
        hw = Homework('Test homework', 2)
        self.assertTrue(hw.is_active())
        hw.created = datetime.now() - timedelta(days=3)
        self.assertFalse(hw.is_active())


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.student = Student('Doe', 'John')

    def test_do_homework(self):
        hw = Homework('Test homework', 2)
        self.assertEqual(self.student.do_homework(hw), hw)

        hw.created = datetime.now() - timedelta(days=3)
        self.assertIsNone(self.student.do_homework(hw))


class TeacherTest(unittest.TestCase):
    def setUp(self):
        self.teacher = Teacher('Smith', 'Alice')

    def test_create_homework(self):
        hw = self.teacher.create_homework('Test homework', 2)
        self.assertIsInstance(hw, Homework)
        self.assertEqual(hw.text, 'Test homework')
        self.assertEqual(hw.deadline, timedelta(days=2))
        self.assertLessEqual(hw.created, datetime.now())


if __name__ == '__main__':
    unittest.main()
