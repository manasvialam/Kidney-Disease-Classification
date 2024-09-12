import os
import sys
import logging

logging_str = "[%(asctime)s:%(levelname)s: %(module)s: %(message)s]"

log_dir ="logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok= True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")

#Importing modules
# os: Provides fuctions for interacting with the operating system(like file and directory management)
# sys: Provides access to system - specific parameters and functions.
# logging: Provides a flexible framework for emitting log messages from python programs

# Defining log format
# Defines the format of log messages: timestamp(asctime), log level(levelname), module name(module), and the actual message(message).

# Creating Log Directory and file path(line 7-9)
# log_dir : The directory to store log files
# log_filepath : The full path for the log file
# os.makedirs : Create the log directory if it doesn't exist (exist_ok= True) avoids errors if the directory already exists)

# Configuring the Logging system (line 11- 19)
# level = logging.INFO : Sets the logging level to INFO, capturing all messages at this level or higher
# format = logging_str: specifies the log message format defined earlier
# handlers:
#   Filehandler : Writes log messages to the specified file
#   StreamHandler : Outputs log messages to the console (sys.stdout)

#Creating a Logger Instance
# getLogger : Creates a logger object named "cnnClassifierLogger" to manage logging in the script

# Purpose - This script sets up a logging system that records events of both a file (running_logs.log) and the console, using a defined format.
# It is useful for tracking the progress, errors, and important events in a ML project or any other Python application.
