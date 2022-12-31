import os
import glob
import re
import sys
import argparse
import pprint
import pdb

FILENAME_PREFIX = 'sbc'
FILENAME_PATTERN = 'sbc-android-staging[a-z0-9A-Z]+.txt'

ERRORS_FOUND = {}

ERRORS_TO_FIND = ['ERROR [TurboConnectSDK | Log]: ']

def get_list_of_files(dir_name):
    full_path = os.path.join(dir_name, '**', FILENAME_PREFIX+'*')
    files = glob.glob(full_path, recursive=True)
    files_matched = [f for f in files if re.search(FILENAME_PATTERN, f)]
    return files_matched


def open_file(file_path):
    lines = []
    sbc_file = dlt.load(file_path)
    for msg in sbc_file:
        lines.append(msg.payload_decoded)
    return lines


def open_others(file_path):
    fd = open(file_path, 'r')
    lines = fd.readlines()
    return lines


def find_errors_in_file(file_path, crash_string):
    counter = 0
    errors_found = []

    if file_path.endswith(".txt"):
        lines = open_file(file_path)
    else:
        lines = open_others(file_path)

    for line in lines:
        counter += 1
        if crash_string in line:
            errors_found.append((counter, line))

    return errors_found


def print_errors_summary(crash_mapping):
    report = ""
    for elem in crash_mapping.keys():
        data = crash_mapping[elem]
        if data['count'] != 0:
            report += "{}: found {} times".format(elem, data['count'])
            report += "\n"
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='****** This Script finds error strings in files ******')
    parser.add_argument('--logs_folder', type=str, help="Where should I search for files")
    parser.add_argument('--output_file', type=str, help="Where to log stuff")

    args = parser.parse_args()
    if not args.logs_folder:
        raise ValueError("Missing mandatory argument --logs_folder")
    if not args.output_file:
        raise ValueError("Missing mandatory argument --output_file")


    # count errors
    ERROR_COUNT = 0
    #here we store crash string mapping to count and files
    errors_map = {}

    files = get_list_of_files(args.logs_folder)
    if len(files) == 0:
        raise ValueError('No files found to search in')

    for log_file in files:
        for crash_string in ERRORS_TO_FIND:
            errors_map.setdefault(crash_string, {'count': 0})
            errors_in_file = find_errors_in_file(log_file, crash_string)
            if errors_in_file:
                errors_map[crash_string]['count'] += len(errors_in_file)
                errors_map[crash_string][log_file] = len(errors_in_file)
                ERRORS_FOUND.setdefault(log_file, [])
                ERROR_COUNT += len(errors_in_file)
                ERRORS_FOUND[log_file].extend(errors_in_file)

    print("Errors count is: {}".format(ERROR_COUNT))
    report_summary = print_errors_summary(errors_map)
    print(report_summary)

    with open(args.output_file, 'w') as logs:
        logs.write("Found: {}\n".format(ERROR_COUNT))
        logs.write(report_summary)
