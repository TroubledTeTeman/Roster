dict = [('91', 1), ('F1', 2), ('93', 3), ('95', 4), ('F3', 5), ('92', 6),('94', 7), ('F2', 8)]
from collections import OrderedDict
dict = OrderedDict(dict)
mylist = list(dict)
del dict[mylist[0]]
print dict
