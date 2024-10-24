import csv

def split_csv(file_name, num_rows=999000):
	with open(file_name, 'r', newline='', encoding='utf-8') as input_csv:
		csv_reader = csv.reader(input_csv)
		header = next(csv_reader)

		file_counter = 1
		rows = []

		for i, row in enumerate(csv_reader, start=1):

			visits = row[7].strip()
			if visits != '0.0' and visits != '':
				rows.append(row)

			if len(rows) >= num_rows:
				output_file_name = f'split_file_{file_counter}.csv'
				with open(output_file_name, 'w', newline='', encoding='utf-8') as output_csv:
					csv_writer = csv.writer(output_csv)
					csv_writer.writerow(header)
					csv_writer.writerows(rows)
				file_counter += 1
				rows = []

		if rows:
			output_file_name = f'split_file_{file_counter}.csv'
			with open(output_file_name, 'w', newline='', encoding='utf-8') as output_csv:
				csv_writer = csv.writer(output_csv)
				csv_writer.writerow(header)
				csv_writer.writerows(rows)

file_name = 'Oral_large_file.csv'
split_csv(file_name)