import json
import csv

def json_to_csv(data, csv_filename):
    # Extract field names from the first JSON object
    field_names = list(data[0].keys())

    # Write data to CSV
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        # Write the header (field names) to the CSV file
        writer.writeheader()

        # Write the JSON data to the CSV file
        for row in data:
            writer.writerow(row)