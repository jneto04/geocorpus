import os
import sys

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

new_file = open(outputFileName, "w+", encoding="utf8")

with open(inputFileName, "r", encoding="utf8") as file:
    for line in file:
        if line != "\n":
            splited = line.split(" ")
            if splited[0] != '':
                line = line.strip()
                spliter = line.split(" ")
                token = spliter[0]
                tag_1 = spliter[1]
                tag_2 = spliter[2]
                new_file.write(str(token)+" "+str(tag_1)+" "+str(tag_2)+"\n")
        else:
            new_file.write("\n")
                
new_file.close()

print(" ")
print("--- CoNLL-02 METRICS EVALUATION ---")
print(" ")

os.system("perl conll.pl < %s"%(outputFileName))