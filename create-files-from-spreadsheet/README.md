# Create Files from Spreadsheet

Use a CSV spreadsheet (default name "files-to-create.csv") to create one file per row, using the name in the "filename" column and the contents in the "contents" column.

## Parameters

`path`: (default `./` [current directory]) Where the newly created files should be stored.
`csv_file`: (default `files-to-create.csv`) The CSV file to use to create the files.
`filename_column`: (default `filename`) Name of the column in the CSV specifying the names of the files to be created.
`contents_column`: (default `contents`) Name of the column in the CSV specifying the content of the files to be created.

## Usage

In Mac OS Terminal, `cd` to the directory of the script and do   
`$ python create_text_documents.py` to use default parameters or  
`$ python create_text_documents.py /path/to/folder my-files-to-create.csv filename_column_name contents_column_name` with custom parameters.