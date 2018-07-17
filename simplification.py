#!/usr/bin/python
# -*-coding: utf-8 -*
import fonction
import sys

class Resolveur:
    """Classe définissant les différentes puissances"""

    def __init__(self, equation):
        self.equation = equation
        self.zero = []
        self.un = []
        self.deux = []
        self.total = {"zero": 0, "un": 0, "deux": 0}
    
    def parse(self):
        egal = self.equation.find('=')        
        gauche = self.equation[:egal-1]
        droite = self.equation[egal+2:]
        tab1 = fonction.parse(gauche)
        tab2 = fonction.parse(droite)
        for x in tab1:
            if x[-1] == '0':
                try:
                    nb = eval(x[:x.find('*')])
                    self.zero.append(nb)
                except:
                    print("Erreur equation")
                    sys.exit(0)
            elif x[-1] == '1':
                try:
                    nb = eval(x[:x.find('*')])                   
                    self.un.append(nb)
                except:
                    print("Erreur equation")
                    sys.exit(0)
            elif x[-1] == '2':
                try:
                    nb = eval(x[:x.find('*')])   
                    self.deux.append(nb)
                except:
                    print("Erreur equation")
                    sys.exit(0)
            elif x[-1] == '3':
                print("Niveau 3")
                sys.exit(0)
        for x in tab2:
            if x[-1] == '0':
                try:
                    nb = eval(x[:x.find('*')]) * -1
                    self.zero.append(nb)
                except:
                    print("Erreur equation")
                    sys.exit(0)
            elif x[-1] == '1':
                try:
                    nb = eval(x[:x.find('*')]) * -1
                    self.un.append(nb)
                except:
                    print("Erreur equation")
                    sys.exit(0)
            elif x[-1] == '2':
                try:
                    nb = eval(x[:x.find('*')]) * -1
                    self.deux.append(nb)
                except:
                    print("Erreur equation")
                    sys.exit(0)
            else:
                print("The polynomial degree is stricly greater than 2, I can't solve.")
                sys.exit(0)
    
    def simplification(self):
        zero = 0
        un = 0
        deux = 0
        for i in self.zero:
            zero += i
        for i in self.un:
            un += i
        for i in self.deux:
            deux += i
        self.total = {"zero": zero, "un": un, "deux": deux}
        total = fonction.int_to_str(zero, "* X^0 ") +  fonction.int_to_str(un, "* X^1 ") + fonction.int_to_str(deux, "* X^2 ")
        if len(total) > 0:
            total = total + "= 0"
        else:
            print("Tous les nombres reels sont solution")
            sys.exit(0)
        if total[0] == '+':
            total = total[2:]
        print("Reduced form: " + total)

    def resolution(self):
        if (self.total["deux"] != 0 and self.total["un"] == 0 and self.total["zero"] == 0) or (self.total["un"] != 0 and self.total["deux"] == 0 and self.total["zero"] == 0) or (self.total["zero"] != 0 and self.total["deux"] == 0 and self.total["un"] == 0):
            print("Aucune solution")
        if self.total["deux"] != 0:
            discriminant = fonction.discriminant(self.total)
            if discriminant > 0:
                ret = fonction.positif(self.total, discriminant)
                affichage = "Polynomial degree: 2\nDiscriminant is strictly positive, the two solutions are:\n{0}\n{1}".format(ret[0], ret[1])
                print(affichage)
            elif discriminant < 0:
                ret = fonction.negatif(self.total, discriminant)
                affichage = "Polynomial degree: 2\nDiscriminant is strictly negative, the two solutions complexe are:\n{0}\n{1}".format(ret[0], ret[1])
                print(affichage)
            else:
                ret = fonction.nul(self.total, discriminant)
                affichage = "Polynomial degree: 2\nDiscriminant is equal to zero, the solution is:\n{0}".format(ret)
                print(affichage)
        elif self.total["deux"] == 0 and self.total["un"] != 0:
            ret = fonction.premier(self.total)
            affichage = "Polynomial degree: 1\nThe solution is:\n{0}".format(ret)
            print(affichage)

                   

