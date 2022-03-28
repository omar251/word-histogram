import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import re
import xlwt

filename = "/Users/omarezzat/Documents/GitHub/text.txt"
filename2 = "/Users/omarezzat/Documents/GitHub/out.txt"

fr = open(filename, "r")
y= fr.read()
y = re.sub(r"[^a-z0-9 ]","",y.lower())
l= y.split(' ')

count = 0
x=0
z=0
size = len(l)
out = list(set(l))
outsize = len(out)
a=[]
s=""
while x < outsize:
    z = 0 
    count = 0
    
    while z < size:
        if out[x]==l[z]:
            count = count + 1
        z = z + 1

    a.append([out[x],count])
    s = s + out[x]+" "+str(count)+"\n"
    x = x + 1
    
a = sorted(a,key=lambda l:l[1], reverse=True)
objects = [ q[0] for q in a]
y_pos = np.arange(len(objects))
performance = [ qw[1] for qw in a]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xticks(fontsize=5, rotation=90)
plt.ylabel('Usage')
plt.title('Word usage')
 
plt.show()
s = ""
for h in range(len(a)):
    s = s +str(a[h][1]) +"           "+a[h][0]+"\n"
fr.close()
fw = open(filename2,"w")
fw.write(s)
fw.close()



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

wb.save('/Users/omarezzat/Documents/GitHub/out.xls')