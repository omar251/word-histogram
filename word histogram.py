#!/usr/local/bin
import os,sys
os.system('cls||clear')
print(sys.version +"\n")
print(sys.executable)

import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import xlwt

count = 0; i=0; j=0; a=[] ;s=""

# READ TEXT FROM FILE

Path = "/Users/omarezzat/myGITrepo/word-histogram/"
filename1 = Path+"text.txt"
filename2 = Path+"out.txt"
fr = open(filename1, "r")
text = fr.read()

# EXTRACT WORDS FROM TEXT

text = re.sub(r"[^a-z0-9 ]","",text.lower())
textj = text.split(' ')
wordlist = list(dict.fromkeys(textj))

# COUNT WORDS IN TEXT

while i < len(wordlist):
    j = 0 ;count = 0  
    while j < len(textj):
        if wordlist[i]==textj[j]:
            count += 1
        j += 1
    a.append([wordlist[i],count])
    s = s + wordlist[i]+" "+str(count)+"\n"
    i+=1

# PLOT ARRAY A

a = sorted(a,key=lambda l:l[1], reverse=True)
objects = [ q[0] for q in a]
y_pos = list(range(len(objects)))
performance = [ qw[1] for qw in a]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xticks(fontsize=10, rotation=90)
plt.ylabel('Usage')
plt.title('Word usage')
plt.show()

# SAVE DATA TO TEXT OUT
s = ""
for h in range(len(a)):
    s = s +str(a[h][1]) +"           "+a[h][0]+"\n"
fr.close()
fw = open(filename2,"w")
fw.write(s)
fw.close()

# SAVE DATA TO EXCEL OUT
wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet 1')
first_row = 0
# write each item in the list to consecutive columns on the first row
for index, item in enumerate(objects):
        ws.write(first_row, 0, item) 
        first_row = first_row + 1
first_row = 0
for index, item in enumerate(performance):
        ws.write(first_row, 1, item) 
        first_row = first_row + 1

wb.save(Path+"out.xls")
