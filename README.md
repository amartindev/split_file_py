# CSV Splitter and Filter

This Python script is designed to split a large CSV file into smaller files, each containing a specified number of rows, and filter out rows based on specific criteria. Specifically, it filters rows where the `visits` column (position 7) is not equal to `'0.0'` or an empty string.

## Features

- Splits large CSV files into multiple smaller CSV files.
- Filters out rows where the `visits` column is either `'0.0'` or empty.
- Customizable number of rows per output file.
- Each output file contains the original CSV header.

## Requirements

- Python 3.x
- CSV file with UTF-8 encoding

## How to Use

1. Place your CSV file in the same directory as this script. The script assumes the file is named `Oral_large_file.csv`. If your file has a different name, update the `file_name` variable accordingly.

2. Install Python on your machine if you haven't already. You can download Python from [here](https://www.python.org/downloads/).

3. Run the script from the terminal or your preferred Python environment:

   ```bash
   python split_csv.py
4. The script will process the CSV file, filter out rows based on the condition for the `visits` column, and output smaller CSV files named `split_file_1.csv`, `split_file_2.csv`, etc.

Each output file will contain:
- The original header from the input CSV.
- Rows where the `visits` column (8th column, index 7) is not `'0.0'` or empty.

### Script Options

You can customize the script by modifying the following parameters:

- `file_name`: The name of the input CSV file.
- `num_rows`: The number of rows per output file. The default value is 999,000, but you can change this to suit your needs.

