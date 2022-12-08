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
import os
import sys
import time


def write_converted_data_to_text_file(converted_data_list: list, output_path: str, verbose: bool) -> None:
    """
    This function writes the data to a text file
    :param converted_data_list: A list of converted data
    :param output_path: The output file path
    :param verbose: If True, then show progress
    :return: None
    """
    if verbose:
        print("----------------------------------------")
        print("Writing the data to a text file...")
    # Start the timer
    start_time = time.time()
    # Get the total number of JSON files
    length_of_data = len(converted_data_list)
    # Print the message
    if verbose:
        print("Writing the data to a text file...")
        print("Output file path: " + output_path)
    # Open the output file
    with open(output_path, "w", encoding="utf-8") as f:
        # Loop through the list of converted data
        for converted_data in converted_data_list:
            # Write the converted data to the output file
            f.write(converted_data + "\n")
    # Stop the timer
    end_time = time.time()
    # Calculate the total time taken
    total_time_taken = end_time - start_time
    # Print the message
    if verbose:
        print("----------------------------------------")
        print("Total data written: " + str(len(converted_data_list)))
        print("Total time taken to write the data: {} seconds".format(total_time_taken))
        print("Average time taken to write a line: {} seconds".format(
            round((total_time_taken / length_of_data), 2)))


def main(converted_data_list: list, output_path: str, verbose: bool):
    """
    This function writes the data to a text file in the required format
    :param converted_data_list:
    :param output_path:
    :param verbose:
    :return: None
    """
    write_converted_data_to_text_file(
        converted_data_list, output_path, verbose)


if __name__ == '__main__':
    inputs = []
    output = None
    is_verbose = False

    args = sys.argv

    if "-o" in args or "--output" in args:
        # Get the index of -o
        index = args.index("-o") if "-o" in args else args.index("--output")
        output = args[index + 1]
        args.pop(index)
        args.pop(index)
    else:
        print("Please specify an output file path")
        exit(1)
    if "-v" in args or "--verbose" in args:
        is_verbose = True
        args.pop(args.index("-v") if "-v" in args else args.index("--verbose"))
    if "-i" in args or "--input" in args:
        index = args.index("-i") if "-i" in args else args.index("--input")
        inputs = args[index + 1:]

    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))

    if len(inputs) == 0:
        while True:
            input_ = input("Please enter an input: ")
            if input_ == "EOF":
                break
            inputs.append(input_)

    main(inputs, output, is_verbose)
