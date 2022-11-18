import os
from pprint import pprint
from dataclasses import dataclass
import timeit

start = timeit.timeit()

start1 = start 


def get_lines(filename):
    csvfile = open(filename, 'r')
    lines = csvfile.readlines()
    return lines

def get_column_names(file_lines):
    lines = file_lines
    column_names = lines[0].split(",")
    column_keys = column_names[:-1]
    return column_keys

def read2dict(file):
    rows={}
    lines = get_lines(file)
    columnnames = get_column_names(lines)
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
    return rows

@dataclass(slots=True)
class Cell:
    value: str
    row: int
    column: str
    column_index: int
    
@dataclass(slots=True)
class Column:
    index: int
    name: str

@dataclass(slots=True)
class Row:
    ncolumns: int
    row: int
    values: list
    column_names: list
    
    
    def setup(self):
        val = enumerate(self.values)
        name = enumerate(self.column_names)
        self.column = {}
        self.value = {}
        for index, x in val:
            cname = name[index]
            self.value[cname] = x
            self.column[cname] = x
        
    
    
        
        

class Table:
    
    def __init__(self, filename: str, table_name: str):
        
        self.name = table_name
        self.file = filename
        self.settings = {}
        self.lines = self._getLines()
        self.column_names = self._getColumnNames()
        self.rows = self._getRows()
        
    
    def _getLines(self):
        csvfile = open(self.file, 'r')
        self.lines = csvfile.readlines()
        return self.lines
    
    def _getColumnNames(self):
        lines = self.lines
        column_names = lines[0].split(",")
        column_keys = column_names[:-1]
        self.column_names = column_keys
        self.column = {}
        for index, x in enumerate(self.column_names):
            self.column[x] = index
        return self.column_names
    
    def _getRows(self):
        self.row={}
        for index, line in enumerate(self.lines):
            listvalues = line.split(",")
            values = listvalues[:-1]
            myline_string_reference = str(index)
            self.row[myline_string_reference] = {}
            for column_value_name in self.column_names:
                self.row[myline_string_reference][column_value_name] = {}
            for value_index, val in enumerate(values):
                value_reference = str(self.column_names[value_index])
                self.row[myline_string_reference][value_reference] = val
    
    def showProperties(self):
        
        self.magic = {}
        self.props = {}
        for x in vars(self):
            
            if x.startswith("__"):
                self.magic[x] = self.__dict__[x]
            else:
                self.props[x] = self.__dict__[x]
                
        with open("debug",'w') as debugfile:
            
            for x in self.props.keys():
                debugfile.write(f"{str(self.props[x])}\n")
            
    
    def showDirs(self):
        
        pprint(dir(self))
    
    def showVariables(self):
        
        pprint(vars(self))
        
    

sheet = Table('data.csv', 'data')

sheet.showProperties()

end = timeit.timeit()
print(start, end)
dtime = abs(start-end)
print(dtime)
#sheet.showVariables()

effiency = (0.029857780995371286/0.04796340601023985)*100

print(effiency)
