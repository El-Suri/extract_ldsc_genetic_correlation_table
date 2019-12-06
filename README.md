# Extract LD score regression genetic correlation log table `v1.0.1`


### What does it do?
Creates a CSV table from the table in the [LD Score Regression](https://github.com/bulik/ldsc) geenetic correlation log output file.

### How do I do it?
To run at the command line type:

`python extract_ldsc_log_table.py -f <path_to_your_log_file>` 

Options are:

 -f --file      specify path to your log file (required)

 -v --verbose   prints table to the command line (optional)

 -h --help      prints options and description before closing (optional)
 
 -o --output    specify output file name, default is the input file name plus _table.csv (optional)
 
 
 ### What do I need?
 
 * python3 
 * pandas package
 * LDSC log output 
             
