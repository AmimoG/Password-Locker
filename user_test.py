import unittest
from  user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Amimo","Matete","gilbertmatete6@gmail.com",)
    def test1(self):
        self.assertEqual(self.new_user.first_name,"Amimo")
        self.assertEqual(self.new_user.middle_name,"Matete")
        self.assertEqual(self.new_user.e_mail,"gilbertmatete6@gmail.com")
    def test_save_user(self):
        self.new_user.save_user()
    def tearDown(self):
        User.userlist = []
    def test_delete_user(self):
        self.new_user.save_user()
        test_data= User("elizabeth","gatwiri","elizagatwiri@gmail.com")
        test_data.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_display_user(self):
        self.assertEqual(User.display_users(),User.user_list)    
if __name__ == '__main__':
    unittest.main()