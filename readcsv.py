import os
from pprint import pprint


def read2dict(file):
    
    csvfile = open(file, 'r')
    
    lines = csvfile.readlines()
    
    column_names = lines[0].split(",")
    
    columnnames = column_names[:-1]
    
    print(columnnames)
    
    rows = {}
    
    for index, line in enumerate(lines):
        
        listvalues = line.split(",")
        
        values = listvalues[:-1]
        
        myline_string_reference = str(index)
        
        rows[myline_string_reference] = {}
        
        for column_value_name in columnnames:
            rows[myline_string_reference][column_value_name] = {}
        
        for value_index, val in enumerate(values):
        
            value_reference = str(columnnames[value_index])
        
            rows[myline_string_reference][value_reference] = val
    
    pprint(rows)
        
        
        
    
read2dict('data.csv')
    
    