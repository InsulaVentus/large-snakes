from os import listdir
import os


class FileNameReader:
    """
    Utility class used to extract version numbers, e.g 7.0.2-SNAPSHOT or 9.2 from a filename in a given directory
    """
    SNAPSHOT = 'SNAPSHOT'

    def extract_version_number(self, directory, file_format):
        """Extract the version number from a file of a given format in any given directory"""
        list_of_files = listdir(directory)

        for file in list_of_files:
            name_and_format = os.path.splitext(file)
            file_name = name_and_format[0]

            if name_and_format[1].__eq__(file_format):
                return self.get_version_number(file_name)

        raise Exception("%s%s%s%s" % ("No files of type ", file_format, " found in directory: ", directory))

    def get_version_number(self, file_name):
        """Extract the version number from a given file name"""
        file_array = file_name.split('-')
        last_element = file_array.__len__() - 1

        if file_array[last_element].__eq__(self.SNAPSHOT):
            version = file_array[last_element - 1] + '-' + self.SNAPSHOT
        else:
            version = file_array[last_element]

        return version
