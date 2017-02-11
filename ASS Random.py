a1 = int(raw_input("Dienst vandaag p1:"))
b1 = int(raw_input("Dienst vandaag p2:"))
overzicht = [11, 13, 15, 12, 14]
from random import randrange

def dienst_vandaag(a1):
    if a1 == 14:
        a2 = randrange(2, len(overzicht))
        a3 = overzicht[a2]
        del overzicht[a2]
        return a3
    elif a1 == 12:
        a2 = randrange(1, len(overzicht))
        a3 = overzicht[a2]
        del overzicht[a2]
        return a3
    else:
        a2 = randrange(len(overzicht))
        a3 = overzicht[a2]
        del overzicht[a2]
        return a3
a4 = dienst_vandaag(a1)
print "Dienst morgen p1 is %s" % (a4)
print overzicht

def dienst_vandaag_2(b1):
    if b1 == 14:
        b2 = randrange(2, len(overzicht))
        b3 = overzicht[b2]
        del overzicht[b2]
        return b3
    elif b1 == 12:
        b2 = randrange(1, len(overzicht))
        b3 = overzicht[b2]
        del overzicht[b2]
        return b3
    else:
        b2 = randrange(len(overzicht))
        b3 = overzicht[b2]
        del overzicht[b2]
        return b3
b4 = dienst_vandaag_2(b1)
print "Dienst morgen p2 is %s" % (b4)
print overzicht