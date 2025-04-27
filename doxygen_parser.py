import csv
import re
import sys

def parse_doxygen_log(log_file_path, output_csv_path="doxygen_warnings.csv"):
    warning_pattern = re.compile(r'^(.*?):(\d+):\s+warning:\s+(.*)$')

    with open(log_file_path, 'r') as log_file, open(output_csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['File', 'Line', 'Message'])

        for line in log_file:
            match = warning_pattern.match(line.strip())
            if match:
                file_path, line_number, message = match.groups()
                writer.writerow([file_path, line_number, message])

    print(f"Parsed warnings written to: {output_csv_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python doxygen_log_parser.py <doxygen_warnings.log>")
    else:
        parse_doxygen_log(sys.argv[1])
