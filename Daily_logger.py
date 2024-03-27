import csv
import datetime
import os
from prettytable import PrettyTable
from colorama import Fore, Style, init
import threading
import time

init(autoreset=True)


def log_work(start_time, end_time, work_name):
    date_str = datetime.datetime.now().strftime('%d_%m_%Y')
    dir_path = os.path.join(os.path.dirname(__file__), date_str)
    os.makedirs(dir_path, exist_ok=True)  # Create the directory if it does not exist
    file_path = os.path.join(dir_path, f'{date_str}.csv')
    duration = end_time - start_time
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    duration_str = f"{hours:02}:{minutes:02}:{seconds:02}"
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([start_time.strftime('%H:%M:%S'), end_time.strftime('%H:%M:%S'), work_name, duration_str])
    last_end_time_file_path = os.path.join(dir_path, 'last_end_time.txt')
    with open(last_end_time_file_path, 'w') as file:  # Save the end time to a separate file
        file.write(end_time.strftime('%Y-%m-%d %H:%M:%S'))

def display_work_log():
    date_str = datetime.datetime.now().strftime('%d_%m_%Y')
    dir_path = os.path.join(os.path.dirname(__file__), date_str)
    file_path = os.path.join(dir_path, f'{date_str}.csv')
    if not os.path.exists(file_path):
        print(Fore.YELLOW + "No work has been logged yet today.")
        return
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        table = PrettyTable(['Start Time', 'End Time', 'Work Name', 'Duration'])
        for row in reader:
            start_time, end_time, work_name, duration = row
            hours, minutes, seconds = map(int, duration.split(':'))
            duration_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            table.add_row([start_time, end_time, work_name, duration_str])
        print(Fore.MAGENTA + str(table))
    

def start_logging():
    date_str = datetime.datetime.now().strftime('%d_%m_%Y')
    dir_path = os.path.join(os.path.dirname(__file__), date_str)
    last_end_time_file_path = os.path.join(dir_path, 'last_end_time.txt')
    def display_duration(start_time):
        time.sleep(1)  # Delay before the first print statement
        while getattr(threading.current_thread(), "do_run", True):
            duration = datetime.datetime.now() - start_time
            total_seconds = duration.total_seconds()
            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            seconds = int(total_seconds % 60)
            duration_str = f"{hours:02}:{minutes:02}:{seconds:02}"
            print(Fore.CYAN + f"\rCurrent duration: {duration_str}", end='')
            time.sleep(1)
    try:
        if os.path.exists(last_end_time_file_path):  # If the file with the last end time exists
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            display_work_log()
            with open(last_end_time_file_path, 'r') as file:
                start_time = datetime.datetime.strptime(file.read(), '%Y-%m-%d %H:%M:%S')  # Use the last end time as the start time
        else:
            input(Fore.GREEN + Style.BRIGHT + "Press Enter to start logging...")
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            display_work_log()
            start_time = datetime.datetime.now()
        while True:
            duration_thread = threading.Thread(target=display_duration, args=(start_time,), daemon=True)
            duration_thread.start()
            print('\n' + Fore.GREEN + Style.BRIGHT + "Press Enter to end task...")
            input()
            duration_thread.do_run = False
            duration_thread.join()
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            display_work_log()
            input(Fore.RED + Style.BRIGHT + "Press Enter again to confirm...")
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            display_work_log()
            end_time = datetime.datetime.now()
            work_name = input(Fore.GREEN + Style.BRIGHT + "Enter work name (or leave blank): ")
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            display_work_log()
            log_work(start_time, end_time, work_name)
            start_time = end_time
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
            display_work_log()
    except KeyboardInterrupt:
        print("Work log saved. Exiting program.")
        exit(0)

if __name__ == "__main__":
    start_logging()
