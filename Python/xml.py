# find xml

import xml.etree.ElementTree as etree


def get_attr_number(node):
    return etree.tostring(node).count(b'=')# your code goes here