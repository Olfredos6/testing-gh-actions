from unittest import TestCase
from os import path
from src.functions import get_current_path


class MyTests(TestCase):
    def test_returns_current_wroking_dir(self):
        current_file_path = path.join(path.realpath('.'), __file__)
        self.assertEqual(current_file_path, get_current_path())