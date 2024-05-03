#!/usr/bin/python3

'''
script that reads stdin line by line
and computes metrics
'''
import sys
import re
import signal

regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b \- \[(?:\d{4})\-(?:\d{2})\-(?:\d{2})'
' (?:\d{1,2})\:(?:\d{1,2})\:(?:\d{1,2})\.(?:\d{1,6})\]'
' \"GET \/projects\/260 HTTP\/1.1" (?:\d{3}) (?:\d{3})'
regex2 = r'\b(\d+)\s+\d+$'
regex3 = r'\b\d+$'


def signal_handler(sig, frame):
    calculation(file_size, status_dict)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def calculation(file_size, status_dict):
    S = 0
    for data in file_size:
        S += int(data)
    print(f'File size: {S}')
    for key in status_dict:
        print(f'{key}: {len(status_dict[key])}')


while True:
    status_dict = {}
    file_size = []
    i = 0

    for line in sys.stdin:
        i += 1
        line = line.strip()
        match = re.match(regex, line)
        if match:
            status_code_match = re.search(regex2, line)
            file_size_match = re.search(regex3, line)
            if status_code_match:
                status_code = status_code_match.group()
                status_code = status_code[:3]
                if status_code not in status_dict:
                    status_dict[status_code] = []
                status_dict[status_code].append(line)
            if file_size_match:
                file_size.append(file_size_match.group())
        if i == 10:
            break

    calculation(file_size, status_dict)
