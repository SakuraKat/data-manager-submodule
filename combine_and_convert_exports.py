# Written with the help of github copilot
# Steps:
# 1. Load all the JSON files from the folder JSON Files
# The JSON files are in the following format:
# {
#   "guild": {
#     "id": "GuildID",
#     "name": "GuildName",
#     "iconUrl": "GuildIconUrl"
#   },
#   "channel": {
#     "id": "ChannelId",
#     "type": "ChannelType",
#     "categoryId": "ChannelCategoryId",
#     "category": "ChannelCategory",
#     "name": "ChannelName",
#     "topic": "ChannelTopic"
#   },
#   "dateRange": {
#     "after": DateRangeAfter,
#     "before": DateRangeBefore
#   },
#   "messages": [
#     {
#       "id": "MessageId",
#       "type": "MessageType",
#       "timestamp": "MessageTimestamp",
#       "timestampEdited": "MessageTimestampEdited",
#       "callEndedTimestamp": MessageCallEndedTimestamp,
#       "isPinned": isMessagePinned,
#       "content": "MessageContent",
#       "author": {
#         "id": "MessageAuthorId",
#         "name": "MessageAuthorName",
#         "discriminator": "MessageAuthorDiscriminator",
#         "nickname": "MessageAuthorNickname",
#         "color": "MessageAuthorColor",
#         "isBot": isMessageAuthorBot,
#         "avatarUrl": "MessageAuthorAvatarUrl"
#       },
#       "attachments": [AttachmentsData],
#       "embeds": [EmbedsData],
#       "stickers": [StickersData],
#       "reactions": [ReactionsData],
#       "mentions": [MentionsData]
#     }
#   ],
#   "messageCount": MessageCount
# }
# The data is in utf-8 format
# 2. Take the following data from the JSON files:
# 2.1. MessageAuthorName
# 2.2. MessageAuthorDiscriminator
# 2.3. MessageContent
# 3. Convert the data to the following format:
# 3.1. MessageAuthorName___MessageAuthorDiscriminator: MessageContent
# If the message content is empty, then the message is skipped
# If the message has new lines, then it is split into multiple messages
# 4. Save the converted data to the file Output/converted.txt
#
# Requirements:
# Use functions to make the code more readable
# Use docstrings to document the functions
# Use comments to explain the code
#
# Code starts here
#
import glob
import json
import os
import sys
import time


# Function to load the JSON files from the folder and time the process
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


# Function to get the data from the JSON files, time the process and show progress
def get_data_from_json_files(json_files_path_list: list, is_verbose: bool) -> list:
    """
    This function gets the raw data from the JSON files
    :param json_files_path_list: A list of JSON file paths
    :param is_verbose: If True, then show progress
    :return: A list of JSON data
    """
    # Start the timer
    start_time = time.time()
    # Create an empty list to store the data
    raw_data_list = []
    # Get the total number of JSON files
    total_number_of_json_files = len(json_files_path_list)
    # Print the message
    if is_verbose:
        print("----------------------------------------")
        print("Getting the data from the JSON files...")
    # Loop through the list of JSON files
    for json_file in json_files_path_list:
        if is_verbose:
            print("Loading JSON file: " + json_file)
        # Open the JSON file
        with open(json_file, "r", encoding="utf-8") as f:
            # Load the JSON file
            data = json.load(f)
            # Get the messages from the JSON file
            messages = data["messages"]
            # Loop through the messages
            for message in messages:
                # Get the message author name
                message_author_name = message["author"]["name"]
                # Get the message author discriminator
                message_author_discriminator = message["author"]["discriminator"]
                # Combine the message author name and discriminator
                message_author = message_author_name + "___" + message_author_discriminator
                # Get the message content
                message_content = message["content"]
                # Append the message author name and message content to the data list
                raw_data_list.append([message_author, message_content])
    # Stop the timer
    end_time = time.time()
    # Calculate the total time taken
    total_time_taken = end_time - start_time
    # Print the message
    if is_verbose:
        print("----------------------------------------")
        print("Total data loaded: " + str(len(raw_data_list)))
        print("Total time taken to load the data: {} seconds".format(total_time_taken))
        print("Average time taken to load a JSON file: {} seconds".format(
            round((total_time_taken / total_number_of_json_files), 2)))
        print("----------------------------------------")
        # print the number of authors
        print("Number of authors: " +
              str(len(set([data[0] for data in raw_data_list]))))
        # print the number of messages
        print("Number of messages: " + str(len(raw_data_list)))
        # Find all the authors
        authors_list = set([data[0] for data in raw_data_list])
        authors_list = [*authors_list]
        authors_list.sort()
        # print the authors
        print("Authors: " + str(authors_list))
        print("----------------------------------------")
        # print the number of messages per author
        for author in authors_list:
            print("Number of messages from " + author + ": " + str(len(
                [data[1] for data in raw_data_list if data[0] == author])))
        print("----------------------------------------")
        print("Average number of messages per author: " + str(len(
            raw_data_list) / len(set([data[0] for data in raw_data_list]))))
    # Return the data list
    return raw_data_list


# Function to convert the data to the required format, time the process and show progress
def convert_data_to_required_format(raw_data_list: list, is_verbose: bool) -> list:
    """
    This function converts the data to the required format by removing the new line characters and replacing the double
    quotes with single quotes
    :param raw_data_list: A list of JSON data
    :param is_verbose: If True, then show progress
    :return: A list of converted data
    """
    # Start the timer
    start_time = time.time()
    # Create an empty list to store the converted data
    converted_data_list = []
    # Get the total number of JSON files
    total_number_of_json_files = len(raw_data_list)
    # Print the message
    if is_verbose:
        print("----------------------------------------")
        print("Converting the data to the required format...")
    # Loop through the list of JSON files
    for data in raw_data_list:
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
    if is_verbose:
        print("----------------------------------------")
        print("Total data converted: " + str(len(converted_data_list)))
        print("Total time taken to convert the data: {} seconds".format(
            total_time_taken))
        print("Average time taken to convert a JSON file: {} seconds".format(
            round((total_time_taken / total_number_of_json_files), 2)))
        print("----------------------------------------")
        # Print the number of lines removed
        print("Number of lines removed: " +
              str(len(raw_data_list) - len(converted_data_list)))
        # Print the number of lines removed per author
        print("Number of lines removed per author: " + str(
            (len(raw_data_list) - len(converted_data_list)) / len(set([data[0] for data in raw_data_list]))))
    # Return the converted data list
    return converted_data_list


# Function to write the data to a text file, time the process and show progress
def write_data_to_text_file(converted_data_list: list, output_path: str, is_verbose: bool) -> None:
    """
    This function writes the data to a text file
    :param converted_data_list: A list of converted data
    :param output_path: The output file path
    :param is_verbose: If True, then show progress
    :return: None
    """
    if is_verbose:
        print("----------------------------------------")
        print("Writing the data to a text file...")
    # Start the timer
    start_time = time.time()
    # Get the total number of JSON files
    total_number_of_json_files = len(converted_data_list)
    # Print the message
    if is_verbose:
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
    if is_verbose:
        print("----------------------------------------")
        print("Total data written: " + str(len(converted_data_list)))
        print("Total time taken to write the data: {} seconds".format(total_time_taken))
        print("Average time taken to write a JSON file: {} seconds".format(
            round((total_time_taken / total_number_of_json_files), 2)))


def _print_help() -> None:
    print("\033[1m\033[4m\033[94mCombine and convert exports\033[0m")
    print("Combine and convert exports from Discord")
    print("Usage: python3 combine_and_convert_exports.py "
          "-i <input_folder_path> -o <output_file_path> -v <true/false>")
    print("=" * 80)
    print("Options:")
    print("\033[1m\033[4m\033[94m-i\033[0m, \033[1m\033[4m\033[94m--input\033[0m: Input folder path")
    print("\033[1m\033[4m\033[94m-o\033[0m, \033[1m\033[4m\033[94m--output\033[0m: Output file path")
    print("\033[1m\033[4m\033[94m-v\033[0m, \033[1m\033[4m\033[94m--verbose\033[0m: Verbose (True or False)")
    print("\033[1m\033[4m\033[94m-h\033[0m, \033[1m\033[4m\033[94m--help\033[0m: Print this help text")
    print("All the parameters are\033[1m\033[4m\033[94m optional\033[0m")
    print("If the parameters are not passed, then the program will use the"
          "\033[1m\033[4m\033[94m default values\033[0m")
    print("=" * 80)
    print("The default values are:")
    print("Verbose:\033[1m\033[4m\033[94m false\033[0m")
    print("Input folder path: \033[1m\033[4m\033[94m" + str(DEFAULT_INPUT_FOLDER_PATH) + "\033[0m")
    print("Output file path: \033[1m\033[4m\033[94m" + str(DEFAULT_OUTPUT_FILE_PATH) + "\033[0m")
    print("=" * 80)
    print("Examples:")
    print("python3 combine_and_convert_exports.py -i "
          "/home/user/Downloads -o /home/user/Downloads/output.txt -v True")
    print("python3 combine_and_convert_exports.py -i /home/user/Downloads -o /home/user/Downloads/output.txt")
    print("python3 combine_and_convert_exports.py -i /home/user/Downloads -v False")
    print("python3 combine_and_convert_exports.py -i /home/user/Downloads")
    print("python3 combine_and_convert_exports.py -v True")
    print("python3 combine_and_convert_exports.py")
    print("python3 combine_and_convert_exports.py -h")
    print("python3 combine_and_convert_exports.py --help")
    print("python3 combine_and_convert_exports.py -o /home/user/Downloads/output.txt")


# Function to run the program, time the process and show progress
def run_program(input_path: str, output_path: str, is_verbose: bool) -> None:
    """
    This function runs the program
    :param input_path: The input folder path
    :param output_path: The output file path
    :param is_verbose: If True, then show progress
    :return: None
    """
    # Start the timer
    start_time = time.time()
    # Print the message
    if is_verbose:
        print("----------------------------------------")
        print("Running the program...")
    # Load the JSON file paths
    json_file_paths = get_json_file_paths(input_path, is_verbose)
    # Load the JSON files
    raw_data_list = get_data_from_json_files(json_file_paths, is_verbose)
    # Convert the data to the required format
    converted_data_list = convert_data_to_required_format(
        raw_data_list, is_verbose)
    # Write the data to a text file
    write_data_to_text_file(converted_data_list, output_path, is_verbose)
    # Stop the timer
    end_time = time.time()
    # Calculate the total time taken
    total_time_taken = end_time - start_time
    # Print the message
    if is_verbose:
        print("----------------------------------------")
        print("Total time taken to run the program: {} seconds".format(
            total_time_taken))
        print("----------------------------------------")
        print("Program finished successfully!")
        print("----------------------------------------")


# Run the program
if __name__ == "__main__":
    # Check the parameters passed to the program
    # The parameters passed are:
    # 1. Verbose (True or False)
    # 2. Input folder path
    # 3. Output file path
    # All the parameters are optional

    DEFAULT_INPUT_FOLDER_PATH = os.getcwd() + "/JSON Files"
    DEFAULT_OUTPUT_FILE_PATH = os.getcwd() + "/Output/output.txt"
    input_folder_path, output_file_path, verbose = None, None, None

    # Get the parameters passed to the program
    parameters = sys.argv[1:]
    # Check if the parameters are passed
    if len(parameters) > 0:
        # Check if the help parameter is passed
        if "-h" in parameters or "--help" in parameters:
            # Print the help message
            _print_help()
            # Exit the program
            sys.exit()
        # Check if the input folder path is passed
        if "-i" in parameters or "--input" in parameters:
            # Get the input folder path
            input_folder_path = parameters[parameters.index("-i") + 1] \
                if "-i" in parameters else parameters[parameters.index("--input") + 1]
        else:
            # Set the default input folder path
            input_folder_path = DEFAULT_INPUT_FOLDER_PATH
        # Check if the output file path is passed
        if "-o" in parameters or "--output" in parameters:
            # Get the output file path
            output_file_path = parameters[parameters.index("-o") + 1] \
                if "-o" in parameters else parameters[parameters.index("--output") + 1]
        else:
            # Set the output file path to the default value
            output_file_path = DEFAULT_OUTPUT_FILE_PATH
        # Check if the verbose parameter is passed
        if "-v" in parameters or "--verbose" in parameters:
            # Get the verbose parameter
            verbose = parameters[parameters.index("-v") + 1] \
                if "-v" in parameters else parameters[parameters.index("--verbose") + 1]
            # Check if the verbose parameter is True
            if verbose.lower() == "true" or verbose.lower() == "t":
                verbose = True
        else:
            verbose = False
    else:
        # Set the default values
        input_folder_path = DEFAULT_INPUT_FOLDER_PATH
        output_file_path = DEFAULT_OUTPUT_FILE_PATH
        verbose = False

    # Check if the output folder exists
    # output_folder_path is path_to_folder/output_file_name.txt
    # So, we need to remove the output_file_name.txt from the path
    output_folder_path = "/".join(output_file_path.split("/")[:-1])
    if not os.path.exists(os.path.dirname(output_folder_path)):
        # Create the output folder
        os.makedirs(os.path.dirname(output_folder_path))

    # Run the program
    run_program(input_folder_path, output_file_path, verbose)
