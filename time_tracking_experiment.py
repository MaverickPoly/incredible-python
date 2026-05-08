import subprocess
import time


def get_active_window():
    name = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"]).decode()
    # name = subprocess.check_output(["xdotool", "getwindowname", win_id]).decode()
    return name


current_app = None
start_time = time.time()

while True:
    app = get_active_window()

    if app != current_app:
        if current_app is not None:
            duration = time.time() - start_time
            print(current_app, duration)

        current_app = app
        start_time = time.time()

    time.sleep(1)
