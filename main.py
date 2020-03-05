#!/venv/Scripts/python.exe
# encoding: utf-8

from datetime import datetime

from library.modules import collector
from library.modules import constants


def startup():
    for extension in constants.SUPPORTED_EXTENSIONS:
        collector_obj = collector.Collector(extension)
        collector_obj.create_work_folder()
        collector_obj.scan_for_files()


def error_on_start():
    print("There was an error during startup.")


if __name__ == "__main__":
    startup()
else:
    error_on_start()


exit()
