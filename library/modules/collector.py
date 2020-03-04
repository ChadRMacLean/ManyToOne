#!../venv/Scripts/python.exe
# encoding: utf-8

import os

from platform import system as platform_name
from pathlib import Path

from library.modules import constants


class Collector:

    platform, cwd = None, None
    input_directory, output_directory = None, None
    css_files, js_files = None, None
    css_files_data, js_files_data = None, None

    def __init__(self):
        self.cwd = os.getcwd()
        self.platform = platform_name
        self.input_directory = self.cwd + constants.INPUT_DIRECTORY
        self.output_directory = self.cwd + constants.OUTPUT_DIRECTORY
        self.css_files, self.js_files = [], []
        self.css_files_data, self.js_files_data = [], []

        self.__create_work_folder()
        self.__scan_for_files()

    def __name__(self):
        return "File Collector"

    def __create_work_folder(self):
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

    def __scan_for_files(self):
        for root, dirs, files in os.walk(self.input_directory, topdown=False):
            for file_name in files:
                file_path = Path(os.path.join(root, file_name))
                file_extension = file_path.suffix
                if file_extension in constants.SUPPORTED_EXTENSIONS:
                    # TODO: Find a better way to add to the arrays. Using
                    # index is not a good idea and it's vague.
                    if (constants.SUPPORTED_EXTENSIONS.index(file_extension)) == 0:
                        if not self.css_files:
                            css_asset_folder = str(file_path).split(self.input_directory)[1].split(file_name)[0]
                            self.css_files.append(css_asset_folder)
                        self.css_files.append(file_path)
                    elif (constants.SUPPORTED_EXTENSIONS.index(file_extension)) == 1:
                        if not self.js_files:
                            js_asset_folder = str(file_path).split(self.input_directory)[1].split(file_name)[0]
                            self.js_files.append(js_asset_folder)
                        self.js_files.append(file_path)
        if self.css_files or self.js_files:
            self.__join_files()

    def __join_files(self):
        for file in self.css_files:
            if os.path.isfile(file):
                with open(file, "r") as f:
                    self.css_files_data.append(f.readlines())
                self.css_files_data.append("\n")

        for file in self.js_files:
            if os.path.isfile(file):
                with open(file, "r") as f:
                    self.js_files_data.append(f.readlines())
                self.js_files_data.append("\n")

        if self.css_files_data:
            self.__write_css_master_file()
        if self.js_files_data:
            self.__write_js_master_file()

    def __write_css_master_file(self):
        if self.css_files_data:
            output_css_dir = self.output_directory + self.css_files[0]
            if not os.path.isdir(output_css_dir):
                try:
                    os.makedirs(output_css_dir)
                except Exception as e:
                    print("[ERROR] Failed to create directory.")
                self.__write_css_master_file()
            else:
                output_css_file = output_css_dir + "master.css"
                if not os.path.isfile(output_css_file):
                    with open(output_css_file, "w") as file:
                        file.write("")
                    self.__write_css_master_file()
                else:
                    # with open(output_css_file, "w") as file:
                    #     for file_data in self.css_files_data:
                    #         file.write(file_data)
                    with open(output_css_file, "w") as file:
                        for file_data in self.css_files_data:
                            for line in file_data:
                                file.write(line)

    def __write_js_master_file(self):
        if self.js_files_data:
            output_js_dir = self.output_directory + self.js_files[0]
            if not os.path.isdir(output_js_dir):
                try:
                    os.makedirs(output_js_dir)
                except Exception as e:
                    print("[ERROR] Failed to create directory.")
                self.__write_js_master_file()
            else:
                output_js_file = output_js_dir + "master.js"
                if not os.path.isfile(output_js_file):
                    with open(output_js_file, "w") as file:
                        file.write("")
                    self.__write_js_master_file()
                else:
                    # with open(output_js_file, "w") as file:
                    #     for file_data in self.css_files_data:
                    #         file.write(file_data)
                    with open(output_js_file, "w") as file:
                        for file_data in self.js_files_data:
                            for line in file_data:
                                file.write(line)
