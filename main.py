#!/venv/Scripts/python.exe
# encoding: utf-8

from datetime import datetime

from library.modules import collector


log_file = None
debug = False


def startup():
    if debug:
        setup_running_log()
        write_to_running_log("This string should be written.")
        write_to_running_log(["These", "strings", "should", "be", "written."])
    else:
        pass

    collector_obj = collector.Collector()


def setup_running_log():
    global log_file

    time_in_seconds = int(datetime.today().timestamp())
    cwd = os.getcwd()
    log_file = (cwd + constants.LOG_DIRECTORY + str(time_in_seconds) + ".txt")


def write_to_running_log(data_in=None):
    # TODO:
    #     - Write code to send data to log file opened in setup_running_log()

    global log_file

    try:
        if data_in is not None:
            print("data_in = ", end="")
            if(type(data_in) is str):
                print("[Type: String, Value: " + data_in + "]")
            if(type(data_in) is list):
                print("[Type: List, Values: " + str(data_in) + "]")
    except Exception as e:
        pass


def error_on_start():
    print("There was an error during startup.")


if __name__ == "__main__":
    startup()
else:
    error_on_start()


exit()
