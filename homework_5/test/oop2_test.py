import unittest
from datetime import datetime
from code.oop2 import DeadlineError, Homework, HomeworkResult, Student, Teacher


class TestOop2(unittest.TestCase):
    def setUp(self):
        self.homework = Homework('Math homework', 3)
        self.student = Student('Bond', 'James')
        self.teacher = Teacher('Smith', 'John')

    def test_is_active(self):
        self.assertTrue(self.homework.is_active())

    def test_is_not_active(self):
        self.homework.created = datetime.now() - self.homework.deadline - datetime(days=1)
        self.assertFalse(self.homework.is_active())

    def test_do_homework_on_time(self):
        homework_result = self.student.do_homework(
            self.homework, 'some solution')
        self.assertIsInstance(homework_result, HomeworkResult)

    def test_do_homework_late(self):
        self.homework.created = datetime.now() - self.homework.deadline - datetime(days=1)
        with self.assertRaises(DeadlineError):
            self.student.do_homework(self.homework, 'some solution')

    def test_check_homework(self):
        homework_result = HomeworkResult(
            self.student, self.homework, 'some solution')
        self.assertTrue(self.teacher.check_homework(homework_result))

    def test_check_homework_long_solution(self):
        long_solution = 'a' * 6
        homework_result = HomeworkResult(
            self.student, self.homework, long_solution)
        self.assertFalse(self.teacher.check_homework(homework_result))

    def test_homework_done(self):
        homework_result = HomeworkResult(
            self.student, self.homework, 'some solution')
        self.teacher.check_homework(homework_result)
        self.assertIn(homework_result,
                      self.teacher.homework_done[self.homework])

    def test_reset_all_results(self):
        homework_result = HomeworkResult(
            self.student, self.homework, 'some solution')
        self.teacher.check_homework(homework_result)
        self.teacher.reset_results()
        self.assertFalse(self.teacher.homework_done)

    def test_reset_spec_result(self):
        homework_result = HomeworkResult(
            self.student, self.homework, 'some solution')
        self.teacher.check_homework(homework_result)
        self.teacher.reset_results(self.homework)
        self.assertNotIn(
            homework_result, self.teacher.homework_done[self.homework])


if __name__ == '__main__':
    unittest.main()
