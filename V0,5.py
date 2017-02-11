a1 = raw_input("Dienst vandaag p1:")
b1 = raw_input("Dienst vandaag p2:")
c1 = raw_input("Dienst vandaag p3:")
overzicht = [('91', 1), ('F1', 2), ('93', 3), ('95', 4), ('F3', 5), ('92', 6), ('94', 7), ('F2', 8)]
from collections import OrderedDict
overzicht = OrderedDict(overzicht)
a2 = overzicht[a1]
b2 = overzicht[b1]
c2 = overzicht[c1]

def dienst_vandaag(a2):
    if a2 <= 5:
        del overzicht['91']
        return "91"
    elif a2 == 6:
        del overzicht['93']
        return "93"
    else:
        del overzicht['95']
        return "95"
a3 = dienst_vandaag(a2)
ks = list(overzicht)
print "De dienst voor person1 morgen is %s" % (a3)

def dienst_vandaag_p2(b2):
    if b2 >= 7:
        if len(ks) >= 4:
            return ks[3]
        else:
            return ks[-1]
    elif b2 == 6:
        if len(ks) >= 3:
            return (ks[2])
        else:
            return ks[-1]
    else:
        return ks[0]
b3 = dienst_vandaag_p2(b2)
del overzicht[b3]
print "De dienst voor person2 morgen is %s" % (b3)

def dienst_vandaag_p3(c2):
    if c2 >= 7:
        if len(ks) >= 4:
            return ks[3]
        else:
            return ks[-1]
    elif c2 == 6:
        if len(ks) >= 3:
            return (ks[2])
        else:
            return ks[-1]
    else:
        return ks[0]
c3 = dienst_vandaag_p3(c2)
del overzicht[c3]
print "De dienst voor person3 morgen is %s" % (c3)
print overzicht