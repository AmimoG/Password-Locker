import unittest
from  user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Collins","Kariuki","collins@gmail.com",)
    def test1(self):
        self.assertEqual(self.new_user.f_name,"Collins")
        self.assertEqual(self.new_user.m_name,"Kariuki")
        self.assertEqual(self.new_user.e_mail,"collins@gmail.com")
    def test_save_user(self):
        self.new_user.save_user()
