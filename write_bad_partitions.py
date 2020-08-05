# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:16:43 2020

@author: Suha Naser-Khdour
"""

import codecs
import pandas as pd
import sys

def compare(All,table,Fail):
    '''
    input
        All: is the file with all the partitions (PARTITION_FILE) in Nexus format
        table: is the csv output file from IQ-TREE with the MaxSym test results
    output
        Fail: is the file that contains all the partitions that failed the MaxSym test
    '''
    df = pd.read_csv(table, comment='#')
    bad_part = df.loc[df.SymPval < 0.05].Name.values
    with open(All,'r') as inf, codecs.open(Fail,'w', "utf-8-sig") as outf:
        outf.writelines('#NEXUS\n')
        outf.writelines('begin sets;\n')            
        for line in inf:
            if any(word in line for word in bad_part):
                outf.write(line)
        outf.writelines('#end;\n')
    return

def FailedPart():
        
    if len(sys.argv) == 1:
        raise SystemExit('Error: No files were detected')
    elif len(sys.argv) == 2:
        raise SystemExit('Error: some files are missing')
    elif len(sys.argv) == 3:
        raise SystemExit('Error: some files are missing')    
    elif len(sys.argv) > 4:
        raise SystemExit('Error: too many arguments')
    compare(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    FailedPart()