##This code for selecting different items in a list, but between these 
##things you want to 
##select must is a \r 


import re
f=file('mac.txt')
data=f.readlines()
f.close()
#print data
#print data
for line in data :
    list1=line.split('\r')
#print python

def fun(list1):

    datadic=dict()
    for element in list1:
        datadic[element]=element
    return datadic.keys()
list2=fun(list1)
print list2
#d.write(list2)
#f.close