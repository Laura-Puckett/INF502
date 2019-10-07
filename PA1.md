# Description

I broke this problem up into smaller functions. Each have specific roles that are explained below. 

## the main workflow functions
The main() function calls each other function and passes the necessary inputs.

The findMaxMatches(chainA, chainB, maxShift, method) function loops through all the integer values 
in the range (-maxShift, maxShift), calls the shift function to apply a shift to the chains, and the calls the appropriate
compare_chains_ function to find the number of matches for that shift. The information for the best shift is recorded
and returned after all iterations.

The print_output funtion prints the appropriate output according to the method, maximum shifts allowed,
and whether or not there were any matches.

## the smaller helper functions

The read_files() functions asks the user to input two filenames. It checks for potential errors such as
the file not existing, the file having at least one character, incorrect characters, and incorrect file type. 
The function will continue to prompt to user for filenames until an acceptable file has been provided. 

The get_chains() function calls the read_files() function. It loads the data from the files, and continue to
call read_files() until the user has provided to compatable files (meaning the chains are the same length).

The get_method() function prompts the user for the type of method that they want to use to match the chains.
The options are either the maximum number of matches, or the maximum contiguous length of matches. 

The getmaxShift(chainLength) function prompts the user for the maximum shift that is allowed (and continues 
to prompt until an integer value is provided). 
If the user gives a number greater than what is theoretically possible, then maxShift will be saved as the highest
possible. Otherwise it'll be saved as what the user inputs. 

The compare_chains_nMatch(chainA, chainB) function compares the two chains and returns 
the number of matching elements.

The compare_chains_nContig(chainA, chainB) function compares the two chains and returns 
the maximum contiguous matching elements.

The shift(chainA, chainB, shifter) function shifts the chains by the number of spaces equal to the value of "shifter". 
Positive and negative values of "shifter" result in a shift in different directions.


# Source Code
```

def read_files():
    path = '/Users/laurapuckett/Documents/INF502/'
    chainList = []
    for i in ['first','second']:
        Done = False        
        while Done is False:             
            filename = input('Enter the name of the text file that contains the ' + i + ' chain: ' )
            
            try:
                file = open((path + filename),'r')
                if filename[-4:] != '.txt':
                    raise ValueError
                    print('Not a .txt file. Must enter the name of a .txt file.')
                
            except (FileNotFoundError, ValueError):
                print(filename + ' does not exist.')
                
            else:
                content = file.read() 
                file.close()
                badChain = False
                for letter in content:
                    try:
                        if letter not in 'actgACTG':
                            raise ValueError()
                    except ValueError:
                        print('there is a "', letter, '" in fileA.')
                        print('Please provide another filename instead.')
                        badChain = True
                try:
                    if content == "":
                        raise ValueError()
                except ValueError:
                    print('The file is empty. Please provide a file with a chain.')
                    badChain = True
                    
                if badChain is False:
                    Done = True
                    chainList.append(content)
                    
    return chainList
                
            
def get_chains():
    chainsGood = False
    while chainsGood is False:
        try:
            chainList = read_files()
            chainA,chainB = chainList[0],chainList[1]
            if len(chainA) != len(chainB):
                raise ValueError
            
        except ValueError:
            print('ERROR, must provide chains of equal length')
            
        else:
            chainsGood = True
    return (chainA, chainB)

        
def getMethod():
    method = 0
    while (method != "nMatch" and method != "nContig"):
        print('What method do you want to use?')
        method = input('[1] Maximum Matches: '
                   '\n[2] Longest Continuous Match: ')
        if(method == "1"):
            method = 'nMatch'
        elif(method == "2"):
            method = 'nContig'
        else:
            print('You must enter "1" or "2" to select a method.')
            exit
    return method
    
        
def getmaxShift(chainLength):
    haveShift = False
    while haveShift == False:
        maxShift = input('Enter the maximum spaces that the chain is allowd to shift by: ')
        try:
            maxShift = abs(int(maxShift))
            if maxShift > (chainLength - 1):
                maxShift = chainLength - 1
        except ValueError:
            print('ERROR, you must provide an integer value')
        else:
            haveShift = True
    return maxShift


def compare_chains_nMatch(chainA, chainB):
    matches = 0
    for i in range(len(chainA)):
        if(chainA[i].upper() == chainB[i].upper()):
            matches = matches + 1
    return matches


def compare_chains_nContig(chainA, chainB):
    longestContig = 0
    contig = 0
    for i in range(len(chainA)):
        if(chainA[i] == chainB[i]):
            contig = contig + 1
            if (contig > longestContig):
                    longestContig = contig
        else:
            contig = 0
            
    return longestContig

    
def shift(chainA, chainB, shifter):
    if shifter > 0:
        newchainA = '-'*shifter + chainA
        newchainB = chainB + '-'*shifter
    else:
        newchainA = chainA + '-'*abs(shifter)
        newchainB = '-'*abs(shifter) + chainB
    return (newchainA, newchainB)

    
def findMaxMatches(chainA, chainB, maxShift, method):
    maxMatches = 0
    bestShift = 'NA'
    if maxShift >0:
        for shiftNum in range(-1*maxShift, maxShift):
            shiftedA, shiftedB = shift(chainA, chainB, shiftNum)
            if(method == 'nMatch'):
                matches = compare_chains_nMatch(shiftedA, shiftedB)  
                
            elif(method == 'nContig'):
                matches = compare_chains_nContig(shiftedA, shiftedB)
                
            if matches >= maxMatches:
                maxMatches = matches
                bestShift = shiftNum
                bestShiftedA = shiftedA
                bestShiftedB = shiftedB
    else:
        if(method == 'nMatch'):
            matches = compare_chains_nMatch(chainA, chainB)  
                
        elif(method == 'nContig'):
            matches = compare_chains_nContig(chainA, chainB)
        
        maxMatches = matches
        bestShift = 0
        bestShiftedA, bestShiftedB = chainA, chainB
            
    return (maxMatches, bestShift, bestShiftedA, bestShiftedB)


def printOutput(method, maxMatches, maxShift, bestShift, bestShiftedA, bestShiftedB, chainA, chainB):
    print('\n-------------RESULTS-------------')
    print('\nWhen there is a maximum shift of ' + str(maxShift) + ' spaces, ')

    if(method == 'nMatch'):
        print('The maximum number of matches is: ' + str(maxMatches))
    
    elif(method == 'nContig'):
        print('\nThe longest contiguous matching chain length is: ' + str(maxMatches))
    
    if (maxMatches > 0 and abs(bestShift) > 0):
    
        if(bestShift >0):
            print('\nAn example of when this occurs is when')
            print('the first chain is shifted ' + str(bestShift) + ' spaces to the right.')

    
        else:
            print('\nAn example of when this occurs is when')
            print('the first chain is shifted ' + str(abs(bestShift)) + ' spaces to the left.')

    
        print('\nThe chain combination with this shift is: ')
        print(bestShiftedA)
        print(bestShiftedB)
        
    else:
        if(maxMatches > 0 and bestShift == 0):
            print('\nAn example of when this occurs is when there is no shift.')
        print('\nThe original chains are: ')
        print(chainA)
        print(chainB)


def main():
    chainA, chainB = get_chains()
    chainLength = len(chainA)

    method = getMethod()
    
    maxShift = getmaxShift(chainLength)
    
    maxMatches, bestShift, bestShiftedA, bestShiftedB = findMaxMatches(chainA, chainB, maxShift, method)
    printOutput(method, maxMatches, maxShift, bestShift, bestShiftedA, bestShiftedB, chainA, chainB)

main()
```
# example runs
## maximum matches example
```
Enter the name of the text file that contains the first chain: string1.txt

Enter the name of the text file that contains the second chain: string2.txt
What method do you want to use?

[1] Maximum Matches: 
[2] Longest Continuous Match: 1

Enter the maximum spaces that the chain is allowd to shift by: 4

-------------RESULTS-------------

When there is a maximum shift of 4 spaces, 
The maximum number of matches is: 8

An example of when this occurs is when
the first chain is shifted 1 spaces to the right.

The chain combination with this shift is: 
-AGTCTATACGA
CAGTTTATCCG-
```

## maximum contiguous chain example
```
Enter the name of the text file that contains the first chain: testcontig1.txt

Enter the name of the text file that contains the second chain: testcontig2.txt
What method do you want to use?

[1] Maximum Matches: 
[2] Longest Continuous Match: 2

Enter the maximum spaces that the chain is allowd to shift by: 6

-------------RESULTS-------------

When there is a maximum shift of 6 spaces, 

The longest contiguous matching chain length is: 4

An example of when this occurs is when
the first chain is shifted 4 spaces to the left.

The chain combination with this shift is: 
ACTCGTACCCTA----
----ATACCAACGCGT
```

## error handling 
The program continues to prompt the user for information when there is an error. This section represents a _single_ run of the program. The code is broken up with headers to emphasize different types of error handling in this single run.

#### file doesn't exist
```
Enter the name of the text file that contains the first chain: 
notafile.txt
ERROR: the file: notafile.txt does not exist.
Enter the name of the text file that contains the first chain: 
```
#### different length of chains

```
7Cs.txt

Enter the name of the text file that contains the second chain: 
6Cs.txt
ERROR, must provide chains of equal length
Enter the name of the text file that contains the first chain: 
```
#### incorrect values in file (numbers, letters other than ACTG)
```
aBadLetter.txt
ERROR: there is a " x " in fileA.
Please provide another filename instead.

Enter the name of the text file that contains the first chain: 
aNumber.txt
ERROR: there is a " 3 " in fileA.
Please provide another filename instead.

Enter the name of the text file that contains the first chain: 
7mixed.txt

Enter the name of the text file that contains the second chain: 
7Cs.txt
What method do you want to use?
```
#### invalid input for selecting method

```
[1] Maximum Matches: 
[2] Longest Continuous Match: 
3
You must enter "1" or "2" to select a method.
What method do you want to use?
[1] Maximum Matches: 
[2] Longest Continuous Match: 
1
```

#### invalid input for max shift
```
Enter the maximum spaces that the chain is allowed to shift by: 
5 spaces
ERROR, you must provide an integer value

Enter the maximum spaces that the chain is allowed to shift by: 
5
```

### and finally, with valid user input for everything, the code can finish running
```
-------------RESULTS-------------

When there is a maximum shift of 5 spaces, 
The maximum number of matches is: 2

An example of when this occurs is when
the first chain is shifted 3 spaces to the right.

The chain combination with this shift is: 
---ACTCGTA
CCCCCCC---
```

NEED TO ADD EXAMPLE RUNS!!
# Discussion of hurdles/issues
