class FileParser:
    def get_commands(self, absolute_file_path):

        ##Open a file in read mode
        file_object = open(absolute_file_path, "r")

        commands = {}

        for line in file_object:
            clean_line = line.strip().expandtabs(2)

            key_builder = [""]
            command_builder = [""]

            ##Key
            looking_for_start_of_code_bracket = True
            looking_for_start_of_key = False
            reading_key = False

            ##Command
            looking_for_start_of_command = False
            reading_command = False

            for character in clean_line:
                if reading_command:
                    if character.isspace() and key_builder:
                        if not command_builder[-1].isspace():
                            command_builder.append(character)
                        else:
                            break

                    elif is_valid_character(character):
                        command_builder.append(character)

                    else:
                        raise Exception(character + " is not a valid character within a command")

                elif looking_for_start_of_command:
                    if is_valid_character(character):
                        command_builder.append(character)
                        reading_command = True

                elif reading_key:
                    if character.isspace() and key_builder:
                        if not key_builder[-1].isspace():
                            key_builder.append(character)
                        else:
                            ##TODO: Throw exception caused by double spaces
                            break

                    elif character.isdigit() or character.isalpha() or character.__eq__("-") or character.__eq__("_"):
                        key_builder.append(character)

                    elif character.__eq__("]"):
                        looking_for_start_of_command = True

                    else:
                        ##TODO: Throw exception caused by invalid key character
                        break

                elif looking_for_start_of_key:
                    if character.__eq__("]"):
                        ##TODO: Throw exception caused by putting ']' before a '['
                        break

                    if character.isdigit() or character.isalpha():
                        key_builder.append(character)
                        reading_key = True

                elif looking_for_start_of_code_bracket:
                    if character.__eq__("["):
                        looking_for_start_of_key = True

            if looking_for_start_of_key and reading_key and looking_for_start_of_command and reading_command:
                key = ''.join(key_builder).rstrip()
                command = ''.join(command_builder).rstrip()
                if not key in commands:
                    commands.update({key: command})

            pass

        file_object.close()
        return commands


def read_command(character, key_builder, command_builder):
    if character.isspace() and key_builder:
        if not command_builder[-1].isspace():
            command_builder.append(character)
        else:
            return False

    elif is_valid_character(character):
        command_builder.append(character)

    else:
        raise Exception(character + " is not a valid character within a command")


def is_valid_character(character):
    return \
        character.isdigit() \
            or character.isalpha() \
            or character.__eq__("-") \
            or character.__eq__("_") \
            or character.__eq__("/") \
            or character.__eq__(":") \
            or character.__eq__(".")