# products_csv_parser

import csv
import argparse

parser = argparse.ArgumentParser(description='Read a file and pass it to csv reader')
parser.add_argument('filename', help='The csv file to read')
# parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
# parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()


# Trial and error is real hehehe (^_^)
# input_file = 'sample_products.csv'

output_file = input("What will be the filename?").lower() + ".csv"

with open(args.filename, newline='') as inp, open(output_file, 'w', newline='') as out:
	# reader = csv.reader(inp)
	writer = csv.writer(out)	
	for row in csv.reader(inp):
		if row[25] != "":
			writer.writerow(row)

print("Successful!")