#!/venv/Scripts/python.exe
# encoding: utf-8

from datetime import datetime

import collector
import constants


def main():
    for extension in constants.SUPPORTED_EXTENSIONS:
        collector_obj = collector.Collector(extension)
        collector_obj.create_work_folder()
        collector_obj.scan_for_files()


def error_on_start():
    print("There was an error during startup.")


if __name__ == "__main__":
    main()
else:
    error_on_start()


exit()
