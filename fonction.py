#!/usr/bin/python
# -*-coding: utf-8 -*
import math

def parse(chaine):
    tab = []
    while True:
        val = chaine.find('^')
        if val == -1:
            break
        else:
            tab.append(chaine[:val+2])
            chaine = chaine[val+2:]
    return (tab)

def int_to_str(val, puissance):
    ret = str()
    if val > 0:
        ret = '+' + ' ' + str(val) + ' ' + puissance
    elif val < 0:
        ret = '-' + ' ' + str(val*-1) + ' ' + puissance
    return ret

def premier(total):
    ret = (total["zero"] * -1) / float(total["un"])
    return ret

def discriminant(total):
    ret = (total["un"] * total["un"]) - (4 * total["deux"] * total["zero"])
    return ret

def positif(total, discriminant):
    un = ((total["un"] * -1) + (math.sqrt(discriminant) * -1)) / float(total["deux"] * 2)
    deux = ((total["un"] * -1) + (math.sqrt(discriminant))) / float(total["deux"] * 2)
    return un, deux

def negatif(total, discriminant):
    un = "(-{0} - i√{1}) / {2}".format(total["un"], discriminant, total["deux"] * 2)
    deux = "(-{0} + i√{1}) / {2}".format(total["un"], discriminant, total["deux"] * 2)
    return un, deux

def nul(total, discriminant):
    ret = (total["un"] * -1) / float(total["deux"] * 2)
    return ret
