#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Group Members: Laura Puckett and Scooter Nowark
"""

filenames = ["age","city","names","phone","state"]
myDirectory = "/Users/laurapuckett/Downloads/data/"

allContent = []
for filename in filenames:
    file = open(myDirectory + filename,'r')
    fileContent = [filename]
    for line in file.readlines():
        fileContent.append(line.strip('\n'))
    file.close()
    allContent.append(fileContent)

with open(myDirectory + 'output.csv','w') as f:
    for row in range(len(allContent[1])): # entries
        for listNum in range(len(allContent)): # categories
            if listNum != len(allContent)-1:
                f.write(allContent[listNum][row] + ",")
            else:
                f.write(allContent[listNum][row]) # don't want to add new column when on last category

        f.write('\n')