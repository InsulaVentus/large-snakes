import unittest
from commandlauncher.fileparser import FileParser

ABSOLUTE_FILE_PATH = "c:/data/commands.txt"

EXPECTED_COMMANDS = {
    '1': 'dir',
    '2': 'cd ..',
    '3': 'cd c:/',
    '4': 'ping imgur.com',
    '5': 'java -version',
    '7': 'cd d:/',
    '8': 'ipconfig',
    '6': 'mvn clean install'
}


class MyTestCase(unittest.TestCase):
    def test_a_valid_file_of_commands(self):
        parser = FileParser()
        actual_commands = parser.get_commands(ABSOLUTE_FILE_PATH)
        self.assertEqual(actual_commands, EXPECTED_COMMANDS)


if __name__ == '__main__':
    unittest.main()
