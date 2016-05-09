#This program can collect target mac address and put them in a same file.

import re
f=file('Aisle1 copy.txt')
data=f.readlines()
f.close()
#print data

for line in data :
    python=line.split('\r')
#    print python # you will get a list, each element is divided my \r
#results=[]
#python=results.append()

def write():
	for each_item in python:
			try:
				m=re.findall(e,each_item)
				d=file(e,'a')
				if m:
#			new_item=each_item, '\n'
					d.write(each_item)
					d.write('\r')
			except:
				pass
	d.close()
		#print each_item
e='1c:aa:07:7b:28:00'
write()
e='1c:aa:07:7b:28:01'
write()

#return for function is not necessary