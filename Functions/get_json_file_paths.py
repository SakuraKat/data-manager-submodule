#  Copyright (c) 2022
#  - Katheryn Sakura (pseudonym)
#  - https://github.com/SakuraKat
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Description:
#  Gets the paths of all JSON files in a directory.

import glob
import os
import sys
import time


def get_json_file_paths(from_folder_full_path: str, is_verbose: bool) -> list:
    """
    This function gets the full paths to all the JSON files in the folder
    :param from_folder_full_path: The full path to the folder with the JSON files
    :param is_verbose: If True, then show progress
    :return: A list of JSON file paths
    """
    # Start the timer
    start_time = time.time()
    # Get the path to the folder with the JSON files
    path_to_json_files = from_folder_full_path
    # Get the list of JSON files
    json_files_list = glob.glob(path_to_json_files + "/*.json")
    if is_verbose:
        print("Loading JSON files from " + from_folder_full_path)
        print("Total JSON files found: " + str(len(json_files_list)))
        print("JSON files: " + str(json_files_list))
    # Get the total number of JSON files
    total_number_of_json_files = len(json_files_list)
    if total_number_of_json_files == 0:
        print("No JSON files found in " + from_folder_full_path)
        exit()
    # Print the message
    if is_verbose:
        print("----------------------------------------")
        print("Loading the JSON files...")
    # Stop the timer
    end_time = time.time()
    # Calculate the total time taken
    total_time_taken = end_time - start_time
    # Print the message
    if is_verbose:
        print("----------------------------------------")
        print("Total JSON files loaded: " + str(total_number_of_json_files))
        print("Total time taken to load the JSON files: {} seconds".format(
            total_time_taken))
        print("Average time taken to load a JSON file: {} seconds".format(round(
            (total_time_taken / total_number_of_json_files), 2)))
    # Return the list of JSON files
    return json_files_list


def main(input_folder_path: str, is_verbose: bool) -> None:
    """
    This function gets the full paths to all the JSON files in the folder
    :param input_folder_path: The full path to the folder with the JSON files
    :param is_verbose: If True, then show progress
    :return:
    """

    json_file_paths = get_json_file_paths(input_folder_path, is_verbose)
    print(json_file_paths)


if __name__ == '__main__':
    verbose, input_path = None, None
    parameters = sys.argv

    if len(sys.argv) == 5:
        if "-v" in parameters or "--verbose" in parameters:
            verbose = True
        else:
            verbose = False

        if "-i" in parameters or "--input" in parameters:
            input_path = parameters[parameters.index("-i") + 1] if "-i" in parameters \
                else parameters[parameters.index("--input") + 1]
        else:
            input_path = input("Enter the input path: ")
            if input_path == "":
                input_path = input("Enter the input path: ")
    else:
        print("Invalid parameters passed. Please pass the following parameters:")
        print("1. -v or --verbose (optional)")
        print(
            "2. -i or --input (the full path to the folder with the JSON files) (required)")
        exit(1)
    if len(sys.argv) == 2:
        verbose = False
        input_path = sys.argv[1]
    if len(sys.argv) == 1:
        verbose = False
        input_path = input("Enter the input path: ")
        if input_path == "":
            input_path = input("Enter the input path: ")
    # Check if input_path folder exists
    if not os.path.exists(input_path):
        print("The input path does not exist. Please enter a valid path.")
        exit(1)

    main(input_path, verbose)
