# Work Logger

Work Logger is a simple Python application that helps you keep track of your work sessions. It logs the start time, end time, and duration of each work session, along with a name for the work done during the session. The logs are saved in a CSV file for each day, making it easy to review your work history.

## Features

- Logs start time, end time, and duration of work sessions
- Allows you to name each work session for easy reference
- Saves logs in a daily CSV file
- Displays the work log in a pretty table format in the console
- Saves the end time of the last work session to use as the start time of the next session

## Usage

To start logging a work session, simply run the script. You will be prompted to press Enter to start logging. When you're done with your work session, press Enter again to end the session. You will then be prompted to enter a name for the work done during the session. The work log will be displayed in the console after each session.

## Requirements

- Python 3.7 or later
- prettytable
- colorama

You can install the required Python packages using pip:

```bash
pip install prettytable colorama
```

## Code Structure

- `log_work(start_time, end_time, work_name)`: Logs a work session to the daily CSV file and saves the end time to a separate file.
- `display_work_log()`: Displays the work log in a pretty table format in the console.
- `start_logging()`: Starts logging work sessions. Prompts the user to press Enter to start and end sessions and to enter a work name.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
