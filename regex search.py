print("Name   : prajwal  br") 
print("USN    : 1AY24AI083") 
print("Section: O") 
import os, re 
pattern = input("Enter a regex pattern: ") 
regex = re.compile(pattern) 
for filename in os.listdir(): 
if filename.endswith('.txt'):                                                                                              
with open(filename) as f: 
for line in f: 
if regex.search(line): 
print(f"{filename}: {line.strip()}")   
