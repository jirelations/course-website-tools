# Original draft by ChatGPT Mar 23 Version.

import csv
import os

def create_text_documents(path="./", csv_file="files-to-create.csv", filename_column="filename", contents_column="contents"):
    # Open the CSV file
    with open(csv_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        # Loop through the rows in the CSV file
        for row in reader:
            # Get the filename and contents from the specified columns
            filename = row[filename_column]
            contents = row[contents_column]
            # Create the text document
            with open(os.path.join(path, filename), "w") as file:
                file.write(contents)

create_text_documents()
