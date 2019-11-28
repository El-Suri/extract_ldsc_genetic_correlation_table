# Extract LD score regression log table

Creates a CSV table from the table in the [LD Score Regression](https://github.com/bulik/ldsc) log output file.

To run at the command line type:

`python extract_ldsc_log_table.py -f <path_to_your_log_file>` 

Options are:

 -f --file      specify path to your log file (mandatory)

 -v --verbose   prints processing steps and tables to the command line (optional)

 -h --help      prints options and description before closing (optional)
             

Requirements: python 3*, pandas
* may work with later versions of python 2, will work with all the dependencies needed for ldsc anyway.

