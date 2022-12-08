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
#  Gets data from JSON files exported via Discord Chat Exporter.
#  Link: https://github.com/Tyrrrz/DiscordChatExporter
#  Format of JSON file:
#  {
#    "guild": {
#      "id": "GuildID",
#      "name": "GuildName",
#      "iconUrl": "GuildIconUrl"
#    },
#    "channel": {
#      "id": "ChannelId",
#      "type": "ChannelType",
#      "categoryId": "ChannelCategoryId",
#      "category": "ChannelCategory",
#      "name": "ChannelName",
#      "topic": "ChannelTopic"
#    },
#    "dateRange": {
#      "after": DateRangeAfter,
#      "before": DateRangeBefore
#    },
#    "messages": [
#      {
#        "id": "MessageId",
#        "type": "MessageType",
#        "timestamp": "MessageTimestamp",
#        "timestampEdited": "MessageTimestampEdited",
#       "callEndedTimestamp": MessageCallEndedTimestamp,
#        "isPinned": isMessagePinned,
#        "content": "MessageContent",
#       "author": {
#          "id": "MessageAuthorId",
#          "name": "MessageAuthorName",
#          "discriminator": "MessageAuthorDiscriminator",
#          "nickname": "MessageAuthorNickname",
#          "color": "MessageAuthorColor",
#          "isBot": isMessageAuthorBot,
#          "avatarUrl": "MessageAuthorAvatarUrl"
#        },
#        "attachments": [AttachmentsData],
#        "embeds": [EmbedsData],
#        "stickers": [StickersData],
#        "reactions": [ReactionsData],
#        "mentions": [MentionsData]
#      }
#    ],
#    [...]
#    "messageCount": MessageCount
#  }

import json
import os
import sys
import time


def get_data_from_discord_chat_exports_json_files(json_files_list: list, verbose: bool) -> list:
    """
    This function gets the raw data from the JSON files
    :param json_files_list: A list of JSON file paths
    :param verbose: If True, then show progress
    :return: A list of JSON data
    """
    # Start the timer
    start_time = time.time()
    # Create an empty list to store the data
    raw_data_list = []
    # Get the total number of JSON files
    total_number_of_json_files = len(json_files_list)
    # Print the message
    if verbose:
        print("----------------------------------------")
        print("Getting the data from the JSON files...")
    # Loop through the list of JSON files
    for json_file in json_files_list:
        if verbose:
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
    if verbose:
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


def main(json_files_list: list, verbose: bool) -> None:
    # Generate the docstring
    """
    This function gets the raw data from the JSON files
    :param json_files_list: A list of JSON file paths
    :param verbose: If True, then show progress
    :returns: None
    """

    data = get_data_from_discord_chat_exports_json_files(json_files_list, verbose)
    print(data)


if __name__ == '__main__':
    args = sys.argv

    number_of_args = len(args)
    json_files_path_list = []
    is_verbose = False

    for i in range(1, number_of_args):
        arg = args[i]
        if arg == "-v" or arg == "--verbose":
            is_verbose = True
        elif arg == "-i" or arg == "--input":
            json_file_path = args[i + 1]
            if os.path.isfile(json_file_path):
                json_files_path_list.append(json_file_path)
            else:
                print("ERROR: The JSON file path is invalid: " + json_file_path)
                sys.exit(1)
        elif arg == "-I" or arg == "--input-list":
            json_file_paths = args[i + 1:]
            for json_file_path in json_file_paths:
                if os.path.isfile(json_file_path):
                    json_files_path_list.append(json_file_path)
                else:
                    print("ERROR: The JSON file path is invalid: " + json_file_path)
                    is_continue = input("Do you want to continue? (y/N): ")
                    if is_continue.lower() != "y" or is_continue.lower()[0] != "y":
                        sys.exit(1)
    if len(json_files_path_list) == 0:
        print("ERROR: No JSON file paths were given")
        sys.exit(1)

    main(json_files_path_list, is_verbose)
