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
pip install prettytable
pip install colorama
```

## simple guide for a basic user
Here's a simple guide for a basic user to run the `Daily_logger.py` script on a Windows-based computer:

1. **Install Python:**
   If you don't have Python installed, download it from the official website (https://www.python.org/downloads/). Make sure to check the box that says "Add Python to PATH" during the installation process.

2. **Install Required Libraries:**
   The script uses some Python libraries that may not be installed by default. Open Command Prompt and type the following commands to install them:

   ```shell
   pip install prettytable
   pip install colorama
   ```

3. **Save the Script:**
   Save the `Daily_logger.py` script to a location on your computer. For example, you might save it to your Documents folder.

4. **Run the Script:**
   To run the script, you'll need to use the Command Prompt. Here's how:

   - Press `Win + R` to open the Run dialog box.
   - Type `cmd` and press `Enter` to open Command Prompt.
   - Navigate to the location where you saved the script. For example, if you saved it in your Documents folder, you would type `cd Documents` and press `Enter`.
   - Once you're in the correct directory, type `python Daily_logger.py` and press `Enter` to run the script.

5. **Use the Script:**
   Once the script is running, follow the prompts in the Command Prompt window to log your work. Press `Enter` to start logging, and press `Enter` again to stop. You'll be asked to enter a name for the work you've done. The script will then log the start time, end time, work name, and duration to a CSV file.

Remember to always save your work before running any scripts, and only run scripts from sources you trust.

## Code Structure

- `log_work(start_time, end_time, work_name)`: Logs a work session to the daily CSV file and saves the end time to a separate file.
- `display_work_log()`: Displays the work log in a pretty table format in the console.
- `start_logging()`: Starts logging work sessions. Prompts the user to press Enter to start and end sessions and to enter a work name.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
