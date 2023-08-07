import unittest
from io import StringIO
from unittest.mock import patch
from hello_world import print_hello_world

class TestHelloWorld(unittest.TestCase):
    """
    Test cases for the print_hello_world function.
    """

    def test_print_hello_world(self):
        """
        Test whether the print_hello_world function prints 'Hello, World!' to the console.
        """
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            print_hello_world()
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
