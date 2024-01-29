import sys
import csv

if len(sys.argv) == 3:
    try:
        with open(sys.argv[1], 'r') as file:
            reader = csv.DictReader(file)

            with open(sys.argv[2], 'w', newline='') as file_new:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(file_new, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    if row['column_name'] != 'value_to_remove':
                        writer.writerow(row)

        sys.exit(0)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    except Exception as e:
        sys.exit(f"Error: {e}")
else:
    sys.exit("Usage: python scourgify.py input_file.csv output_file.csv")
