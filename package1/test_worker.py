from unittest import TestCase, mock
from unittest.mock import patch
from package1.Worker import Worker

class TestWorker(TestCase):
    def setUp(self):
        self.adam = Worker("yossi", "shlomi", 1995, 11, 12, "rambam", "il")

    def tearDown(self):
        pass

    # @mock.patch('package1.Worker.Worker.full_name', return_value="dolev")
    # def test_full_name(self, mock_fullname):
    #     self.assertEqual(self.adam.full_name(), "dolev")
    #
    # @mock.patch('package1.Worker.Worker.age', return_value=42)
    # def test_age(self, mock_age):
    #     self.assertEqual(self.adam.age(), 42)
    #
    #
    #
    # def test_days_to_birthday(self):
    #     pass
    #
    # def test_greet(self):
    #     pass

    def test_location(self):
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'success'
            res = self.adam.location()
            self.assertEqual(res, 'success')

