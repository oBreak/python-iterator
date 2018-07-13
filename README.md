# python-iterator

### Author(s)

- ... (6/2018)

### Development to occur

- Create handling for parameters for inputs to either specify the 
infile, outfile, or iteration process (if more than one exists)
- Add debugging functionality. 

### Usage
 
This is for iterating through items in python. 
The plan is to make this more generic so it can iterate through items
to perform specific functions with input and output files. 


##### Log parsing

Right now it is set up like a log parser, but additional functionality 
will be added. It will take relational path /in/ and search through items 
of type *.txt and *.log, looking for terms defined in the `term` variable. 
It will print these items to /out/

### Change Log

0.1 - 6/6/2018

- Successfully pulls .log and .txt files from the /in/ directory, reads lines, and returns each 
line containing the matched terms in a new /out/out file.

0.1.1 - 6/8/2018

- Pulled writing to the out file out of the 'iterate' function and placed in the out
function.
- Removed outdated elements related to group parsing for a specific outdated purpose.
- Moved processing to logical flow through the'main' function. Now it flows boot, inputs, iterate, out.
- Removed log parsing from iterate function to a new function 'matchterms'; this is used to find
matches in the .txt or .log files and append them to the parsedData variable.
- Added exact lines output to returned values.
- Added outbound file handling to append timestamp if file already exists. Time stamp added
is file-YYYYMMDD-HHMMSS.txt.

0.1.2 - 6//2018

- 

