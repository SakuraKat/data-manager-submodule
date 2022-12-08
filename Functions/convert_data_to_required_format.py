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
#  This script is used to convert the JSON data into the required format.

import sys
import time


def convert_data_to_required_format(data_list: list, verbose: bool) -> list:
    """
    This function converts the data to the required format
    by removing the new line characters and
    replacing the double quotes with single quotes
    :param data_list: A list of JSON data
    :param verbose: If True, then show progress
    :return: A list of converted data
    """
    # Start the timer
    start_time = time.time()
    # Create an empty list to store the converted data
    converted_data_list = []
    # Get the total number of JSON files
    total_number_of_json_files = len(data_list)
    # Print the message
    if verbose:
        print("----------------------------------------")
        print("Converting the data to the required format...")
    # Loop through the list of JSON files
    for data in data_list:
        # Get the message author name
        message_author_name = data[0]
        # Get the message content
        message_content = data[1]
        message_content_list = message_content.split("\n")
        # Loop through the message content list
        for message in message_content_list:
            # Only add the message if it is not empty
            if message != "":
                # Append the message author name and message content to the converted data list
                converted_data_list.append(
                    message_author_name + ": " + message + "\n")
    # Stop the timer
    end_time = time.time()
    # Calculate the total time taken
    total_time_taken = end_time - start_time
    # Print the message
    if verbose:
        print("----------------------------------------")
        print("Total data converted: " + str(len(converted_data_list)))
        print("Total time taken to convert the data: {} seconds".format(
            total_time_taken))
        print("Average time taken to convert a JSON file: {} seconds".format(
            round((total_time_taken / total_number_of_json_files), 2)))
        print("----------------------------------------")
        # Print the number of lines removed
        print("Number of lines removed: " +
              str(len(data_list) - len(converted_data_list)))
        # Print the number of lines removed per author
        print("Number of lines removed per author: " + str(
            (len(data_list) - len(converted_data_list)) / len(set([data[0] for data in data_list]))))
    # Return the converted data list
    return converted_data_list


def main(data_list: list, verbose: bool = False) -> None:
    """
    This function converts the JSON data into the required format
    :param data_list: list of raw data
    :param verbose: if True, then show progress
    :return: None
    """
    # TODO: Check if other docstrings use rtype instead of return

    converted_data = convert_data_to_required_format(data_list, verbose)
    print(converted_data)


if __name__ == '__main__':
    is_verbose = False
    args = sys.argv[1:]

    if len(args) == 0:
        print("No arguments provided. Exiting.")
        sys.exit(1)
    if '-v' in args or '--verbose' in args:
        # TODO: check if other places have args.contains()
        is_verbose = True
        try:
            args.remove('-v')
        finally:
            pass
        try:
            args.remove('--verbose')
        finally:
            pass
    if len(args) == 0:
        print("No items provided. Exiting.")
        sys.exit(1)

    main(args, is_verbose)
