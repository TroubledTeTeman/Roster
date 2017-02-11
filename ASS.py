a1 = raw_input("Dienst vandaag p1:")
b1 = raw_input("Dienst vandaag p2:")
c1 = raw_input("Dienst vandaag p3:")
d1 = raw_input("Dienst vandaag p4:")
e1 = raw_input("Dienst vandaag p5:")
overzicht = [('11', 1), ('13', 2), ('15', 3), ('12', 4), ('14', 5)]
from collections import OrderedDict
overzicht = OrderedDict(overzicht)
a2 = overzicht[a1]
b2 = overzicht[b1]
c2 = overzicht[c1]
d2 = overzicht[d1]
e2 = overzicht[e1]

#shift for tomorrow
def dienst_vandaag(a2):
    if a2 <= 3:
        return '11'
    elif a2 == 4:
        return '13'
    else:
        return '15'
a3 = dienst_vandaag(a2)
print "De dienst voor person1 morgen is %s" % (a3)
del overzicht[a3]
ks = list(overzicht)
print overzicht

def dienst_vandaag_p2(b2):
    if b2 == 5:
        if len(ks) >= 3:
            return ks[2]
        else:
            return ks[-1]
    elif b2 == 4:
        if len(ks) >= 2:
            return ks[1]
        else:
            return ks[-1]
    else:
        return ks[0]
b3 = dienst_vandaag_p2(b2)
print "De dienst voor person2 morgen is %s" % (b3)
del overzicht[b3]
ks = list(overzicht)
print overzicht

def dienst_vandaag_p3(c2):
    if c2 == 5:
        if len(ks) >= 3:
            return ks[2]
        else:
            return ks[-1]
    elif c2 == 4:
        if len(ks) >= 2:
            return ks[1]
        else:
            return ks[-1]
    else:
        return ks[0]
c3 = dienst_vandaag_p3(c2)
print "De dienst voor person3 morgen is %s" % (c3)
del overzicht[c3]
ks = list(overzicht)
print overzicht

def dienst_vandaag_p4(d2):
    if d2 == 5:
        if len(ks) >= 3:
            return ks[2]
        else:
            return ks[-1]
    elif d2 == 4:
        if len(ks) >= 2:
            return ks[1]
        else:
            return ks[-1]
    else:
        return ks[0]
d3 = dienst_vandaag_p4(d2)
print "De dienst voor person4 morgen is %s" % (d3)
del overzicht[d3]
ks = list(overzicht)
print overzicht

def dienst_vandaag_p5(e2):
    if e2 == 5:
        if len(ks) >= 3:
            return ks[2]
        else:
            return ks[-1]
    elif e2 == 4:
        if len(ks) >= 2:
            return ks[1]
        else:
            return ks[-1]
    else:
        return ks[0]
e3 = dienst_vandaag_p5(e2)
print "De dienst voor person5 morgen is %s" % (e3)
del overzicht[e3]
ks = list(overzicht)
print overzicht

print

aa1 = b3
bb1 = c3
cc1 = d3
dd1 = e3
ee1 = a3
overzicht = [('11', 1), ('13', 2), ('15', 3), ('12', 4), ('14', 5)]
from collections import OrderedDict
overzicht = OrderedDict(overzicht)
aa2 = overzicht[aa1]
bb2 = overzicht[bb1]
cc2 = overzicht[cc1]
dd2 = overzicht[dd1]
ee2 = overzicht[ee1]

# shifts for day after tomorrow
def dienst_morgen_p2(aa2): #person2 overmorgen
    if aa2 <= 3:
        return '11'
    elif aa2 == 4:
        return '13'
    else:
        return '15'
aa3 = dienst_morgen_p2(aa2)
print "De dienst voor person2 overmorgen is %s" % (aa3)
del overzicht[aa3]
ks = list(overzicht)
print overzicht

def dienst_morgen_p3(bb2): #person3 overmorgen
    if bb2 == 5:
        if len(ks) >= 3:
            return ks[2]
        else:
            return ks[-1]
    elif bb2 == 4:
        if len(ks) >= 2:
            return ks[1]
        else:
            return ks[-1]
    else:
        return ks[0]
bb3 = dienst_morgen_p3(bb2)
print "De dienst voor person3 overmorgen is %s" % (bb3)
del overzicht[bb3]
ks = list(overzicht)
print overzicht

def dienst_morgen_p4(cc2): #person4 overmorgen
    if cc2 == 5:
        if len(ks) >= 3:
            return ks[2]
        else:
            return ks[-1]
    elif cc2 == 4:
        if len(ks) >= 2:
            return ks[1]
        else:
            return ks[-1]
    else:
        return ks[0]
cc3 = dienst_morgen_p4(cc2)
print "De dienst voor person4 overmorgen is %s" % (cc3)
del overzicht[cc3]
ks = list(overzicht)
print overzicht

def dienst_morgen_p5(dd2): #person5 overmorgen
    if dd2 == 5:
        if len(ks) >= 3:
            return ks[2]
        else:
            return ks[-1]
    elif dd2 == 4:
        if len(ks) >= 2:
            return ks[1]
        else:
            return ks[-1]
    else:
        return ks[0]
dd3 = dienst_morgen_p5(dd2)
print "De dienst voor person5 overmorgen is %s" % (dd3)
del overzicht[dd3]
ks = list(overzicht)
print overzicht

def dienst_morgen_p1(ee2): #person1 overmorgen
    if ee2 == 5:
        if len(ks) >= 3:
            return ks[2]
        else:
            return ks[-1]
    elif ee2 == 4:
        if len(ks) >= 2:
            return ks[1]
        else:
            return ks[-1]
    else:
        return ks[0]
ee3 = dienst_morgen_p1(ee2)
print "De dienst voor person1 overmorgen is %s" % (ee3)
del overzicht[ee3]
ks = list(overzicht)
print overzicht