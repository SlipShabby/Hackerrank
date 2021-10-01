# find xml

import xml.etree.ElementTree as etree

def get_attr_number(node):
    return etree.tostring(node).count(b'=')# your code goes here

# find max depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)
        
   
 

