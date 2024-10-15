import unittest
from io import StringIO
from unittest.mock import patch
from katas.file_exceptions import file_exceptions
import os


workdir = os.getcwd()
BASE_PATH = '../files' if workdir.endswith('test') else 'files'


class TestFileExceptions(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_file_not_found_error(self, mock_stdout):
        file_exceptions(f'{BASE_PATH}/nonexistent_file.txt')
        self.assertIn("FileNotFoundError", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.open', side_effect=PermissionError("Invalid permissions"))
    def test_handle_permission_error(self, mock_open, mock_stdout):
        file_exceptions(f'{BASE_PATH}/somefile', op='w')
        self.assertIn("PermissionError", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_is_a_directory_error(self, mock_stdout):
        file_exceptions(f'{BASE_PATH}/')
        self.assertIn("IsADirectoryError", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_file_exists_error(self, mock_stdout):
        file_exceptions(f'{BASE_PATH}/someotherfile', op='x')
        self.assertIn("FileExistsError", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.open', side_effect=OSError("OS error - failed to access disk"))
    def test_handle_os_error(self, mock_open, mock_stdout):
        file_exceptions(f'{BASE_PATH}/someotherfile')
        self.assertIn("OSError", mock_stdout.getvalue())

