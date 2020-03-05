#!../venv/Scripts/python.exe
# encoding: utf-8

import os

from platform import system as platform_name
from pathlib import Path

import constants


class Collector:

    """class: Collector

    This module maps and processes input files supplied by the user. After
    mapping the files supplied, files that match the extension supplied during
    initialization of this module are joined together into a single master
    file for use in another environment.

    Arguments:
        extension (str): String containing the full file extension. (ex ".py")
    """

    platform, cwd = None, None
    input_directory, output_directory = None, None
    in_files, in_files_data = None, None
    file_extension = None

    def __init__(self, extension):
        self.cwd = os.getcwd()
        self.platform = platform_name
        self.input_directory = self.cwd + constants.INPUT_DIRECTORY
        self.output_directory = self.cwd + constants.OUTPUT_DIRECTORY
        self.in_files, self.in_files_data = [], []
        self.file_extension = extension

    def create_work_folder(self):

        """function: create_work_folder

        This function checks for existance of the user input directory. If one
        does not exist, it will be created.

        Raises:
            Exception: Creation of folder was not possible or exists.

        Todo:
            Add better error detection and improve exception handling.
        """

        if not os.path.exists(self.input_directory):
            try:
                os.mkdir(self.input_directory)
            except Exception as e:
                print(e)
        if not os.path.exists(self.output_directory):
            try:
                os.mkdir(self.output_directory)
            except Exception as e:
                print(e)

    def scan_for_files(self):

        """function: scan_for_files

        This function checks for files that match the extension passed to the
        class. If a match is found, adds the path to a list for future
        processing.

        Todo:
            Add better error detection and improve exception handling.
        """

        for root, dirs, files in os.walk(self.input_directory, topdown=False):
            unhandled = dirs
            for file_name in files:
                file_path = Path(os.path.join(root, file_name))
                file_extension = file_path.suffix
                if file_extension in self.file_extension:
                    if not self.in_files:
                        asset_folder = str(file_path).split(self.input_directory)[1].split(file_name)[0]
                        self.in_files.append(asset_folder)
                    self.in_files.append(file_path)
        if self.in_files:
            self.join_files()

    def join_files(self):

        """function: join_files

        This function will iterate through a list of file paths, open it, store
        it in memory for future processing.

        Todo:
            Add better error detection and improve exception handling.
        """

        for file in self.in_files:
            if os.path.isfile(file):
                with open(file, "r") as f:
                    self.in_files_data.append(f.readlines())
                self.in_files_data.append("\n")

        if self.in_files_data:
            self.write_master_file()

    def write_master_file(self):

        """function: write_master_file

        This function generates a single master file from the stored
        input files.

        Raises:
            Exception: Creation of output folder not possible or exists.

        Todo:
            Add better error detection and improve exception handling.
        """

        if self.in_files_data:
            output_dir = self.output_directory + self.in_files[0]
            if not os.path.isdir(output_dir):
                try:
                    os.makedirs(output_dir)
                except Exception as e:
                    print(e)
                self.write_master_file()
            else:
                output_file = output_dir + "master" + self.file_extension
                if not os.path.isfile(output_file):
                    with open(output_file, "w") as file:
                        file.write("")
                    self.write_master_file()
                else:
                    with open(output_file, "w") as file:
                        for file_data in self.in_files_data:
                            for line in file_data:
                                file.write(line)
