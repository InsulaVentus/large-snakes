from os import listdir
import os


class FileNameReader:
    SNAPSHOT = 'SNAPSHOT'

    def extract_version_number(self, directory, file_format):
        list_of_files = listdir(directory)

        for file in list_of_files:
            name_and_format = os.path.splitext(file)
            file_name = name_and_format[0]

            if name_and_format[1].__eq__(file_format):
                return self.get_version_number(file_name)

        raise Exception('No files of type ' + file_format + ' found in directory: ' + directory)

    def get_version_number(self, file_name):
        file_array = file_name.split('-')
        last_element = file_array.__len__() - 1

        if file_array[last_element].__eq__(self.SNAPSHOT):
            version = file_array[last_element - 1] + '-' + self.SNAPSHOT
        else:
            version = file_array[last_element]

        return version
