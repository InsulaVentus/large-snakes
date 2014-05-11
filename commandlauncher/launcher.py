from subprocess import call
from os import path
import sys
from commandlauncher.fileparser import FileParser


def launch():
    ##Recieve path to command file from command line args
    command_file = sys.argv.__getitem__(1)

    if path.exists(command_file):
        ##Parse file and return a map of codes and commands
        parser = FileParser()
        parser.get_commands(command_file)
    else:
        raise Exception("The file %s does not exist" % command_file)

    ##Run a command from the shell
    call(["git", "log"], shell=True)

launch()
