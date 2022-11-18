#!/usr/bin/env python
from pprint import pprint

def getlines(filename):
    with open(filename, 'r') as rfile:
        lines = rfile.readlines()
    xlines = []
    for line in lines:
        xline = line.strip()
        xlines.append(xline)
    alines = []
    for line in xlines:
        alne = line[:-1]
        alines.append(alne)    
    return alines
            


def get_column_names(flines):
    mycolumnnames = []
    mycols = []
    
    mycol = []
    
    for colname in str(flines[0]).split(","):
        x = colname.strip()
        if x == "\n":
            continue
        elif x == "":
            continue
        
        mycol.append(x)
    
    for item in str(flines[0]).split(","):
        if item == "\n" or item == None:
            continue
        mycolumnnames.append(item)
    return mycolumnnames
    
def make_sheet(lines, column_names):
    sheet = {}
    
    for index, line in enumerate(lines):
        
        row = {}
        
        for col_index, col_name in enumerate(column_names):
            
            myvalues = enumerate(str(line).split(","))
            
            row[str(index)] = {}
            
            row[str(index)][str(col_name)] = str(myvalues[col_index])
        sheet[str(index)] = row
    
    return sheet

def read_csv(filename):
    
    csv_lines = getlines(filename)
    
    my_columns = get_column_names(csv_lines)
    
    sheet = make_sheet(csv_lines, my_columns)
    
    pprint(sheet)     

read_csv('data.csv')