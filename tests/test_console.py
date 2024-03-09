#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        with patch('builtins.input', side_effect=['quit']):
            self.console.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '(hbnb) ')

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        with patch('builtins.input', side_effect=['EOF']):
            self.console.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), '\n')

        # Write similar tests for other commands like create, show, destroy, update, etc.

if __name__ == '__main__':
    unittest.main()

