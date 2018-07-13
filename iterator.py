#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

'''
Program intended to iterate through data to pull out relevant bits.
Program requires no additional installed modules. Can be run in either Python 2.7, 3.5, or 3.6

Please see readme.md for relevant usage instructions.

This is version 0.1.1

'''

#Importing libraries

import os
import sys
import time

from os import listdir
from pathlib import Path

# Set to True to print detailed output, False to be quiet
home            = str(Path.home())
debug           = False
parsedData      = []
errorMessages   = []
fileDir         = os.path.dirname(os.path.realpath('__file__'))
outfile         = os.path.join(fileDir, 'out/out.txt')
mypath          = home + "/Projects/bitbucket-python-iterator/in/"
relpath         = ""
outpath         = ""
rGroups         = 0
group           = 1
aNum            = 0
terms           = ['error','term2']
lineBreaks      = str('\n')

#make readable

try:
    arg =	sys.argv[0]
except IndexError:
    print
    print('IndexError reading argument 1. Please specify argument.')
    exit()
    #arg = '2.1.1.1'

def setPath():
    print()
    print('Do you want to set a custom path for the input (Press "Enter" to skip)?')
    yon = yesOrNo()
    print()
    valid = False
    if yon == True:
        while(valid == False):
            print('Example path for Mac would be "/Users/example/Desktop/files/"')
            print('What path would you like to pull the log files from?')
            pathNew = input()
            pathNew = str(pathNew)
            try:
                for f in listdir(pathNew):
                    if f.find(".log") or f.find(".txt"):
                        valid = True
                        print('Directory is valid and log files are present.')
                        print()
                        return pathNew
            except FileNotFoundError:
                print('File or directory not found.')
    else:
        return mypath

def yesOrNo(): #Determines yes or no. Passes back True for yes, False for no.
    while True:
        again = input()
        if (again in ['y','ye','yes','YES','Yes','Ye','1']):
            return True
        elif (again in ['n','no','NO','No','0','']):
            return False
        else:
            print('Input not valid. Please enter yes or no:')

def myprint(data):
  if debug is True:
    print(data)
  # else not debug, print nothing

# create a list of all .log files in current dir
def findInputs():
    inputFiles = []
  # check every file in path
    for f in listdir(mypath):
    # .log or .txt should be the last 4 chars of the filename
        if f.find(".log", len(f) - 4) != -1:
            inputFiles.append(f)
        elif f.find(".txt", len(f) - 4) != -1:
            inputFiles.append(f)
  # if none of the files were .log files, print error and bail
    if len(inputFiles) == 0:
        print("Couldn't find any .log or .txt files in the", mypath  ,"directory!")
        exit()
    print('Identifying inputs:')
    print()
    for i in inputFiles:
        print('\t' + i)
    print()
    return inputFiles

def BootUp():
    os.system('clear')
    print('======================================')
    print('=== Beginning Sequential Iteration ===')
    print('======================================')
    print()
    return

def groupSize():
    print('Please enter the size of each group: ')
    j = input()
    return j

def countGroupsPerFile(i):
    x = int(len(i)/size)+1
    return x

def matchterms(x):
    for j in terms:
        if x.find(j) != -1:
            parsedData.append(x)
        else:
            pass
    else:
        pass

    return x

def iterate(inputFile): # Modular (?) iteration over the input files.

    print("\tParsing entry criteria: " + '\t' + (mypath + inputFile))
    try:
        g = open((mypath + inputFile),'r')
    except:
        print("Failed to open file " + inputFile)
        exit()
    # read in the log, strip newlines
    log = g.readlines()
    log = [x.strip('\n') for x in log]
    g.close()
    print('\t' + str(len(log)), 'lines found.')
    print('\tWriting to parsedData.')
    print()
    for line in log:
        matchterms(line)
    #print (parsedData)
    return


def main():
    BootUp()
    '''Remove comment tag from below line if running from the command line and specifying input directory.
    This should be changed in a later version to accept arguments from the command line (or IDE) 
    that specify input and output paths.'''
	# mypath = setPath()
    inputFiles = findInputs()
    for i in inputFiles:
        iterate(i)
    out()

def out():
    print('================')
    print('==Begin output==')
    print('================')
    n = 0
    global outfile
    if os.path.isfile(outfile):
        print(outfile + ' exists; appending timestamp to written file.')
        timestr = time.strftime("%Y%m%d-%H%M%S")
        outfilefull = str(outfile)
        outfiletype = outfilefull[-4:]
        outfilename = outfilefull[:(len(outfilefull)-4)]
        outfilefull = outfilename + '-' + timestr + outfiletype
        print(outfilefull)
        outfile = os.path.join(fileDir, outfilefull)


    try:
        f = open(outfile, 'a')
        print('')
        print('\tSetting output file,', outfile)
        print('')
    except:
        print("\tFailed to open output file!")
        f.close()
    for j in parsedData:
        f.write(j)
        f.write(lineBreaks) #This is to add a new line at the end of each line of the log or text file.
        n = n + 1
        if n % 100 == 0:
            print('\tWriting outputs: ' + str(n) + ' lines complete.')
        else:
            pass
    else:
        pass
    print('\tOutput complete: ' + str(n) + ' lines written.')
    print('\n')
    return

#	Start main program

main()
