import unittest
from credentials import Info

class TestInfo(unittest.TestCase):
    def setUp(self):
        self.new_info =Info("amimo.matete","amimo.matete")
    def test_init(self):
        self.assertEqual(self.new_info.linkedInp,"amimo.matete")
        self.assertEqual(self.new_info.email_p,"matete.amimo")
    def test_save_info(self):
        '''
        to test if user info is saved
        '''
        self.new_info.save_info()
        self.assertEqual(len(Info.info_list),1)
    def tearDown(self):
        Info.info_list = []
    def test_delete_info(self):
        self.new_info.save_info()
        test_info = Info("amimo.matete","amimo.matete")
        test_info.save_info()
        test_info.delete_info()
        self.assertEqual(len(Info.info_list),1)

if __name__ == '__main__':
    unittest.main()
