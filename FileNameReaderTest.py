import unittest
from FileNameReader import FileNameReader


class MyTestCase(unittest.TestCase):
    FIRST_DIR = 'D:/Test_files'
    SECOND_DIR = 'D:/Test_files/second'
    NO_FILE_DIR = 'D:'
    EAR_FILE = '.ear'
    SNAPSHOT_VERSION = '7.0.2-SNAPSHOT'
    SIMPLE_VERSION = '7.0.2'

    reader = FileNameReader()

    def test_should_find_snapshot_version(self):
        actual_version = self.reader.extract_version_number(self.FIRST_DIR, self.EAR_FILE)
        self.assertEqual(self.SNAPSHOT_VERSION, actual_version, 'Unexpected version found')

    def test_should_find_simple_version(self):
        actual_version = self.reader.extract_version_number(self.SECOND_DIR, self.EAR_FILE)
        self.assertEqual(self.SIMPLE_VERSION, actual_version, 'Unexpected version found')

    def test_should_rise_exception_when_file_not_found(self):
        self.assertRaises(Exception, self.reader.extract_version_number, self.NO_FILE_DIR, self.EAR_FILE)


if __name__ == '__main__':
    unittest.main()
