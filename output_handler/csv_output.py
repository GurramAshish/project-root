import csv

def write_to_csv(data, output_file):
    if len(data) > 0:
        keys = data[0].keys()
        with open(output_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
