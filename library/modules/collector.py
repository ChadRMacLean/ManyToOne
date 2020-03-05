#!../venv/Scripts/python.exe
# encoding: utf-8

import os

from platform import system as platform_name
from pathlib import Path

from library.modules import constants


class Collector:

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

    def __name__(self):
        return "File Collector"

    def create_work_folder(self):
        if not os.path.exists(self.input_directory):
            try:
                os.mkdir(self.input_directory)
            except Exception as e:
                print("[ERROR] Failed to create directory.")
        if not os.path.exists(self.output_directory):
            try:
                os.mkdir(self.output_directory)
            except Exception as e:
                print("[ERROR] Failed to create directory.")

    def scan_for_files(self):
        for root, dirs, files in os.walk(self.input_directory, topdown=False):
            for file_name in files:
                file_path = Path(os.path.join(root, file_name))
                file_extension = file_path.suffix
                if file_extension in self.file_extension:
                    # TODO: Find a better way to add to the arrays. Using
                    # index is not a good idea and it's vague.
                    if not self.in_files:
                        asset_folder = str(file_path).split(self.input_directory)[1].split(file_name)[0]
                        self.in_files.append(asset_folder)
                    self.in_files.append(file_path)
        if self.in_files:
            self.join_files()

    def join_files(self):
        for file in self.in_files:
            if os.path.isfile(file):
                with open(file, "r") as f:
                    self.in_files_data.append(f.readlines())
                self.in_files_data.append("\n")

        if self.in_files_data:
            self.write_master_file()

    def write_master_file(self):
        if self.in_files_data:
            output_dir = self.output_directory + self.in_files[0]
            if not os.path.isdir(output_dir):
                try:
                    os.makedirs(output_dir)
                except Exception as e:
                    print("[ERROR] Failed to create directory.")
                self.write_master_file()
            else:
                output_file = output_dir + "master" + self.file_extension
                if not os.path.isfile(output_file):
                    with open(output_file, "w") as file:
                        file.write("")
                    self.write_master_file()
                else:
                    # with open(output_css_file, "w") as file:
                    #     for file_data in self.in_files_data:
                    #         file.write(file_data)
                    with open(output_file, "w") as file:
                        for file_data in self.in_files_data:
                            for line in file_data:
                                file.write(line)
