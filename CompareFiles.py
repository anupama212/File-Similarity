# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:09:26 2022

@author: Anupama
"""
#import filecmp
  
  
# Path of first file
f1 = open("C:/Users/Anupama/Documents/file1.txt.txt")
  
# Path of second file
f2 = open("C:/Users/Anupama/Documents/file2.txt.txt")
   
i = 0
  
for line1 in f1:
    i += 1
      
    for line2 in f2:
          
        # matching line1 from both files
        if line1 == line2:  
            # print IDENTICAL if similar
            print("Line ", i, ": IDENTICAL")       
        else:
            print("Line ", i, ":")
            # else print that line from both files
            print("\tFile 1:", line1, end='')
            print("\tFile 2:", line2, end='')
        break
  
# closing files
f1.close()                                       
f2.close()        